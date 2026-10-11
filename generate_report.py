import os
import glob
import base64

def get_image_base64(filepath):
    if os.path.exists(filepath):
        with open(filepath, "rb") as f:
            return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"
    return None

# Find screenshots automatically in the folder
ss1_path = "Screenshot 2026-10-01 202235.png"
ss2_path = "Screenshot 2026-10-01 202206.png"

# Fallback: search for any .png files if exact names differ
if not os.path.exists(ss1_path) or not os.path.exists(ss2_path):
    pngs = glob.glob("*.png")
    if len(pngs) >= 2:
        ss1_path = pngs[0]
        ss2_path = pngs[1]

img1_b64 = get_image_base64(ss1_path)
img2_b64 = get_image_base64(ss2_path)

img1_html = f'<img src="{img1_b64}" class="screenshot" alt="Detection Console">' if img1_b64 else '<div class="placeholder">[Screenshot 1: Hardware Detection & Auto-Block]</div>'
img2_html = f'<img src="{img2_b64}" class="screenshot" alt="Audit Report">' if img2_b64 else '<div class="placeholder">[Screenshot 2: reporter.py Audit Output]</div>'

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Anurag_Singh_BTCE24O1013_Project_Report</title>
<style>
    @page {{
        size: A4;
        margin: 20mm 15mm 20mm 15mm;
    }}
    body {{
        font-family: 'Segoe UI', Arial, sans-serif;
        line-height: 1.55;
        color: #222;
        background-color: #f8fafc;
        margin: 0;
        padding: 0;
    }}
    .document-container {{
        max-width: 820px;
        margin: 20px auto;
        background: #fff;
        padding: 40px 50px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        border-radius: 6px;
    }}
    @media print {{
        body {{ background: #fff; }}
        .document-container {{
            max-width: 100%;
            margin: 0;
            padding: 0;
            box-shadow: none;
        }}
        .page-break {{ page-break-before: always; }}
    }}
    .header-box {{
        border-bottom: 3px solid #1e3a8a;
        padding-bottom: 15px;
        margin-bottom: 25px;
    }}
    h1 {{
        color: #0f172a;
        font-size: 26px;
        margin: 0 0 8px 0;
        letter-spacing: -0.5px;
    }}
    .subtitle {{
        color: #2563eb;
        font-size: 16px;
        font-weight: 600;
        margin: 0 0 15px 0;
    }}
    .meta-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 8px 20px;
        background: #f1f5f9;
        padding: 12px 18px;
        border-radius: 6px;
        font-size: 13.5px;
    }}
    .meta-grid div strong {{ color: #1e293b; }}
    h2 {{
        color: #1e3a8a;
        font-size: 18px;
        border-bottom: 1.5px solid #e2e8f0;
        padding-bottom: 5px;
        margin-top: 25px;
        margin-bottom: 10px;
    }}
    h3 {{
        color: #334155;
        font-size: 15px;
        margin-top: 15px;
        margin-bottom: 6px;
    }}
    p, li {{
        font-size: 13.5px;
        color: #334155;
    }}
    ul, ol {{
        padding-left: 20px;
        margin-top: 6px;
        margin-bottom: 10px;
    }}
    li {{ margin-bottom: 4px; }}
    table {{
        width: 100%;
        border-collapse: collapse;
        margin: 12px 0;
        font-size: 12.5px;
    }}
    th, td {{
        border: 1px solid #cbd5e1;
        padding: 7px 10px;
        text-align: left;
    }}
    th {{
        background: #f8fafc;
        color: #1e293b;
        font-weight: 600;
    }}
    pre {{
        background: #0f172a;
        color: #e2e8f0;
        padding: 12px;
        border-radius: 6px;
        font-family: Consolas, 'Courier New', monospace;
        font-size: 11.5px;
        line-height: 1.4;
        overflow-x: auto;
        margin: 10px 0;
    }}
    .screenshot-card {{
        margin: 15px 0;
        border: 1px solid #e2e8f0;
        border-radius: 6px;
        padding: 10px;
        background: #fafafa;
        text-align: center;
    }}
    .screenshot {{
        max-width: 100%;
        height: auto;
        border: 1px solid #cbd5e1;
        border-radius: 4px;
    }}
    .caption {{
        font-size: 12px;
        color: #64748b;
        margin-top: 6px;
        font-weight: 500;
    }}
    .badge {{
        display: inline-block;
        padding: 2px 8px;
        font-size: 11px;
        font-weight: 600;
        border-radius: 4px;
        background: #dbeafe;
        color: #1e40af;
    }}
</style>
</head>
<body>

<div class="document-container">
    <div class="header-box">
        <h1>USB Device Control & Monitoring Framework</h1>
        <div class="subtitle">Comprehensive Endpoint Hardware Security & Threat Auditing Report</div>
        <div class="meta-grid">
            <div><strong>Candidate Name:</strong> Anurag Singh</div>
            <div><strong>Enrollment Number:</strong> BTCE24O1013</div>
            <div><strong>Internship Domain:</strong> Cybersecurity / Endpoint Security</div>
            <div><strong>Host Organization:</strong> Unified Mentor</div>
            <div><strong>Assigned Supervisor:</strong> Technical Mentor (Unified Mentor)</div>
            <div><strong>Submission Date:</strong> October 1, 2026</div>
        </div>
    </div>

    <h2>1. Executive Summary & Abstract</h2>
    <p>
        Universal Serial Bus (USB) peripherals represent a prevalent physical attack vector in enterprise network perimeters. Despite endpoint antivirus suites, unauthorized USB drives can facilitate rapid data exfiltration, malware staging, and physical keystroke injection attacks. This project presents the design and deployment of an automated <strong>USB Device Control & Monitoring Framework</strong> developed in Python for Windows endpoints. 
    </p>
    <p>
        The framework intercepts hardware connection events in real time using Windows Management Instrumentation (WMI), parses hardware identities (Vendor ID, Product ID, Serial Number), and enforces an allowlist policy. Unauthorized devices are programmatically neutralized via Windows Plug-and-Play (PnP) cmdlets, while authorized drives are audited in real time with SHA-256 cryptographic hashing to maintain a tamper-evident chain of custody.
    </p>

    <h2>2. Problem Statement & Practical Motivation</h2>
    <ul>
        <li><strong>Data Exfiltration:</strong> Malicious or negligent insiders can extract gigabytes of confidential trade secrets onto unmonitored flash drives within seconds.</li>
        <li><strong>Malware Introduction:</strong> Offline air-gapped endpoints are frequently breached via infected USB drives carrying worms, ransomware, or trojans.</li>
        <li><strong>Rogue Microcontroller Implants:</strong> Tools such as BadUSB register as trusted input devices to inject high-speed keystroke payloads.</li>
        <li><strong>Lack of Auditing Visibility:</strong> Default operating systems do not provide fine-grained, forensic logs connecting physical hardware IDs to copied files.</li>
    </ul>

    <h2>3. System Architecture & Workflow</h2>
    <pre>
[ Physical USB Port ] ---> [ WMI Notification: Win32_PnPEntity ]
                                        |
                                        v
                 [ Hardware Fingerprinting (VID, PID, Serial) ]
                                        |
                 +----------------------+----------------------+
                 |                                             |
        [ Allowlist Match ]                           [ Policy Violation ]
                 |                                             |
                 v                                             v
     [ Status: AUTHORIZED ]                       [ Status: UNAUTHORIZED_BLOCKED ]
                 |                                             |
                 v                                             v
     [ Filesystem Auditing ]                      [ Disable-PnpDevice (PowerShell) ]
  (Watchdog + SHA-256 Checksums)                               |
                 |                                             v
                 +----------------------+----------------------+
                                        |
                                        v
                        [ Tamper-Evident Audit Logging ]
                               (logs/usb_events.jsonl)
                                        |
                                        v
                          [ Incident Report (reporter.py) ]
    </pre>

    <div class="page-break"></div>

    <h2>4. Core Modules & Deliverables Breakdown</h2>
    <table>
        <thead>
            <tr>
                <th>Module Name</th>
                <th>Source File</th>
                <th>Functional Responsibility</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Listener & Orchestrator</strong></td>
                <td><code>main.py</code></td>
                <td>Initializes WMI notification query, extracts VID/PID, isolates mass storage from input peripherals, dispatches enforcement.</td>
            </tr>
            <tr>
                <td><strong>Policy Engine</strong></td>
                <td><code>policy_engine.py</code></td>
                <td>Evaluates hardware attributes against <code>config.json</code>; executes PowerShell remediation cmdlets.</td>
            </tr>
            <tr>
                <td><strong>File Movement Auditor</strong></td>
                <td><code>file_auditor.py</code></td>
                <td>Hooks into mounted removable volumes; records file creation, deletion, renaming, and computes SHA-256 hashes.</td>
            </tr>
            <tr>
                <td><strong>Incident Reporter</strong></td>
                <td><code>reporter.py</code></td>
                <td>Aggregates recorded JSON Lines audit trails into a clean, human-readable terminal table.</td>
            </tr>
            <tr>
                <td><strong>Policy Configuration</strong></td>
                <td><code>config.json</code></td>
                <td>Defines approved hardware profiles and global enforcement behaviors.</td>
            </tr>
        </tbody>
    </table>

    <h2>5. Learning Outcomes Achieved</h2>
    <ol>
        <li><strong>OS & Hardware Interfacing:</strong> Mastered the Windows Plug-and-Play (PnP) lifecycle and event-driven querying via <code>Win32_PnPEntity</code>.</li>
        <li><strong>Threat Analysis:</strong> Evaluated physical threat vectors including BadUSB HID spoofing, autorun propagation, and insider data exfiltration.</li>
        <li><strong>Endpoint Hardening:</strong> Engineered defensive Blue Team mechanisms utilizing automated, native OS-level enforcement.</li>
        <li><strong>Cryptographic Auditing:</strong> Applied SHA-256 integrity verification to file movement tracking, generating forensic-grade evidence trails.</li>
        <li><strong>Zero-Trust Policy Enforcement:</strong> Built and verified a strict allowlist/blocklist ruleset for removable endpoint devices.</li>
    </ol>

    <h2>6. Experimental Testing & Verification Results</h2>
    <p>
        The framework was evaluated on an active Windows endpoint under elevated administrative privileges. An unauthorized hardware peripheral (<code>MTP USB Device</code>) was connected to test system responsiveness and enforcement accuracy.
    </p>

    <div class="screenshot-card">
        {img1_html}
        <div class="caption">Figure 1: Console execution showing real-time hardware detection (VID: 2D95, PID: 6002) and automated disabling via PnP cmdlet.</div>
    </div>

    <div class="screenshot-card">
        {img2_html}
        <div class="caption">Figure 2: Forensic incident table generated by reporter.py showing the UNAUTHORIZED_BLOCKED event record.</div>
    </div>

    <h2>7. Conclusion & Future Roadmap</h2>
    <p>
        The <strong>USB Device Control & Monitoring Framework</strong> successfully accomplishes its core objectives: identifying connected USB peripherals, restricting unauthorized devices in real time, and recording structured audit trails. Future iterations will incorporate Windows Kernel Minifilter Drivers (<code>fltmgr.sys</code>) for pre-mount I/O interception and direct SIEM syslog integration (Splunk/Wazuh).
    </p>

    <hr style="border: 0; border-top: 1px solid #cbd5e1; margin-top: 30px;">
    <div style="font-size: 11.5px; color: #64748b; text-align: center; margin-top: 10px;">
        Internship Project Deliverable | Candidate: Anurag Singh (BTCE24O1013) | Unified Mentor &copy; 2026
    </div>
</div>

</body>
</html>
"""

output_filename = "Anurag_Singh_BTCE24O1013_Project_Report.html"
with open(output_filename, "w", encoding="utf-8") as f:
    f.write(html_content)

print("=" * 60)
print(f"SUCCESS: Report file generated -> {output_filename}")
print("=" * 60)
print("Steps to get your PDF:")
print("1. Double click and open the generated HTML file in Chrome or Edge.")
print("2. Press Ctrl + P (Print).")
print("3. Destination: 'Save as PDF' | Layout: Portrait | Margins: Default")
print("4. Click Save! Your final submission PDF is ready.")