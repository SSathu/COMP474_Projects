# -----IMPORTS----------

from components.TerminalClient import TerminalClient
from components.connector import HTTPConnector
from logs.loggers import logger
import time

# -----INITIALIZATION-------------

hc = HTTPConnector()
tClient = TerminalClient()

# -----MAIN-METHOD----------------

if __name__=="__main__":
    
    time.sleep(5)
    # giving docker enough time to attach the container to the terminal, so we dont miss any outputs
    
    logger.debug("Starting Terminal Chatbot....")