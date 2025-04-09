import requests
from logs.loggers import logger

url = "https://api.dbpedia-spotlight.org/en/annotate"

headers = {
    'Accept': 'application/json',  
}

def get_from_dbpedia_spotlight(text):
    
    try:
        
        params = {'text':text, 'confidence':0.5}
        
        response = requests.get(url, params=params, headers=headers, verify=False)
        
        logger.debug(f"DBpedia for text : {text}")
        
        if response.status_code == 200:
            
            data = response.json()
            
            # logger.debug(data)
            
            # for entity in data['Resources']:
            #     logger.debug(f"Entity: {entity['@surfaceForm']}")
            #     logger.debug(f"URI: {entity['@URI']}")
            
            return data['Resources']
        
    except Exception as e:
        
        logger.error(f"failed. e => {e}")
        
        return None
    
    