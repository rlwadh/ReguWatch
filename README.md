# ReguWatch — Daily Website Change Monitor (Text + Links)

> A GitHub Actions–based watchdog for regulatory and standards websites.  
> Runs **once per day**, detects **text changes** and **new/removed links**, and creates both a **Daily Summary** (Markdown in the repo) and a **Daily Issue** (which triggers GitHub email/push notifications).

---

## ✨ Features

- **Daily run** via GitHub Actions (cron)
- Detects **text changes** (compact diff with ±8 lines of context)
- Detects **link changes** (new and removed URLs listed)
- Generates a **Markdown report**: `reports/YYYY-MM-DD/daily-summary.md`
- Creates a **Daily Issue**: “ReguWatch Daily Summary YYYY-MM-DD”
- **Zero install**: manage monitors entirely through GitHub Issues (UI form)
- **History**: snapshots stored under `/snapshots` (tracked in Git)

---

## 🚀 Quick Start

1. **Set up the repo**  
   Add these files to your repository:  
   - `reguwatch.config.json`  
   - `.github/ISSUE_TEMPLATE/reguwatch.yml`  
   - `.github/workflows/reguwatch.yml`  
   - `.github/scripts/check.py`

2. **Enable GitHub Actions**  
   - Go to `Settings → Actions → General`  
   - Allow all actions  
   - Set workflow permissions to *Read and write permissions*

3. **Add monitors (your UI)**  
   - Go to `Issues → New issue → "Add/Update a page to watch"`  
   - Fill in a **Short name** (e.g. “MDCG Guidance”) and the **URL**  
   - To pause: remove the `reguwatch` label  
   - To remove: close the issue

4. **Run the first check manually**  
   - Go to `Actions → ReguWatch (Daily) → Run workflow`  
   - Results:  
     - `reports/YYYY-MM-DD/daily-summary.md`  
     - A new Issue: “ReguWatch Daily Summary YYYY-MM-DD”

---

## 🔔 Email Alerts (native via GitHub)

You will automatically receive an email whenever the Daily Summary Issue is created or updated:

1. **Enable email notifications**  
   - Profile picture → `Settings → Notifications`  
   - Tick *“Send notifications to email”*  
   - Verify your primary email under **Emails**

2. **Watch this repo**  
   - On the repo page: click **Watch → All Activity**

3. (Optional) **Push on mobile**  
   - Install the GitHub Mobile App and enable notifications

---

## ➕ Recommended Start Monitors

Here are some useful starting points (add one issue per URL):

- FDA Medical Devices — https://www.fda.gov/medical-devices  
- FDA Guidance (Device Advice) — https://www.fda.gov/medical-devices/device-advice-comprehensive-regulatory-assistance/guidance-documents-medical-devices-and-radiation-emitting-products  
- MDCG Guidance — https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en  
- EU MDR – New Regulations — https://health.ec.europa.eu/medical-devices-sector/new-regulations_en  
- EU Directives (Medical Devices) — https://health.ec.europa.eu/medical-devices-sector/directives_en  
- EU In Vitro Diagnostics — https://health.ec.europa.eu/medical-devices-sector/vitro-diagnostics_en  
- EU EUDAMED — https://health.ec.europa.eu/medical-devices-sector/eudamed_en  
- EU Guidance & Useful Info — https://health.ec.europa.eu/medical-devices-sector/guidance-and-useful-information_en  
- EU Coordination & Governance — https://health.ec.europa.eu/medical-devices-sector/coordination-and-governance_en  
- IEC Just Published — https://webstore.iec.ch/en/just-published/  
- ISO Insights (Standards World) — https://www.iso.org/insights/standards-world  

---

## 🧠 How It Works

- The workflow runs **once per day** (default: 05:00 UTC ≈ 07:00 Berlin during summer)  
- For each monitored URL it saves snapshots under `/snapshots`:  
  - **HTML** (`.html`)  
  - **Visible text** (`.txt`)  
  - **Links** (`.links.json`)  
- Comparison logic:  
  - **Text diff** (compact unified diff, max ~100 lines)  
  - **Links**: lists new and removed URLs  
- Outputs:  
  - **Markdown report** under `reports/YYYY-MM-DD/daily-summary.md`  
  - **Daily Issue** with the same content (triggers email/push)

---

## ⚙️ Configuration

The configuration is stored in `reguwatch.config.json`.  

### Elements explained:
- **profile**: selects which profile to use (e.g. `community`)  
- **max_monitors**: maximum number of watch issues to include  
- **min_interval_minutes**: minimum time gap between checks for the same URL  
- **checks_per_month_cap**: maximum number of checks allowed per month (safety cap)  
- **webhook_alert_cap_per_month**: maximum number of webhook alerts per month  
- **notifications**:  
  - `use_github_issues`: whether to post daily summaries as GitHub Issues  
  - `webhook_url`: optional URL to send alerts to (Slack, Teams, etc.)  
- **macros**: optional filters (e.g. CSS selectors or regex to narrow what is compared)

---

## 🧩 File Structure

reguwatch.config.json
.github/
  ISSUE_TEMPLATE/
    reguwatch.yml
  scripts/
    check.py
  workflows/
    reguwatch.yml
reports/
  YYYY-MM-DD/
    daily-summary.md   ← generated daily
snapshots/
  <hash>.html
  <hash>.txt
  <hash>.links.json
state/
  last_run.json
  monthly_counters.json

---

## 🤝 Contributing

PRs and issues are welcome!
When adding new sources, please use clear short names and always the canonical URL.

---

❤️ Support Our Kindergarten Project

If ReguWatch is useful to you, please consider supporting the
Bildungswerk für Kinder und nachhaltiges Lernen (BKNL):
	•	Donation link: 👉 Donate here : https://bknl.de
Every contribution helps us fund local educational projects for children. Thank you! 🙏

---

📜 License

Apache-2.0 – see LICENSE.
