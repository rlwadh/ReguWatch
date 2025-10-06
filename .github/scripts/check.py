import os, re, json, argparse
import datetime as dt
import pathlib, requests, difflib
from urllib.parse import urljoin, urldefrag
from selectolax.parser import HTMLParser

# ------------ Paths ------------
ROOT = pathlib.Path(__file__).resolve().parents[2]
sites_file  = ROOT / "sites.json"
cfg_file    = ROOT / "reguwatch.config.json"
snap_dir    = ROOT / "snapshots"
state_dir   = ROOT / "state"
reports_dir = ROOT / "reports"
snap_dir.mkdir(exist_ok=True)
state_dir.mkdir(exist_ok=True)
reports_dir.mkdir(exist_ok=True)

def now_utc():
    return dt.datetime.utcnow()

def today_str():
    return now_utc().strftime("%Y-%m-%d")

def month_key(ts=None):
    ts = ts or now_utc()
    return ts.strftime("%Y-%m")

def load_json(p: pathlib.Path, default):
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            return default
    return default

def save_json(p: pathlib.Path, obj):
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")

def safe_name(s: str) -> str:
    return "".join(c if c.isalnum() else "_" for c in s)[:150]

# ------------ Config & State ------------
cfg = load_json(cfg_file, {})
profile_name = cfg.get("profile", "community")
profiles  = cfg.get("profiles", {})
profile   = profiles.get(profile_name, {})
min_interval = int(profile.get("min_interval_minutes", 10))
checks_cap   = int(profile.get("checks_per_month_cap", 100000))
# Optional behavior switches
summary_mode = cfg.get("summary_mode", "full")  # "full" or "compact" (default to full for regulatory)
# (webhook_cap unused here)

counters_path = state_dir / "monthly_counters.json"
last_run_path = state_dir / "last_run.json"
counters = load_json(counters_path, {"month": month_key(), "checks": 0, "webhooks": 0})
last_run = load_json(last_run_path, {})  # {url: ISO8601}

if counters.get("month") != month_key():
    counters = {"month": month_key(), "checks": 0, "webhooks": 0}

# ------------ Extraction & fetching ------------
def extract_text_and_links(html: str, base_url: str):
    """
    Return visible text + absolute links (no fragments).
    """
    tree = HTMLParser(html)
    # Visible text from <body>; fallback: whole doc text
    text = tree.body.text(separator="\n", strip=True) if tree.body else tree.text(separator="\n", strip=True)

    links = set()
    # Only http/https (ignore mailto:, javascript:)
    for a in (tree.css('a[href]') if hasattr(tree, "css") else []):
        href = (a.attributes.get('href') or "").strip()
        if not href:
            continue
        if href.lower().startswith(("http://", "https://")) or href.startswith("/"):
            absu, _ = urldefrag(urljoin(base_url, href))
            links.add(absu)
    return text, sorted(links)

def fetch_if_due(url: str):
    """
    Fetch page while honoring monthly cap and per-URL min interval.
    Returns (html, skip_reason).
    """
    if checks_cap >= 0 and counters["checks"] >= checks_cap:
        return None, f"[SKIPPED checks_cap reached: {checks_cap}]"
    last = last_run.get(url)
    if last:
        try:
            last_dt = dt.datetime.fromisoformat(last.replace("Z", ""))
            delta_min = (now_utc() - last_dt).total_seconds() / 60.0
            if delta_min < min_interval:
                return None, f"[SKIPPED min_interval {min_interval}m; last {delta_min:.1f}m ago]"
        except Exception:
            pass
    try:
        r = requests.get(url, timeout=60, headers={"User-Agent": "reguwatch/1.4"})
        r.raise_for_status()
        counters["checks"] += 1
        last_run[url] = now_utc().isoformat() + "Z"
        return r.text, None
    except Exception as ex:
        counters["checks"] += 1
        last_run[url] = now_utc().isoformat() + "Z"
        return f"[ERROR fetching {url}]: {ex}", None

# ------------ Diffs ------------
def full_unified_diff(old: str, new: str, name: str):
    """
    Untruncated unified diff (line-by-line) for text changes.
    """
    return "\n".join(difflib.unified_diff(
        old.splitlines(), new.splitlines(),
        fromfile=f"{name} (old)", tofile=f"{name} (new)", lineterm=""
    ))

# (We keep compact helpers available; summary_mode can switch later if needed)
def _clip_block(lines, start, end, max_lines=3):
    block = lines[start:end]
    if len(block) > max_lines:
        head = block[:max_lines]
        head.append("…")
        return head
    return block

