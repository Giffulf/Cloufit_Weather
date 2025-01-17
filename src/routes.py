import os
import uuid

import requests
from fastapi import APIRouter, HTTPException
from starlette.responses import FileResponse

from config import API_URL, FEEDBACK_FILE
from src.services import get_weather_and_recommendations, write_queue
from src.shemas import WeatherResponse, WeatherEntry, WeatherRecResponse, FeedbackRequest, FeedbackEntry

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


@router.post("/report")
async def report_router(feedback: FeedbackRequest):
    try:
        feedback_id = str(uuid.uuid4())

        new_entry = FeedbackEntry(id=feedback_id, email=feedback.email, text=feedback.text)

        await write_queue.put(new_entry.dict())

        return {"message": "Отзыв успешно добавлен в очередь", "id": feedback_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/report-download")
async def download_feedback():
    if not os.path.exists(FEEDBACK_FILE):
        raise HTTPException(status_code=404, detail="Файл с отзывами не найден")
    return FileResponse(FEEDBACK_FILE, filename="feedback_data.json", media_type="application/json")
