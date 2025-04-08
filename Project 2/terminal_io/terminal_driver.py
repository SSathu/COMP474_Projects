# -----IMPORTS----------
from components.connector import HTTPConnector
from logs.loggers import logger
import time
import asyncio

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
    f"{empty_indentation} Can we start with your name please?"
]


# -----MAIN-ASYNC-LOOP---------

async def main_loop():
    
    logger.debug("Starting Terminal Chatbot....")
    
    for w in welcome_message:
        print(w)
    
    print()
    
    answer = input(f"{get_username_indentation()} ")
    
    response = await hc.send_message(path="/testing", data={"message":answer})
    
    # expects a response of format {"response":"......."}
    
    print(response["response"])
    
    # need to do a processing for the output so that its printed clean
    
# -----MAIN-METHOD----------------

if __name__=="__main__":
    
    time.sleep(2)
    # giving docker enough time to attach the container to the terminal, so we dont miss any outputs
    
    asyncio.run(main_loop())