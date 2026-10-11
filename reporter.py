import json
import os

def generate_report(event_log="logs/usb_events.jsonl", file_log="logs/file_audit.jsonl"):
    print("=" * 70)
    print("           ENDPOINT USB MONITORING & AUDIT REPORT")
    print("=" * 70)

    if os.path.exists(event_log):
        print("\n--- [1] HARDWARE CONNECTION EVENTS ---")
        with open(event_log, "r") as f:
            for line in f:
                if not line.strip(): continue
                ev = json.loads(line)
                status = ev.get('status', 'UNKNOWN')
                flag = "[!]" if "BLOCKED" in status else "[+]"
                print(f"{flag} {ev.get('timestamp')} | {status:22} | {ev.get('device_name')} (VID:{ev.get('vid')} PID:{ev.get('pid')})")

    if os.path.exists(file_log):
        print("\n--- [2] FILE TRANSFERS & MODIFICATIONS DETECTED ---")
        with open(file_log, "r") as f:
            for line in f:
                if not line.strip(): continue
                fl = json.loads(line)
                print(f"[*] {fl.get('timestamp')} | {fl.get('action'):18} | {fl.get('path')} ({fl.get('size_bytes')} bytes)")
                if fl.get('sha256') and fl['sha256'] not in ("SKIPPED_LARGE_FILE", "READ_ERROR"):
                    print(f"    SHA-256: {fl['sha256']}")
    print("=" * 70)

if __name__ == "__main__":
    generate_report()