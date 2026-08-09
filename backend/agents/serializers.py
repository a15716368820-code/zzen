from dataclasses import dataclass


@dataclass
class AgentTaskSerializer:
    """Basic serializer foundation for Agent tasks."""

    agent_name: str
    input_text: str
    output_text: str = ""
    status: str = "pending"
