print("🤖 ChatBot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("🤖 ChatBot: Hi there!")

    elif user == "how are you":
        print("🤖 ChatBot: I am doing great!")

    elif user == "what is your name":
        print("🤖 ChatBot: My name is RuleBot.")

    elif user == "bye":
        print("🤖 ChatBot: Goodbye!")
        break

    else:
        print("🤖 ChatBot: Sorry, I don't understand.")