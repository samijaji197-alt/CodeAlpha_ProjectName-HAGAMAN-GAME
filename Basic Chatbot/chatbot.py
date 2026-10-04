
import random
from datetime import datetime
 
JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "I would tell you a joke about UDP, but you might not get it.",
]
 
 
def get_response(user_input):
    """Take the user's message and return a matching predefined reply."""
    message = user_input.lower().strip()
 
    # --- Greetings ---
    if message in ("hello", "hi", "hey", "hey there", "hola"):
        return "Hi!"
    elif message in ("good morning",):
        return "Good morning! Hope you have a great day."
    elif message in ("good night",):
        return "Good night! Sleep well."
 
    # --- Small talk ---
    elif message in ("how are you", "how are you?"):
        return "I'm fine, thanks! How about you?"
    elif message in ("i am fine", "i'm fine", "i am good", "i'm good"):
        return "Glad to hear that!"
    elif message in ("what is your name", "what's your name", "who are you"):
        return "I'm a simple rule-based chatbot!"
    elif message in ("how old are you", "what is your age"):
        return "I don't have an age, I'm just a Python script!"
    elif message in ("who made you", "who created you", "who built you"):
        return "I was built as a Python practice project!"
 
    # --- Courtesy ---
    elif message in ("thank you", "thanks", "thank you so much"):
        return "You're welcome!"
    elif message in ("please", "please help"):
        return "Sure, tell me what you need help with."
    elif message in ("sorry", "i am sorry"):
        return "No worries at all!"
 
    # --- Fun ---
    elif message in ("tell me a joke", "joke", "make me laugh"):
        return random.choice(JOKES)
    elif message in ("what is the time", "what time is it", "current time"):
        return "Current time: " + datetime.now().strftime("%H:%M:%S")
    elif message in ("what is the date", "what's the date", "today's date"):
        return "Today's date: " + datetime.now().strftime("%Y-%m-%d")
 
    # --- Chatbot self-help ---
    elif message in ("help", "what can you do", "commands"):
        return ("I can respond to greetings, small talk, jokes, the time/date, "
                "and a few other things. Try saying 'joke', 'what is your name', "
                "or 'bye' to exit.")
 
    # --- Ending the chat ---
    elif message in ("bye", "goodbye", "exit", "quit", "see you"):
        return "Goodbye! Have a nice day."
 
    # --- Fallback ---
    elif message == "":
        return "Please type something."
    else:
        return "Sorry, I don't understand that yet. Type 'help' to see what I can do."
 
 
def chat():
    print("=== Simple Chatbot ===")
    print("Type 'bye' to end the conversation.\n")
 
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Bot:", response)
 
        if user_input.lower().strip() in ("bye", "goodbye", "exit", "quit", "see you"):
            break
 
 
if __name__ == "__main__":
    chat()
 