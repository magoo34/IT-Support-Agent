%%writefile agent/ticket.py
import json, uuid, os

class TicketSystem:
    FILE = "tickets.json"

    def __init__(self):
        if not os.path.exists(self.FILE):
            with open(self.FILE, "w") as f:
                json.dump([], f)

    def create_ticket(self, user, issue, severity="Medium"):
        ticket = {
            "id": str(uuid.uuid4()),
            "user": user,
            "issue": issue,
            "severity": severity,
            "status": "Open"
        }

        with open(self.FILE, "r+") as f:
            data = json.load(f)
            data.append(ticket)
            f.seek(0)
            json.dump(data, f, indent=2)

        return ticket

    def list_tickets(self):
        with open(self.FILE) as f:
            return json.load(f)
