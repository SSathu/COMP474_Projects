import spacy
import responses
import re

nlp = spacy.load("en_core_web_sm");


def get_response(user_input):
    text = user_input.lower()

    # Basic Resp
    for intent in ["greet", "bye", "help"]:
        if re.search(responses.patterns[intent], text):
            return responses.responses[intent]

    # Java terms
    for intent, pattern in responses.patterns.items():
        if re.search(pattern, text):
            return responses.responses[intent]

    return responses.responses["default"]  # Default



def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)


if __name__ == "__main__":
    chat()