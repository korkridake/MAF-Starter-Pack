# Placeholder for model definition
class SimpleModel:
    def predict(self, input_text: str) -> str:
        # Dummy logic
        if "capital of france" in input_text.lower():
            return "Paris"
        elif "1984" in input_text:
            return "George Orwell"
        else:
            return "I don't know."
