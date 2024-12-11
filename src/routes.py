from fastapi import APIRouter, HTTPException
from src.services import get_weather_and_recommendations
from src.shemas import WeatherResponse

router = APIRouter()

GENDERS = ["женский", "мужской"]
AGE_GROUPS = ["0-5 лет", "6-9 лет", "10-14 лет", "14-18 лет", "18-21 лет", "21-35 лет", "35-50 лет", "51+ лет"]


@router.get("/weather", response_model=WeatherResponse)
async def get_weather():
    example_data = {
        "list": [
            {
                "dt": 1733994000,
                "main": {
                    "temp": 269.31,
                    "feels_like": 263.23,
                    "temp_min": 268.0,
                    "temp_max": 270.0,
                    "pressure": 1008,
                    "sea_level": None,
                    "grnd_level": None,
                    "humidity": 91,
                    "temp_kf": 0.5,
                },
                "weather": [
                    {
                        "id": 803,
                        "main": "Clouds",
                        "description": "облачно с прояснениями",
                        "icon": "04d"
                    }
                ],
                "clouds": {
                    "all": 57
                },
                "wind": {
                    "speed": 5.32,
                    "deg": 294,
                    "gust": None
                },
                "visibility": 5071,
                "pop": 0,
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2024-12-12 09:00:00"
            }
        ],
        "city": {
            "id": 524901,
            "name": "Москва",
            "coord": {
                "lat": 55.7504,
                "lon": 37.6175
            },
            "country": "RU",
            "population": 1000000,
            "timezone": 10800,
            "sunrise": 1733896163,
            "sunset": 1733921797
        },
        "recommendations": "Не выходить на улицу. Опасно для здоровья."
    }

    return WeatherResponse(**example_data)

@router.get("/info")
def get_info():
    return {
        "genders": GENDERS,
        "ages": AGE_GROUPS
    }

@router.post("/recommendations")
def get_recommendations(city: str, gender: str, age_group: str):
    return get_weather_and_recommendations(city, gender, age_group)
