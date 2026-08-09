"""Base interface for ZZEN agents."""


class BaseAgent:
    name = "base"

    def execute(self, task, context=None):
        raise NotImplementedError
