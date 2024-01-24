from decimal import Decimal

import requests
from django.conf import settings


class OpenWeatherAPIClient:
    BASE_URL = "http://api.openweathermap.org/"

    @classmethod
    def get_current_temperature(cls) -> Decimal:
        city_lat, city_lon = cls.get_city_coordinates()
        response = requests.get(
            f"{cls.BASE_URL}data/2.5/weather",
            {
                "lat": city_lat,
                "lon": city_lon,
                "units": "metric",  # for Celsius values
                "appid": settings.OPEN_WEATHER_API_KEY,
            },
        )
        response.raise_for_status()
        return response.json()["main"]["temp"]

    @classmethod
    def get_city_coordinates(cls) -> tuple[Decimal, Decimal]:
        response = requests.get(
            f"{cls.BASE_URL}geo/1.0/direct",
            {
                "q": settings.CITY_NAME,
                "limit": 1,  # we don't need to look for more than 1 place
                "appid": settings.OPEN_WEATHER_API_KEY,
            },
        )
        response.raise_for_status()
        city_data = response.json()[0]
        return city_data["lat"], city_data["lon"]
