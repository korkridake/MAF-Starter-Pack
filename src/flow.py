from src.agent import MyAgent

def main():
    agent = MyAgent()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ("exit", "quit"):
            break
        response = agent.run(user_input)
        print("Agent:", response)

if __name__ == "__main__":
    main()
