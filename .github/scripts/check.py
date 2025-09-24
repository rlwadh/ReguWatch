import os, re, json, argparse
import datetime as dt
import pathlib, requests, difflib
from urllib.parse import urljoin, urldefrag
from selectolax.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parents[2]
sites_file = ROOT / "sites.json"
cfg_file = ROOT / "reguwatch.config.json"
snap_dir = ROOT / "snapshots"
state_dir = ROOT / "state"
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

def load_json(p, default):
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            return default
    return default

def save_json(p, obj):
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")

# --- Config
cfg = load_json(cfg_file, {})
profile_name = cfg.get("profile", "community")
profiles = cfg.get("profiles", {})
profile = profiles.get(profile_name, {})
min_interval = int(profile.get("min_interval_minutes", 10))
checks_cap = int(profile.get("checks_per_month_cap", 100000))
webhook_cap = int(profile.get("webhook_alert_cap_per_month", 2000))

# --- State
counters_path = state_dir / "monthly_counters.json"
last_run_path = state_dir / "last_run.json"
counters = load_json(counters_path, {"month": month_key(), "checks": 0, "webhooks": 0})
last_run = load_json(last_run_path, {})  # {url: ISO8601}

if counters.get("month") != month_key():
    counters = {"month": month_key(), "checks": 0, "webhooks": 0}

def safe_name(s):
    return "".join(c if c.isalnum() else "_" for c in s)[:150]

def extract_text_and_links(html, base_url):
    tree = HTMLParser(html)
    text = tree.body.text(separator="\n", strip=True) if tree.body else tree.text(separator="\n", strip=True)
    links = set()
    for a in tree.css('a[href]') if hasattr(tree, "css") else []:
        href = a.attributes.get('href','').strip()
        if not href:
            continue
        href = urljoin(base_url, href)
        href, _ = urldefrag(href)
        links.add(href)
    return text, sorted(links)

def limited_unified_diff(old, new, name, context=8, max_lines=100):
    diff_lines = list(difflib.unified_diff(
        old.splitlines(), new.splitlines(),
        fromfile=f"{name} (old)", tofile=f"{name} (new)", lineterm=""
    ))
    if len(diff_lines) > max_lines:
        head = diff_lines[:max_lines//2]
        tail = diff_lines[-max_lines//2:]
        diff_lines = head + ["... (diff truncated) ..."] + tail
    return "\n".join(diff_lines)

def fetch_if_due(url):
    # Checks-Cap
    if checks_cap >= 0 and counters["checks"] >= checks_cap:
        return None, f"[SKIPPED checks_cap reached: {checks_cap}]"
    # Min-Intervall pro URL
    last = last_run.get(url)
    if last:
        try:
            last_dt = dt.datetime.fromisoformat(last.replace("Z",""))
            delta = (now_utc() - last_dt).total_seconds() / 60.0
            if delta < min_interval:
                return None, f"[SKIPPED min_interval {min_interval}m; last {delta:.1f}m ago]"
        except Exception:
            pass
    try:
        r = requests.get(url, timeout=60, headers={"User-Agent": "reguwatch/1.2"})
        r.raise_for_status()
        counters["checks"] += 1
        last_run[url] = now_utc().isoformat()+"Z"
        return r.text, None
    except Exception as ex:
        counters["checks"] += 1
        last_run[url] = now_utc().isoformat()+"Z"
        return f"[ERROR fetching {url}]: {ex}", None

def main(is_daily: bool):
    # Summary-Verzeichnis heute
    summary_dir = reports_dir / today_str()
    summary_dir.mkdir(exist_ok=True)

    if not sites_file.exists():
        (summary_dir / "daily-summary.md").write_text("# ReguWatch — Daily Summary\n\nKeine Monitore konfiguriert.\n", encoding="utf-8")
        return False

    entries = json.loads(sites_file.read_text(encoding="utf-8"))
    any_changes = False
    changes_md = []

    for e in entries:
        name = e.get("name") or e["url"]
        url = e["url"]
        base_path = snap_dir / safe_name(url)
        html_path = base_path.with_suffix(".html")
        text_path = base_path.with_suffix(".txt")
        links_path = base_path.with_suffix(".links.json")

        new_html, skip_reason = fetch_if_due(url)
        if skip_reason:
            continue

        # alte Stände
        old_html = html_path.read_text(encoding="utf-8") if html_path.exists() else ""
        old_text = text_path.read_text(encoding="utf-8") if text_path.exists() else ""
        old_links = load_json(links_path, [])

        # neue Stände
        new_text, new_links = extract_text_and_links(new_html, url)

        # Vergleiche
        text_changed = (new_text != old_text)
        added_links = sorted(list(set(new_links) - set(old_links)))
        removed_links = sorted(list(set(old_links) - set(new_links)))
        links_changed = bool(added_links or removed_links)

        if text_changed or links_changed:
            any_changes = True
            text_diff = limited_unified_diff(old_text, new_text, name, context=8, max_lines=100) if text_changed else "_(kein Text-Diff)_"
            links_block = "_(keine Link-Änderungen)_"
            if links_changed:
                parts = []
                if added_links:
                    parts.append("**Neu hinzugefügte Links:**\n" + "\n".join(f"- {u}" for u in added_links))
                if removed_links:
                    parts.append("**Entfernte Links:**\n" + "\n".join(f"- {u}" for u in removed_links))
                links_block = "\n\n".join(parts)

            changes_md.append(f"""### {name}
**Seite:** {url}

**Änderungen:** {"Text" if text_changed else ""}{" & " if (text_changed and links_changed) else ""}{"Links" if links_changed else ""}

**Vorher/Nachher (kompakter Text-Diff):**
