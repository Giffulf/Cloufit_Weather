import requests
import json
from fastapi import HTTPException

API_URL = "https://weather.cloufit.ru/api/v1/weather"

def load_recommendations():
    with open(r"C:UsersulianCloufitCloufitsrcweather-recs-result.json", 'r', encoding='utf-8') as f:
        return json.load(f)

def get_weather_and_recommendations(city: str, gender: str, age_group: str):

    if gender == "женский":
        gender = "female"
    elif gender == "мужской":
        gender = "male"
    else:
        raise HTTPException(status_code=400, detail="Некорректный пол.")

    age_group_mapping = {
        "0-5 лет": "0-5",
        "6-9 лет": "6-9",
        "10-14 лет": "10-14",
        "14-18 лет": "14-18",
        "18-21 лет": "18-21",
        "21-35 лет": "21-35",
        "35-50 лет": "35-50",
        "51+ лет": "51+"
    }

    if age_group in age_group_mapping:
        age_group = age_group_mapping[age_group]
    else:
        raise HTTPException(status_code=400, detail="Некорректная возрастная группа.")

    try:
        response = requests.get(f"{API_URL}/{city}")
        response.raise_for_status()
        weather_data = response.json()
    except requests.exceptions.HTTPError as http_err:
        raise HTTPException(status_code=response.status_code, detail=str(http_err))
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))

    temperature = weather_data['list'][0]['main']['temp'] - 273.15  # Преобразование из Кельвинов в Цельсий

    # Извлечение типа погоды
    weather_conditions = weather_data['list'][0]['weather']
    precipitation = weather_conditions[0]['main'] if weather_conditions else "неизвестно"

    recommendations = find_recommendations(gender, age_group, temperature, precipitation)

    return {
        "weather": weather_data,
        "recommendations": recommendations
    }

def find_recommendations(gender: str, age_group: str, temperature: float, precipitation: str):
    recommendations_data = load_recommendations()

    if precipitation in ["Thunderstorm", "Drizzle", "Rain"]:
        precipitation_category = "rain"
    elif precipitation == "Snow":
        precipitation_category = "snow"
    else:
        precipitation_category = "any"

    for rec in recommendations_data['recommendations']:
        if rec['gender'] == gender and rec['age_group'] == age_group:
            for weather_condition in rec['weather_precipitation']:
                if weather_condition['temperature_range'][0] <= temperature <= weather_condition['temperature_range'][1]:
                    if weather_condition['precipitation'] == precipitation_category or weather_condition['precipitation'] == "any":
                        return weather_condition['recommendation']

    return "Нет рекомендаций для данных условий."





