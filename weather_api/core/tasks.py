from celery import shared_task

from weather_api.core.api_client import OpenWeatherAPIClient
from weather_api.core.models import Temperature


@shared_task(ignore_result=True)
def retrieve_temperature_data():
    temperature_value = OpenWeatherAPIClient.get_current_temperature()
    Temperature.objects.create(value=temperature_value)
