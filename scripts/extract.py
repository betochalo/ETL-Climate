"""Extracts data from the raw data files."""
import requests
from config.settings import settings

def extract_data_from_openweathermap(lat: float, lon: float):
    """Extracts data from the OpenWeatherMap raw data file."""
    params = {
        "lat": lat,
        "lon": lon,
        "API_KEY": settings.OPEN_WEATHER_MAP_API_KEY
    }
    response = requests.get(
        "https://api.openweathermap.org/data/3.0/onecall", params=params, timeout=10
    )
    return response.json()

def extract_data_from_openmeteo(lat: float, lon: float):
    """Extracts data from the OpenMeteo raw data file."""
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m",
    }
    responses = requests.get(
        "https://api.open-meteo.com/v1/forecast", params=params, timeout=10
    )
    return responses.json()

data = extract_data_from_openmeteo(0.35171, -78.12233)
