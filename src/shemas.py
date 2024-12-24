from pydantic import BaseModel
from typing import List, Optional


class WeatherRequest(BaseModel):
    city: str
    gender: str
    age_group: str


class WeatherCondition(BaseModel):
    id: int
    main: str
    description: str
    icon: str


class MainData(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    sea_level: Optional[int] = None
    grnd_level: Optional[int] = None
    humidity: int
    temp_kf: float


class CloudData(BaseModel):
    all: int


class WindData(BaseModel):
    speed: float
    deg: int
    gust: Optional[float] = None


class WeatherEntry(BaseModel):
    dt: int
    main: MainData
    weather: List[WeatherCondition]
    clouds: CloudData
    wind: WindData
    visibility: int | None = None
    pop: float
    sys: dict
    dt_txt: str


class CityCoord(BaseModel):
    lat: float
    lon: float


class CityData(BaseModel):
    id: int
    name: str
    coord: CityCoord
    country: str
    population: int
    timezone: int
    sunrise: int
    sunset: int


class WeatherResponse(BaseModel):
    list: List[WeatherEntry]
    city: CityData


class WeatherRecResponse(BaseModel):
    weather: WeatherResponse
    recommendations: str
