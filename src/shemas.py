from pydantic import BaseModel

class WeatherRequest(BaseModel):
    city: str
    gender: str
    age_group: str
