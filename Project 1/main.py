import spacy
import responses
import re
#python -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm");

def preprocess_text(text):
    # Pass user input into nlp
    doc = nlp(text)

    #Using token.lemma to convert words into base form
    #Also removing punctuation and articles with "if not token.is_stop/if not token.is_punct"
    question_words = {"what", "how", "why", "who", "when", "where"}
    programming_keywords = {"if", "else", "elseif", "while", "for", "switch", "case", "try", "except", "finally"}  

    processed_text = " ".join([
        token.lemma_ 
        for token in doc 
        if not token.is_punct and (token.text.lower() in question_words or token.text.lower() in programming_keywords or not token.is_stop)
    ])
    #Convert to lower case and return
    return processed_text.lower()

def get_response(user_input):
    text = preprocess_text(user_input)

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