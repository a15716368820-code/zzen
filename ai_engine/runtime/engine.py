"""ZZEN AI OS Runtime foundation."""


class AgentRuntime:
    def __init__(self):
        self.agents = {}

    def register(self, agent):
        self.agents[agent.name] = agent

    def run(self, agent_name, task, context=None):
        agent = self.agents.get(agent_name)
        if not agent:
            raise ValueError(f"Agent not found: {agent_name}")
        return agent.execute(task, context)
