#Team Members:
#1. Sathurthikan Saththyvel 40213455
#2. Alex Lee Tong Fong 40220887

import spacy
import responses
import re
#Tokenize/lemmatize input text
nlp = spacy.load("en_core_web_sm");

# Remove punctuation/stop words (the, is, etc)
def preprocess_text(text):
    # Pass user input into nlp
    doc = nlp(text)

    #Also removing punctuation and articles with "if not token.is_stop/if not token.is_punct"
    # Keep important words in a question 
    question_words = {"what", "how", "why", "who", "when", "where"}
    programming_keywords = {"if", "else", "elseif", "while", "for", "switch", "case", "try", "except", "finally", "overloading"}  

    #Using token.lemma to convert words into base form
    processed_text = " ".join([
        token.lemma_ 
        for token in doc 
        if not token.is_punct and (token.text.lower() in question_words or token.text.lower() in programming_keywords or not token.is_stop)
    ])
    #Convert to lower case and return
    return processed_text.lower()

# Match the processed user input against pattern and retrieve response accordingly
def get_response(user_input):

    # Clean whitespace
    user_input = re.sub(r'\s+', ' ', user_input.strip())  
    # Call preprocess_text()
    text = preprocess_text(user_input)

    # Iterate over predefined response and return it
    for intent, pattern in responses.patterns.items():
        if re.search(pattern, text):
            return responses.responses[intent]

    return responses.responses["default"]  

# Run chatbot session in terminal
def chat():
    while True:
        user_input = input("You: ").strip().lower()

        # Stop convo if user inputs 'bye'
        if user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        # Showcase for demo when input is "start"    
        if user_input == "start":
            showcase_responses()  
            continue  
        
        response = get_response(user_input)
        print("Chatbot:", response)


# Showcase function for demo purposes "start"
def showcase_responses():
    print("=== Chatbot Showcase demo===\n")

    if not responses.patterns:
        print("No predefined patterns found.")
        return

    # Iterate over predefined responses
    for intent, pattern in responses.patterns.items():
        # Extract the first example input from the regex pattern
        example_input = re.sub(r"\\b|\(|\)", "", pattern.split("|")[0])
        example_input = re.sub(r"\s+", " ", example_input).strip()

        response = get_response(example_input)

        print(f"User: {example_input}")
        print(f"Chatbot: {response}\n")


if __name__ == "__main__":
    chat()

