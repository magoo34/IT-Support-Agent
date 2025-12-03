class LLMClient:
    def __init__(self, model_name="gemini-1.5-pro"):
        self.model_name = model_name

    def generate(self, text):
        # Placeholder LLM response. Replace this with real Gemini client calls.
        return f"[LLM Generated Response] (model={self.model_name}) Based on: {text}"
