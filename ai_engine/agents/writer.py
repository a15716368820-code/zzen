from .base import BaseAgent


class WriterAgent(BaseAgent):
    name = "writer"

    def execute(self, task, context=None):
        return {
            "title": task,
            "content": f"Generated draft for: {task}"
        }
