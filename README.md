# ReguWatch — Daily Website Change Monitor (Text + Links) (FOR EVER FREE)

> Zero-install, GitHub-Actions-basierter Watchdog für regulatorische/Standard-Webseiten:  
> prüft **einmal täglich** auf **Textänderungen** und **neue/entfernte Links**, erzeugt ein **Daily Summary** (Markdown im Repo) **und** ein Daily-Issue (E-Mail/Push über GitHub).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](#license)
[![GitHub Actions](https://img.shields.io/badge/CI-GitHub%20Actions-informational)](#-wie-es-funktioniert)
[![Made for GitHub UI](https://img.shields.io/badge/No%20install-browser%20only-success)](#-quick-start)

---

## ✨ Features

- **Täglich 1x** prüfen (Cron, GitHub Actions)
- **Text-Diff** (kompakt, ±8 Zeilen Kontext) & **Link-Diff** (neu/entfernt)
- **Daily Summary** als Markdown: `reports/YYYY-MM-DD/daily-summary.md`
- **Daily Issue**: „ReguWatch Daily Summary YYYY-MM-DD“ (triggert GitHub E-Mail/Push)
- **Keine Installation**: Monitore pflegst du rein über **GitHub Issues (Formular)**
- **History** über Git (Snapshots in `/snapshots`)

---

## 🚀 Quick Start

1. **Repo forken/klonen oder neu erstellen.**  
   Lege dann diese Dateien wie folgt an:
   - `reguwatch.config.json`
   - `.github/ISSUE_TEMPLATE/reguwatch.yml`
   - `.github/workflows/reguwatch.yml`
   - `.github/scripts/check.py`

2. **GitHub Actions aktivieren**  
   `Settings → Actions → General`  
   - **Allow all actions**  
   - **Workflow permissions → Read and write permissions**

3. **Monitore hinzufügen (dein UI)**  
   `Issues → New issue → "Add/Update a page to watch"` ausfüllen:  
   - **Short name**: z. B. `MDCG Guidance`  
   - **URL**: komplette Adresse  
   - **Pausieren**: Label `reguwatch` entfernen  
   - **Entfernen**: Issue schließen

4. **Ersten Lauf starten**  
   `Actions → ReguWatch (Daily) → Run workflow`  
   Ergebnis:  
   - `reports/YYYY-MM-DD/daily-summary.md`  
   - Issue **"ReguWatch Daily Summary YYYY-MM-DD"**

---

## 🔔 E-Mail Alerts setzen (nativ über GitHub)

Du bekommst **automatisch E-Mails**, wenn das Daily-Issue angelegt/aktualisiert wird:

1. **Notifications aktivieren**  
   - Profilbild → `Settings → Notifications`  
   - **Email**: „Send notifications to email“ anhaken  
   - Primäre E-Mail verifizieren (Tab **Emails**)

2. **Repo beobachten**  
   - In diesem Repo oben: **Watch → All Activity**

3. (Optional) **Push aufs Handy**  
   - GitHub Mobile App installieren und Benachrichtigungen aktivieren

Fertig – keine SMTP-Konfiguration nötig.

---

## ➕ Empfohlene Start-Monitore

Lege je einen Eintrag als Issue an (Short name + URL):

- **FDA Medical Devices** — https://www.fda.gov/medical-devices  
- **FDA Guidance (Device Advice)** — https://www.fda.gov/medical-devices/device-advice-comprehensive-regulatory-assistance/guidance-documents-medical-devices-and-radiation-emitting-products  
- **MDCG Guidance** — https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en  
- **EU MDR – New Regulations** — https://health.ec.europa.eu/medical-devices-sector/new-regulations_en  
- **EU Directives (Medical Devices)** — https://health.ec.europa.eu/medical-devices-sector/directives_en  
- **EU In Vitro Diagnostics** — https://health.ec.europa.eu/medical-devices-sector/vitro-diagnostics_en  
- **EU EUDAMED** — https://health.ec.europa.eu/medical-devices-sector/eudamed_en  
- **EU Guidance & Useful Info** — https://health.ec.europa.eu/medical-devices-sector/guidance-and-useful-information_en  
- **EU Coordination & Governance** — https://health.ec.europa.eu/medical-devices-sector/coordination-and-governance_en  
- **IEC Just Published** — https://webstore.iec.ch/en/just-published/  
- **ISO Insights (Standards World)** — https://www.iso.org/insights/standards-world

---

## 🧠 Wie es funktioniert

- Der Workflow läuft **täglich** (Standard: 05:00 UTC ≈ 07:00 Berlin Sommerzeit)  
- Für jede URL speichert er Snapshots in `/snapshots`:
  - **HTML** (`.html`), **sichtbarer Text** (`.txt`), **Links** (`.links.json`)
- Vergleiche:
  - **Text-Diff** mit Unified-Diff (kompakt, max. ~100 Zeilen)
  - **Links**: Listen neu/entfernt
- Ausgabe:
  - **Markdown-Report** `reports/YYYY-MM-DD/daily-summary.md`
  - **Daily-Issue** (E-Mail/Push über GitHub)

---

## ⚙️ Konfiguration

Datei: `reguwatch.config.json`

```json
{
  "profile": "community",
  "profiles": {
    "community": {
      "max_monitors": 150,
      "min_interval_minutes": 10,
      "checks_per_month_cap": 100000,
      "webhook_alert_cap_per_month": 2000
    }
  },
  "notifications": {
    "use_github_issues": true,
    "webhook_url": ""
  },
  "macros": []
}
