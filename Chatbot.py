import datetime

def chatbot():
    name = input("🤖 Chatbot: Hi! What's your name? ").strip().title()
    print(f"🤖 Chatbot: Nice to meet you, {name}! Type 'bye' to exit.\n")

    while True:
        user_input = input(f"{name}: ").lower().strip()

        # Greetings
        if user_input in ["hi", "hello", "hey"]:
            print(f"🤖 Chatbot: Hello {name}! 😊")

        # How are you
        elif "how are you" in user_input:
            print(f"🤖 Chatbot: I'm doing great, {name}! 😄")

        # User asks their name
        elif "my name" in user_input:
            print(f"🤖 Chatbot: Of course! Your name is {name} 😊")

        # Chatbot name
        elif "your name" in user_input:
            print("🤖 Chatbot: I'm your Python Chatbot 🤖")

        # Time
        elif "time" in user_input:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"🤖 Chatbot: {name}, current time is {current_time}")

        # Date
        elif "date" in user_input:
            today = datetime.date.today()
            print(f"🤖 Chatbot: {name}, today's date is {today}")

        # Help
        elif "help" in user_input:
            print(f"🤖 Chatbot: {name}, you can ask me about time, date, or just chat!")

        # Exit
        elif user_input == "bye":
            print(f"🤖 Chatbot: Goodbye {name}! Have a great day! 👋")
            break

        # Empty input
        elif user_input == "":
            print("🤖 Chatbot: Please say something 😅")

        # Default response
        else:
            print(f"🤖 Chatbot: Hmm {name}, I don't understand that yet 🤔")

# Run chatbot
chatbot()