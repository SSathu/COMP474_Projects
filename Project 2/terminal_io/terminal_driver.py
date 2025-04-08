# -----IMPORTS----------

from components.TerminalClient import TerminalClient
from components.connector import HTTPConnector
from logs.loggers import logger

# -----INITIALIZATION-------------

hc = HTTPConnector()
tClient = TerminalClient()

# -----MAIN-METHOD----------------

if __name__=="__main__":
    
    logger.info("Starting Terminal Chatbot....")
    
    print("hello this is from the terminal! Please provide your name: ", end='')
    
    while True:
        
        answer = input()
        
        print(f"this was your answer: {answer}")
        
        
        pass