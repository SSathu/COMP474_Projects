import logging
import os
from datetime import datetime, timezone, timedelta

LOG_DIRECTORY = os.path.dirname(__file__)
os.makedirs(LOG_DIRECTORY, exist_ok=True)

log_level = 10

class EasternTimeFormatter(logging.Formatter):
    # this class is used to change the timezone in the logger for eastern standard time (EST)
    
    def formatTime(self, record, datefmt=None):
        # only method in the class, this is the logic to set the time to EST
        
        eastern_offset = timedelta(hours=-4)
        dt = datetime.fromtimestamp(record.created, timezone.utc) + eastern_offset
        return dt.strftime(datefmt) if datefmt else dt.isoformat()

formatter = EasternTimeFormatter("%(asctime)s [%(name)s] %(levelname)s @ %(filename)s:%(lineno)d - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
# uses the class EasternTimeFormatter that we defined to set the formatter

TerminalClient_file_handler = logging.FileHandler(os.path.join(LOG_DIRECTORY, "TerminalClient.log"))
TerminalClient_file_handler.setLevel(logging.DEBUG)
TerminalClient_file_handler.setFormatter(formatter)
# defines the general loggger for everything

logger = logging.getLogger("terminal")
logger.setLevel(log_level)
logger.addHandler(TerminalClient_file_handler)
# creates the default/general logger.



