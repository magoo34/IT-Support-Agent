import json, os

class WorkflowEngine:
    def __init__(self):
        path = os.path.join(os.path.dirname(__file__), '..', 'data', 'workflows.json')
        path = os.path.normpath(path)
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                self.workflows = json.load(f)
        else:
            self.workflows = []

    def match_workflow(self, message):
        for wf in self.workflows:
            if wf.get('pattern', '').lower() in message.lower():
                return wf
        return None

    def run_workflow(self, workflow, message, hostname="Unknown"):
        # Simple, deterministic workflow runner for demo
        return {
            "workflow": workflow.get('workflow'),
            "message": message,
            "hostname": hostname,
            "steps": workflow.get('steps', ['Inspect device', 'Collect logs', 'Escalate if unresolved'])
        }
