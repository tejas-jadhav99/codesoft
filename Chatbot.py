# TASK 1 - CHATBOT WITH RULE-BASED RESPONSES

# Build a simple chatbot that responds to user inputs based on
# predefined rules. Use if-else statements or pattern matching
# techniques to identify user queries and provide appropriate
# responses. This will give you a basic understanding of natural
# language processing and conversation flow.


import re

def chbt(user_input):
    # We have added some Predefined rules and responses
    rules = [
        (r'hello|hi|hey', 'Hello! How can I help you?'),
        (r'how are you', 'I am a computer program, but thanks for asking!'),
        (r'what is your name', 'I am a chatbot. You can call me bugsboby.'),
        (r'bye|goodbye', 'Goodbye! Have a great day!'),
        (r'\b(?:thank you|thanks)\b', 'You\'re welcome!'),
        (r'\b(?:help|support)\b', 'Sure, I can help you. What do you need assistance with?'),
    
    ]

    # To provide a response, Check user input against rules
    for pattern, response in rules:
        if re.search(pattern, user_input, re.IGNORECASE):
            return response

    # Return Default response if no matching rule is found
    return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Main loop for the chatbot
def main():
    print("Welcome to the bugsboby - An chatbot!")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye! Have a great day!")
            break

        response = chbt(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    main()
