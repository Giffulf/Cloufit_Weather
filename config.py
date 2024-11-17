import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL", "https://weather.cloufit.ru/api/v1/weather")
