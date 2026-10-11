# USB Device Control & Monitoring Framework

An endpoint security framework designed to detect USB connections, enforce allowlist policies, automatically block unauthorized storage devices via Windows PnP, and audit file transfers using SHA-256 hashing.

## Tech Stack
- Python 3.x
- WMI & pywin32
- Watchdog (Filesystem Monitoring)
- PowerShell (PnP Device Control)

## Setup & Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt