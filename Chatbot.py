print("Welcome to ChatBot! Type 'bye' to exit.")
print("ChatBot: Hello! How can I assist you today?")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello", "hey"]:
        print("ChatBot: Hello! How can I help you?")
    
    elif "your name" in user_input:
        print("ChatBot: I am a simple chatbot created using Python.")

    elif "how are you" in user_input:
        print("ChatBot: I'm just a bunch of code, but I'm functioning as expected!")

    elif "help" in user_input:
        print("ChatBot: Sure! I can answer basic questions. Try asking about weather, time, or greetings.")
    
    elif "weather" in user_input:
        print("ChatBot: Sorry, I can't fetch live weather data. I recommend checking a weather website.")
    
    elif "time" in user_input:
        from datetime import datetime
        print(f"ChatBot: The current time is {datetime.now().strftime('%H:%M:%S')}.")

    elif user_input in ["bye", "exit", "quit"]:
        print("ChatBot: Goodbye! Have a great day!")
        break

    else:
        print("ChatBot: I'm sorry, I don't understand that. Can you try something else?")
