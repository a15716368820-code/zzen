class ModelRouter:
    """Unified model access layer."""

    def chat(self, prompt, model="auto"):
        return {
            "model": model,
            "response": prompt
        }
