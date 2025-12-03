from agent.llm import LLMClient
from agent.workflows import WorkflowEngine
from agent.kb import KnowledgeBase

class SupportAgentEngine:
    def __init__(self):
        self.llm = LLMClient()
        self.kb = KnowledgeBase()
        self.workflow_engine = WorkflowEngine()

    def run(self, user, message, hostname="Unknown"):
        # 1. Check workflow triggers
        workflow = self.workflow_engine.match_workflow(message)
        if workflow:
            return self.workflow_engine.run_workflow(workflow, message, hostname)

        # 2. Check knowledge base
        kb_answer = self.kb.search(message)
        if kb_answer:
            return {"source": "kb", "answer": kb_answer}

        # 3. Use LLM
        llm_response = self.llm.generate(message)
        return {"source": "llm", "answer": llm_response}
