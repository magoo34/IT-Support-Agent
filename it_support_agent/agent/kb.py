import json, os

class KnowledgeBase:
    def __init__(self):
        path = os.path.join(os.path.dirname(__file__), '..', 'data', 'kb_faq.json')
        path = os.path.normpath(path)
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                self.kb = json.load(f)
        else:
            self.kb = []

    def search(self, query):
        ql = query.lower()
        for item in self.kb:
            if item.get('q', '').lower() in ql:
                return item.get('a')
        return None
