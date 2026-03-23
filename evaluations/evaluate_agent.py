import json
from src.agent import MyAgent

def load_data(path):
    with open(path, "r") as f:
        return json.load(f)

def evaluate(agent, data):
    correct = 0
    for item in data:
        response = agent.run(item["input"])
        if response.strip().lower() == item["expected_output"].strip().lower():
            correct += 1
    accuracy = correct / len(data)
    print(f"Accuracy: {accuracy:.2%}")

if __name__ == "__main__":
    agent = MyAgent()
    data = load_data("../data/example_data.json")
    evaluate(agent, data)
