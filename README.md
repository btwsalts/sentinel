# 🛡️ Sentinel

### Mini SIEM · Log Analysis · Threat Detection

> A lightweight web-based SIEM for analyzing logs, detecting suspicious patterns, and presenting security alerts through a local dashboard.

## What is Sentinel?

Sentinel is a learning-focused mini SIEM. It accepts an authorized log file, parses security events, applies detection rules, and turns matching activity into alerts.

Current detections:
- Possible brute-force activity from repeated failed logins.
- Repeated error-level events from the same source IP.

## Features
- Log file upload
- Structured log parsing
- Rule-based detection
- Security summary dashboard
- Source IP tracking
- Severity levels
- Event and alert views
- Included sample log for testing
- Local-only operation

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend and detection logic |
| Flask | Web application/API |
| HTML/CSS | Dashboard |
| JavaScript | Uploads and dynamic rendering |
| Regular expressions | Log parsing and pattern matching |

## Project Structure

```text
sentinel/
├── app.py
├── requirements.txt
├── analyzer/
│   ├── __init__.py
│   ├── parser.py
│   └── rules.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
├── logs/
│   └── sample.log
└── README.md
```

## How It Works

```text
Log File
   ↓
Parser
   ↓
Normalized Events
   ↓
Detection Rules
   ↓
Alerts
   ↓
Web Dashboard
```

### Detection logic

**Possible brute force:** five or more failed-login events from the same IP within 60 seconds create a HIGH alert.

**Repeated server errors:** three or more error-level events from the same IP create a MEDIUM alert.

These are intentionally simple educational rules, not production-grade detections.

## Run Locally

```bash
git clone https://github.com/btwsalts/sentinel.git
cd sentinel
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

Open `http://127.0.0.1:5000`.

## Test It

Upload `logs/sample.log` through the dashboard. The included sample contains failed-login and server-error events designed to trigger the current detection rules.

## Security Note

Use Sentinel with logs you own or are authorized to analyze. The project is intended for cybersecurity education, home labs, and authorized defensive testing.

## Limitations
- The parser currently expects the included simple log format.
- Detection rules are intentionally basic.
- Events are analyzed in memory and are not yet stored in a database.
- There is no authentication for the local dashboard.
- This is not intended to replace a production SIEM.

## Roadmap
- [ ] SQLite event storage
- [ ] More log formats
- [ ] Detection rule management
- [ ] Event timeline charts
- [ ] Search and filtering
- [ ] Alert acknowledgement
- [ ] CSV/JSON report export
- [ ] Authentication
- [ ] Docker deployment
- [ ] Automated tests

## What I Practiced
- Python backend development
- Flask APIs
- Log parsing
- Regular expressions
- Rule-based threat detection
- Security event normalization
- Dashboard development
- File uploads
- Frontend/backend communication

## Author

Built by **btwsalts** as a cybersecurity and software-engineering learning project.