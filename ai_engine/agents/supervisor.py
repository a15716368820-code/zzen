class SupervisorAgent:
    name = "supervisor"

    def execute(self, task, context=None):
        return [
            {
                "agent": "writer",
                "task": task
            }
        ]
