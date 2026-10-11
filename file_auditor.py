import os
import hashlib
import json
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def calculate_sha256(filepath: str, max_size_mb: int = 50) -> str:
    if not os.path.exists(filepath) or os.path.isdir(filepath):
        return ""
    try:
        if os.path.getsize(filepath) > (max_size_mb * 1024 * 1024):
            return "SKIPPED_LARGE_FILE"
        hasher = hashlib.sha256()
        with open(filepath, "rb") as f:
            while chunk := f.read(65536):
                hasher.update(chunk)
        return hasher.hexdigest()
    except (PermissionError, FileNotFoundError):
        return "READ_ERROR"

class USBFileAuditHandler(FileSystemEventHandler):
    def __init__(self, log_path: str):
        self.log_path = log_path
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

    def _log_event(self, action: str, src_path: str, dest_path: str = None):
        target = dest_path or src_path
        size = 0
        sha256 = ""
        if os.path.exists(target) and not os.path.isdir(target):
            try:
                size = os.path.getsize(target)
                sha256 = calculate_sha256(target)
            except Exception:
                pass

        record = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "action": action,
            "path": target,
            "source": src_path if dest_path else None,
            "size_bytes": size,
            "sha256": sha256
        }
        with open(self.log_path, "a") as f:
            f.write(json.dumps(record) + "\n")

    def on_created(self, event):
        if not event.is_directory:
            self._log_event("FILE_CREATED", event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            self._log_event("FILE_MODIFIED", event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            self._log_event("FILE_DELETED", event.src_path)

    def on_moved(self, event):
        if not event.is_directory:
            self._log_event("FILE_RENAMED_MOVED", event.src_path, event.dest_path)

class FileAuditor:
    def __init__(self, log_path: str):
        self.log_path = log_path
        self.observers = {}

    def start_monitoring(self, drive_letter: str):
        path = drive_letter if drive_letter.endswith("\\") else f"{drive_letter}\\"
        if not os.path.exists(path) or drive_letter in self.observers:
            return
        event_handler = USBFileAuditHandler(self.log_path)
        observer = Observer()
        observer.schedule(event_handler, path=path, recursive=True)
        observer.start()
        self.observers[drive_letter] = observer

    def stop_monitoring(self, drive_letter: str):
        if drive_letter in self.observers:
            self.observers[drive_letter].stop()
            self.observers[drive_letter].join()
            del self.observers[drive_letter]