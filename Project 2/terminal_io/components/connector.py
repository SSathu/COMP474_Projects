from logs.loggers import logger
import aiohttp
import os

class HTTPConnector:
    # class based because we want to have one instance of an HTTP client session to avoid memory leaks
    
    def __init__(self):
        # constructor
        
        self.httpClient_session = None
        # we need a single http_client_session to handle the fetch events and proper cleanup
        
        self.base_url = os.getenv("FASTAPI_URL", None)
        # get the default path frmo the env variables
        
        logger.debug("class HTTPConnector initialised correctly")
        
    async def start_http_session(self):
        # creates a session and adds it to self.httpClient_session
        # we cant do this in the constructor because the constructor shouldnt run async methods
        # dont forget to use await when using this
        
        try:
            
            logger.debug("Starting new session creation....")
            
            if self.httpClient_session is None:
                # for the first time we start it, the object was initialised as None
                
                self.httpClient_session = aiohttp.ClientSession()
                
                logger.debug(f"Passed start_http_session with session is None or session == None")

            else:
                
                logger.debug("Session already initialized, passed without errors.")
            
        except Exception as e: 
            # if the self.httpClient_Session cant be initialised properly
            
            logger.error(f"Failed to start_session() because : {e}")
            
            return None
    
    async def close_http_session(self):
        # closing the http session
        # dont forget to use await when using this
        
        if self.httpClient_session:
            await self.httpClient_session.close()
        # close the http session 
        
    async def send_message(self, path="/chat", data={"message":"default"}):
        # API call to fastAPI
        
        try:
            
            logger.debug("Starting send_message()...")
            
            await self.start_http_session()
            # makes sure that a session has started
            
            full_path = self.base_url + path
            # constructing the path from the the env vars and the input parameter
            
            logger.debug(f"full_path: {full_path}")
            
            logger.debug(f"data to be sent: {data}")
            
            async with self.httpClient_session.post(full_path, json=data) as response:
                # sends a request to the specified path with aiohttp session post
                
                logger.debug("now inside the httpClient_session.post()")
                
                return await response.json()
                # returns the json of the response object, but not sure if we should deconstruct it here and pass the data without the message from the server
                
        except Exception as e: 
            
            logger.error(f"Error send_message : {e}")
            
            await self.close_http_session()
            
            return None
            # fallback -> returns None if anything crashes