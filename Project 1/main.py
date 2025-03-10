#Team Members:
#1. Sathurthikan Saththyvel 40213455
#2. Alex Lee Tong Fong 40220887
#3. Victor Zhou (Unknown)

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
    programming_keywords = {"if", "else", "elseif", "while", "for", "switch", "case", "try", "except", "finally", "overloading"}  

    processed_text = " ".join([
        token.lemma_ 
        for token in doc 
        if not token.is_punct and (token.text.lower() in question_words or token.text.lower() in programming_keywords or not token.is_stop)
    ])
    #Convert to lower case and return
    return processed_text.lower()


def get_response(user_input):
    user_input = re.sub(r'\s+', ' ', user_input.strip())  
    text = preprocess_text(user_input)

    for intent, pattern in responses.patterns.items():
        if re.search(pattern, text):
            return responses.responses[intent]

    return responses.responses["default"]  



def chat():
    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "bye":
            print("Chatbot: Goodbye!")
            break

        if user_input == "start":
            showcase_responses()  
            continue  
        
        response = get_response(user_input)
        print("Chatbot:", response)


# Showcase function for demo purposes
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

