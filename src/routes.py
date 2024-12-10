from fastapi import APIRouter, HTTPException
from src.services import get_weather_and_recommendations

router = APIRouter()

GENDERS = ["женский", "мужской"]
AGE_GROUPS = ["0-5 лет", "6-9 лет", "10-14 лет", "14-18 лет", "18-21 лет", "21-35 лет", "35-50 лет", "51+ лет"]

@router.get("/info")
def get_info():
    return {
        "genders": GENDERS,
        "ages": AGE_GROUPS
    }

@router.post("/recommendations")
def get_recommendations(city: str, gender: str, age_group: str):
    return get_weather_and_recommendations(city, gender, age_group)
