import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"

if not API_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set in environment variables")
