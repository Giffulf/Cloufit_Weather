import requests
from fastapi import APIRouter, HTTPException

from config import API_URL
from src.services import get_weather_and_recommendations
from src.shemas import WeatherResponse, WeatherEntry, WeatherRecResponse

router = APIRouter()

GENDERS = ["женский", "мужской"]
AGE_GROUPS = ["0-5 лет", "6-9 лет", "10-14 лет", "14-18 лет", "18-21 лет", "21-35 лет", "35-50 лет", "51+ лет"]


@router.get("/weather/{city}", response_model=WeatherResponse)
async def get_weather(city: str):
    response = requests.get(f"{API_URL}/{city}")

    if response.status_code == 200:
        return WeatherResponse(**response.json())

    return HTTPException(
        status_code=response.status_code,
        detail=response.text
    )


@router.get("/info")
def get_info():
    return {
        "genders": GENDERS,
        "ages": AGE_GROUPS
    }


@router.post("/recommendations", response_model=WeatherRecResponse)
def get_recommendations(city: str, gender: str, age_group: str):
    return get_weather_and_recommendations(city, gender, age_group)
