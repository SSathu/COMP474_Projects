# -----IMPORTS----------
from components.connector import HTTPConnector
from logs.loggers import logger
import time
import asyncio
import requests

from models import Query

# -----INITIALIZATION-------------

hc = HTTPConnector()

desired_length = 12

chatbot_signature = "CHATBOT"
user_name = "YOU"
hanging_space = " "

chatbot_indentation = chatbot_signature.ljust(desired_length) + "=>"

def get_username_indentation():
    
    username_indentation = user_name.ljust(desired_length) + "=>"
    
    return username_indentation

empty_indentation = hanging_space.ljust(desired_length) + "=>"


welcome_message = [
    f"{chatbot_indentation} Hi! Welcome to our Chatbot!",
    f"{empty_indentation} What do you want to talk about today?"
]

# -----MAIN-ASYNC-LOOP---------

async def main_loop():
    logger.debug("Starting Terminal Chatbot....")

    for w in welcome_message:
            print(w)

    while(True):

        print()

        user_input = input(f"{get_username_indentation()} ")

        print()

        if "exit chatbot" in user_input:
            print(f"{chatbot_indentation} You wrote 'exit chatbot'! Now quitting the program. See you next time!", end=' ')
            break

        query = Query(text=user_input)
        
        response_data = await terminal_analyze_via_api(query)
        if response_data:
            print(f"{chatbot_indentation} {response_data}")
    
async def terminal_analyze_via_api(query: Query):
    try: 
        payload = {"text": query.text}
        response = requests.post(
            "http://fastapi:80/api/v1/chat",
            json=payload,
            timeout=2.0
            )
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")
        return None
    except ValueError as e:
        print(f"JSON decoding error: {e}")
        return None

    """
    # expects a response of format {"response":"......."}
    
    raw_response_first = response["response"]
    
    response_list_1 = raw_response_first.split()
    
    for i in range(len(response_list_1)):
        
        if i == 0:
            print(f"{chatbot_indentation} {response_list_1[i]}", end=' ')
            continue
        
        if i == len(response_list_1) - 1:
            print(f"{response_list_1[i]}")
            break
        
        if not (i % 15 == 0): 
            print(f"{response_list_1[i]} ", end=' ')
            continue
        
        if (i % 15 == 0):
            print(f"\n{empty_indentation} {response_list_1[i]}", end=' ')
    
    print()
    
    # now for the convo loop
    
    while True:
        
        user_input = input(f"{get_username_indentation()} ")
        
        print()
        
        if "exit chatbot" in user_input:
            print(f"{chatbot_indentation} You wrote 'exit chatbot'! Now quitting the program. See you next time!", end=' ')
            await hc.close_http_session()
            break
        
        response_2 = await hc.send_message(path="/testing", data={"text":user_input})
        
        raw_response_first_2 = response_2["response"]
    
        response_list_2 = raw_response_first_2.split()
        
        for i in range(len(response_list_2)):
            
            if i == 0:
                print(f"{chatbot_indentation} {response_list_2[i]}", end=' ')
                continue
            
            if i == len(response_list_2) - 1:
                print(f"{response_list_2[i]}")
                break
            
            if not (i % 15 == 0): 
                print(f"{response_list_2[i]} ", end=' ')
                continue
            
            if (i % 15 == 0):
                print(f"\n{empty_indentation} {response_list_2[i]}", end=' ')
        
        print()
"""
    
    
# -----MAIN-METHOD----------------

if __name__=="__main__":
    
    time.sleep(2)
    # giving docker enough time to attach the container to the terminal, so we dont miss any outputs
    
    asyncio.run(main_loop())

