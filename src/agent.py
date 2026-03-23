from agent_framework_core import Agent

class MyAgent(Agent):
    def __init__(self):
        super().__init__()
        # Initialize model or tools here

    def run(self, input_text: str) -> str:
        # Minimal logic for demonstration
        if "capital of france" in input_text.lower():
            return "Paris"
        elif "1984" in input_text:
            return "George Orwell"
        else:
            return "I don't know."
