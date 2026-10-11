import json
import subprocess
import logging

logger = logging.getLogger("PolicyEngine")

class PolicyEngine:
    def __init__(self, config_path="config.json"):
        with open(config_path, "r") as f:
            self.config = json.load(f)

    def is_authorized(self, vid: str, pid: str, serial: str) -> bool:
        for blocked in self.config.get("blocked_devices", []):
            if blocked.get("vendor_id", "").lower() == vid.lower() and blocked.get("product_id", "").lower() == pid.lower():
                return False

        if self.config.get("mode") == "ALLOWLIST_ONLY":
            for allowed in self.config.get("allowed_devices", []):
                vid_match = allowed.get("vendor_id", "").lower() == vid.lower()
                pid_match = allowed.get("product_id", "").lower() == pid.lower()
                serial_rule = allowed.get("serial_number")
                serial_match = (serial_rule is None) or (serial_rule.lower() in serial.lower())
                
                if vid_match and pid_match and serial_match:
                    return True
            return False

        return True

    def block_device(self, device_instance_id: str) -> bool:
        try:
            cmd = [
                "powershell",
                "-ExecutionPolicy", "Bypass",
                "-Command",
                f'Disable-PnpDevice -InstanceId "{device_instance_id}" -Confirm:$false'
            ]
            subprocess.run(cmd, capture_output=True, text=True, check=True)
            logger.warning(f"[BLOCKED] Device {device_instance_id} disabled successfully.")
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to disable device: {e.stderr.strip()}")
            return False