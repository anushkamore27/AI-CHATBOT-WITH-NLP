import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    # Greetings
    [r"hi|hello|hey", ["Hello! How can I help you today?", "Hey there! What can I do for you?"]],
    [r"how are you", ["I'm just a bot, but I'm doing great! How about you?", "I'm fine, thanks for asking!"]],

    # Personal Info
    [r"what is your name", ["I'm an AI chatbot created to help you!", "You can call me ChatBot!"]],
    [r"who created you", ["I was created using Python and NLP!", "A developer built me with Python and NLTK."]],

    # General Knowledge
    [r"who is the president of usa", ["As of 2024, it's Joe Biden. You can check news for updates."]],
    [r"who discovered gravity", ["Sir Isaac Newton discovered gravity."]],
    [r"what is the capital of france", ["The capital of France is Paris."]],
    [r"what is the largest ocean", ["The Pacific Ocean is the largest ocean on Earth."]],

    # Technology & Programming
    [r"what is python", ["Python is a high-level programming language used for web development, AI, and more."]],
    [r"what is artificial intelligence", ["AI is the simulation of human intelligence in machines."]],
    [r"who is the founder of microsoft", ["Bill Gates and Paul Allen founded Microsoft in 1975."]],
    [r"what is machine learning", ["Machine learning is a subset of AI that enables computers to learn from data."]],

    # Health & Lifestyle
    [r"how to stay healthy", ["Eat a balanced diet, exercise regularly, and get enough sleep!"]],
    [r"what are benefits of meditation", ["Meditation reduces stress, improves focus, and enhances well-being."]],
    [r"how much water should i drink daily", ["Doctors recommend about 8 glasses (2 liters) per day."]],

    # Fun & Entertainment
    [r"who is the richest person in the world", ["It changes often! As of 2024, it's usually Elon Musk or Jeff Bezos."]],
    [r"what is the tallest building", ["The Burj Khalifa in Dubai is the tallest building in the world."]],
    [r"tell me a joke", ["Why don’t programmers like nature? It has too many bugs!"]],
    
    # Exit
    [r"bye|goodbye", ["Goodbye! Have a great day!", "See you next time!"]],

    # Default Response
    [r"(.*)", ["I'm not sure I understand. Can you rephrase that?", "I'm still learning. Ask me another question!"]],
]

def chatbot():
    print("Hello! I am your AI ChatBot. Ask me anything, or type 'bye' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
