import requests
import json
from fastapi import HTTPException
from starlette import status

from config import API_URL, FILE_REC


def load_recommendations():
    with open(FILE_REC, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_weather_and_recommendations(city: str, gender: str, age_group: str):
    if gender.lower() == "женский":
        gender = "female"
    elif gender.lower() == "мужской":
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
        if not 200 <= response.status_code < 300:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Погодный сервис не дал корректный ответ")
        weather_data = response.json()
    except requests.exceptions.HTTPError as http_err:
        raise HTTPException(status_code=400, detail="Ошибка погодного сервера")
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))

    temperatures = [entry['main']['temp'] - 273.15 for entry in weather_data['list']]
    weather_conditions = [entry['weather'][0]['main'] for entry in weather_data['list'] if entry['weather']]

    precipitation_found = any(cond in ["Thunderstorm", "Drizzle", "Rain", "Snow"] for cond in weather_conditions)

    precipitation_category = "any"
    if precipitation_found:
        if any(cond in ["Rain", "Drizzle"] for cond in weather_conditions):
            precipitation_category = "rain"
        elif any(cond == "Snow" for cond in weather_conditions):
            precipitation_category = "snow"

    recommendations = find_recommendations(gender, age_group, temperatures, precipitation_category)

    return {
        "weather": weather_data,
        "recommendations": recommendations
    }


def find_recommendations(gender: str, age_group: str, temperatures: list, precipitation_category: str):
    recommendations_data = load_recommendations()

    temperature = sum(temperatures) // len(temperatures)

    for rec in recommendations_data['recommendations']:
        if rec['gender'] == gender and rec['age_group'] == age_group:
            precipitations = [el['precipitation'] for el in rec['weather_precipitation']]

            if precipitation_category not in precipitations:
                precipitation_category = "any"

            for weather_condition in rec['weather_precipitation']:
                if weather_condition['temperature_range'][0] <= temperature <= \
                        weather_condition['temperature_range'][1]:
                    if weather_condition['precipitation'] == precipitation_category:
                        return weather_condition['recommendation']

    return "Нет рекомендаций для данных условий."
