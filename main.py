from fastapi import FastAPI
from src.routes import router

app = FastAPI()

app.include_router(router)

# from fastapi import FastAPI, HTTPException
# import requests
# from config import API_URL
#
# app = FastAPI()
#
# @app.get("/weather/{city}")
# def get_weather(city: str):
#     try:
#         response = requests.get(f"{API_URL}/{city}")
#         response.raise_for_status()  # Проверка на ошибки HTTP
#
#         result = response.json()
#         return result
#
#     except requests.exceptions.HTTPError as http_err:
#         raise HTTPException(status_code=response.status_code, detail=str(http_err))
#     except Exception as err:
#         raise HTTPException(status_code=500, detail=str(err))