from difflib import SequenceMatcher
def make_compact_change_snippet(old_text: str, new_text: str, max_ctx=3):
    old_lines = old_text.splitlines()
    new_lines = new_text.splitlines()
    sm = SequenceMatcher(None, old_lines, new_lines, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            continue
        i_start = max(i1 - 1, 0)
        i_end   = min(i2 + 1, len(old_lines))
        j_start = max(j1 - 1, 0)
        j_end   = min(j2 + 1, len(new_lines))
        old_snip = _clip_block(old_lines, i_start, i_end, max_ctx) if tag in ('replace', 'delete') else None
        new_snip = _clip_block(new_lines, j_start, j_end, max_ctx) if tag in ('replace', 'insert') else None
        return (old_snip, new_snip)
    return (None, None)

def fmt_quote_block(lines):
    if not lines:
        return None
    return "\n".join(["> " + l for l in lines])

# ------------ Main ------------
def main(is_daily: bool):
    summary_dir = reports_dir / today_str()
    summary_dir.mkdir(exist_ok=True)

    if not sites_file.exists():
        (summary_dir / "daily-summary.md").write_text("# ReguWatch — Daily Summary\n\nNo monitors configured.\n", encoding="utf-8")
        return False

    entries = json.loads(sites_file.read_text(encoding="utf-8"))
    any_changes = False
    changes_md = []

    for e in entries:
        name = e.get("name") or e["url"]
        url  = e["url"]

        base_path = snap_dir / safe_name(url)
        html_path = base_path.with_suffix(".html")
        text_path = base_path.with_suffix(".txt")
        links_path= base_path.with_suffix(".links.json")

        new_html, skip_reason = fetch_if_due(url)
        if skip_reason:
            continue

        # Previous
        old_html = html_path.read_text(encoding="utf-8") if html_path.exists() else ""
        old_text = text_path.read_text(encoding="utf-8") if text_path.exists() else ""
        old_links = load_json(links_path, [])

        # New
        new_text, new_links = extract_text_and_links(new_html, url)

        # Link & text comparisons
        text_changed = (new_text != old_text)
        added_links  = sorted(list(set(new_links) - set(old_links)))
        removed_links= sorted(list(set(old_links) - set(new_links)))
        links_changed= bool(added_links or removed_links)

        if text_changed or links_changed:
            any_changes = True
            section_lines = [f"### {name}", f"**Page:** [{url}]({url})"]

            if summary_mode.lower() == "full" and text_changed:
                # Full, untruncated unified diff
                diff_text = full_unified_diff(old_text, new_text, name)
                section_lines += [
                    "**Changes:** " + ("Text & Links" if links_changed else "Text"),
                    "",
                    "**Full text diff:**",
                    "```",
                    diff_text if diff_text.strip() else "(no textual diff produced)",
                    "```"
                ]
            elif text_changed:
                # Fallback compact (not default)
                old_snip, new_snip = make_compact_change_snippet(old_text, new_text, max_ctx=3)
                old_block = fmt_quote_block(old_snip)
                new_block = fmt_quote_block(new_snip)
                section_lines += ["**Changes:** " + ("Text & Links" if links_changed else "Text")]
                if old_block and new_block:
                    section_lines += ["**Before (context):**", old_block, "**After (context):**", new_block]
                elif new_block and not old_block:
                    section_lines += ["**New (context):**", new_block]
                elif old_block and not new_block:
                    section_lines += ["**Removed (context):**", old_block]

            if links_changed:
                if not text_changed:
                    section_lines += ["**Changes:** Links"]  # ensure label if only links changed
                if added_links:
                    section_lines += ["", "**Added links (all):**"] + [f"- {u}" for u in added_links]
                if removed_links:
                    section_lines += ["", "**Removed links (all):**"] + [f"- {u}" for u in removed_links]

            section_lines.append("")  # spacing
            changes_md.append("\n".join(section_lines))

        # Always update snapshots for audit trail
        html_path.write_text(new_html, encoding="utf-8")
        text_path.write_text(new_text, encoding="utf-8")
        save_json(links_path, new_links)

    # Save state
    save_json(state_dir / "monthly_counters.json", counters)
    save_json(state_dir / "last_run.json", last_run)

    # Write summary
    summary = ["# ReguWatch — Daily Summary", f"Date (UTC): {today_str()}", ""]
    if changes_md:
        summary += ["## Changes today", ""] + changes_md
    else:
        summary += ["No changes detected."]

    # Persist outputs
    (ROOT / "last_diff.txt").write_text("\n\n".join(changes_md) if changes_md else "No changes.", encoding="utf-8")
    (summary_dir / "daily-summary.md").write_text("\n".join(summary), encoding="utf-8")
    return any_changes

# ------------ Entrypoint ------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--daily", action="store_true", help="daily run")
    args = parser.parse_args()
    changed = main(is_daily=args.daily)
    gho = os.environ.get("GITHUB_OUTPUT", "")
    if gho:
        with open(gho, "a") as f:
            f.write(("changed=1\n" if changed else "changed=0\n"))
            f.write("state_written=1\n")
