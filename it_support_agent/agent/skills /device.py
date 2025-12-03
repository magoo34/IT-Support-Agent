%%writefile agent/device.py

class DeviceSupport:

    def diagnose(self, issue):
        issue = issue.lower()

        if "slow" in issue:
            return self.performance_issue()
        if "no boot" in issue:
            return self.boot_failure()
        if "storage" in issue:
            return self.disk_issue()

        return "Device issue detected. Run diagnostics and update drivers."

    def performance_issue(self):
        return {
            "fix": ["Close heavy apps", "Upgrade RAM", "Scan malware"]
        }

    def boot_failure(self):
        return {
            "fix": ["Check BIOS", "Reinstall OS"],
            "escalation": "Send to hardware team"
        }

    def disk_issue(self):
        return {
            "fix": ["Clear space", "Replace failing disk"],
            "backup": "Ensure backup before changes"
        }
