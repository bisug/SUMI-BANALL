import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", 26208465))
API_HASH = os.getenv("API_HASH", "bd4e2fe9c30486282417cdf9a93333b2")
BOT_TOKEN = os.getenv("BOT_TOKEN", None)
BOT_USERNAME = os.getenv("BOT_USERNAME", None)
OWNER_ID = int(os.getenv("OWNER_ID", 7804972365)) 
WEB_APP = os.getenv("WEB_APP", "False").lower() == "true"
