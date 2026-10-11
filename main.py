import os
import re
import json
import time
import logging
from datetime import datetime, timezone
import pythoncom
import win32com.client
import win32file

from policy_engine import PolicyEngine
from file_auditor import FileAuditor

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("USBSentry")

def extract_identifiers(device_id: str):
    vid_match = re.search(r"VID_([0-9A-Fa-f]{4})", device_id)
    pid_match = re.search(r"PID_([0-9A-Fa-f]{4})", device_id)
    serial = device_id.split("\\")[-1] if "\\" in device_id else "UNKNOWN"
    vid = vid_match.group(1) if vid_match else "UNKNOWN"
    pid = pid_match.group(1) if pid_match else "UNKNOWN"
    return vid, pid, serial

def get_removable_drive_letters():
    drives = []
    bitmask = win32file.GetLogicalDrives()
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if bitmask & 1:
            drive_root = f"{letter}:\\"
            if win32file.GetDriveType(drive_root) == win32file.DRIVE_REMOVABLE:
                drives.append(drive_root)
        bitmask >>= 1
    return drives

def main():
    # Logs directory ko ensure karein ki wo exist kare
    os.makedirs("logs", exist_ok=True)

    logger.info("Initializing USB Device Control & Monitoring Framework...")
    policy = PolicyEngine("config.json")
    auditor = FileAuditor("logs/file_audit.jsonl")

    pythoncom.CoInitialize()
    wmi = win32com.client.Dispatch("WbemScripting.SWbemLocator")
    service = wmi.ConnectServer(".", "root\\cimv2")

    watcher = service.ExecNotificationQuery(
        "SELECT * FROM __InstanceCreationEvent WITHIN 1 WHERE TargetInstance ISA 'Win32_PnPEntity'"
    )

    seen_devices = set()

    logger.info("Service active. Awaiting USB hardware events (Ctrl+C to stop)...")

    try:
        while True:
            event = watcher.NextEvent()
            target = event.TargetInstance
            device_id = str(target.DeviceID or "")
            service_name = str(target.Service or "")

            if device_id.upper().startswith("USBSTOR\\") or service_name.upper() == "USBSTOR":
                if "HID" in device_id and "USBSTOR" not in device_id:
                    continue  # Keyboards aur mice ko protect karne ke liye

                if device_id.upper() in seen_devices:
                    continue
                seen_devices.add(device_id.upper())

                vid, pid, serial = extract_identifiers(device_id)
                name = target.Name or "Unknown USB Entity"

                logger.info(f"[DETECTED] Hardware: '{name}' | VID: {vid} | PID: {pid} | ID: {device_id}")

                authorized = policy.is_authorized(vid, pid, serial)

                log_entry = {
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "device_name": name,
                    "device_id": device_id,
                    "vid": vid,
                    "pid": pid,
                    "serial": serial,
                    "status": "AUTHORIZED" if authorized else "UNAUTHORIZED_DETECTED"
                }
                with open("logs/usb_events.jsonl", "a") as f:
                    f.write(json.dumps(log_entry) + "\n")

                if not authorized:
                    logger.warning(f"[ALERT] Unauthorized storage device detected: VID={vid} PID={pid}")
                    if policy.config.get("auto_block_unauthorized", True):
                        policy.block_device(device_id)
                else:
                    logger.info(f"[APPROVED] Device allowed: {name}")
                    time.sleep(3)
                    for drive in get_removable_drive_letters():
                        logger.info(f"[AUDIT] Attaching file auditing hook to {drive}")
                        auditor.start_monitoring(drive)

    except KeyboardInterrupt:
        logger.info("Stopping monitoring service...")
    finally:
        pythoncom.CoUninitialize()

if __name__ == "__main__":
    main()