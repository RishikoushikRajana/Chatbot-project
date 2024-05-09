"""
Created on Thu may 09 00:12:31 2024

@author:  © Rishi
"""
def Rishi_chatbot(user_input):
    user_input = user_input.lower()  # Convert user input to lowercase for case-insensitivity

    if user_input in ['hello', 'hi']:
        return "Hello there! I am Rishi"
    elif user_input == "who are you?":
        return "I'm a rule-based, chatbot developed by Rishi."
    elif user_input == "how are you?":
        return "I'm Fine. What about you ? I'm here to assist you!"
    elif user_input == "what is artificial intelligence?":
        return "Artificial intelligence (AI) refers to the simulation of human intelligence processes by machines."
    elif user_input == "name some fruits":
        return "Yeah sure! Mango, Apple, Guava, Graphes are some fruits which I can suggest"
    elif user_input == "name some vegetables":
        return "Yeah sure! Potato, Tomato, Carrot, Cabbage are some vegetables which I can suggest"
    elif user_input in ['bye', 'goodbye']:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't quite get that. I am a pre-defined chatbot of Rishi. Please ask me pre-defined Questions"

# Test the chatbot
while True:
    user_query = input("You: ")
    if user_query.lower() == 'exit':
        break
    response = Rishi_chatbot(user_query)
    print("Rishi_AI:", response)