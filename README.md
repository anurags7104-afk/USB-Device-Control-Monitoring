# USB Device Control & Monitoring Framework

## Project Overview

The USB Device Control & Monitoring Framework is a Python-based Windows security project that detects USB storage device connections, records device events, and monitors file activity for security auditing.

The project demonstrates endpoint monitoring concepts, structured event logging, file integrity hashing, and configurable device policies.

## Objectives

- Detect USB storage device connections.
- Record device information and security alerts.
- Apply configurable device authorization policies.
- Monitor file creation, modification, and deletion.
- Calculate SHA-256 hashes for accessible file contents during auditing.
- Maintain logs for testing and security analysis.

## Features

- USB device detection using Windows Management Instrumentation (WMI).
- USB event logging in JSONL format.
- Device identification using available vendor and product IDs.
- File activity monitoring using Watchdog.
- SHA-256 file hashing.
- Configurable policy settings.
- Testing and report-generation support.

**Implementation note:** Automatic USB blocking and file auditing on a physical USB volume have not yet been verified. Detection and alerting should not be interpreted as proof that a device was blocked.

## Technology Stack

- Python 3.x
- WMI
- pywin32
- Watchdog
- PowerShell
- JSON and JSONL

## Project Structure

```text
USB-Device-Control-Monitoring/
├── main.py
├── policy_engine.py
├── file_auditor.py
├── reporter.py
├── generate_report.py
├── config.json
├── requirements.txt
├── README.md
└── docs/
    ├── USB_Device_Control_Monitoring_Test_Report.docx
    └── USB_Device_Control_Monitoring_Final_Presentation.pptx
```

## Requirements

- Windows
- A compatible Python installation
- The dependencies listed in `requirements.txt`

## Installation

Clone the repository:

```bash
git clone https://github.com/anurags7104-afk/USB-Device-Control-Monitoring.git
cd USB-Device-Control-Monitoring
```

Create and activate a virtual environment in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Running the Application

Start USB monitoring:

```powershell
python main.py
```

Keep the application running while connecting a test USB storage device. Review the application output and generated event logs.

Use only devices and systems you are authorized to monitor.

## Testing Status

| Test | Status |
|---|---|
| Dependency installation and imports | Passed |
| USB device detection | Passed |
| USB event logging | Passed |
| Local-folder file creation monitoring | Passed |
| Local-folder file modification monitoring | Passed |
| Local-folder file deletion monitoring | Passed |
| File hashing for accessible file contents | Observed during local testing |
| File auditing on a physical USB volume | Not yet verified |
| Automatic blocking of unauthorized USB devices | Not yet verified |

## Documentation

The `docs/` directory contains the testing report and final presentation.

## Future Improvements

- Verify file auditing on a mounted USB volume.
- Safely test and validate device-blocking behavior.
- Improve handling of duplicate Windows device events.
- Add sanitized screenshots and additional test evidence.
- Improve reporting and device authorization controls.

## Author

Anurag Singh

## Disclaimer

This project is developed for educational purposes and authorized cybersecurity testing. Do not use device-control features on systems without appropriate permission.