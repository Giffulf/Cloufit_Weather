import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")
API_KEY_GPT = os.getenv("API_KEY_GPT")
FILE_REC = os.getenv("FILE_REC")