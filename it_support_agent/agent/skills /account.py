# account.py

class AccountManager:

    def handle(self, issue: str):
        issue = issue.lower()

        if "password" in issue:
            return self.reset_password()
        elif "locked" in issue:
            return self.unlock_account()
        elif "permission" in issue:
            return self.fix_permissions()
        else:
            return "Account issue logged for IT review."

    def reset_password(self):
        return {
            "action": "Password Reset",
            "steps": [
                "Verify user identity",
                "Generate reset token",
                "Force password change on login"
            ]
        }

    def unlock_account(self):
        return {
            "action": "Unlock Account",
            "steps": [
                "Confirm identity",
                "Reset failed login counter",
                "Notify user"
            ]
        }

    def fix_permissions(self):
        return {
            "action": "Access Control",
            "steps": [
                "Review group membership",
                "Assign least-privilege roles",
                "Audit access logs"
            ]
        }
