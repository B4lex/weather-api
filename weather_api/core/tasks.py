import logging

from celery import shared_task
from django.conf import settings
from django.utils import timezone

from weather_api.core.api_client import OpenWeatherAPIClient
from weather_api.core.models import Temperature

logger = logging.getLogger(__name__)


@shared_task(ignore_result=True)
def retrieve_temperature_data():
    temperature_value = OpenWeatherAPIClient.get_current_temperature()
    Temperature.objects.create(value=temperature_value)
    logger.info("Retrieved temperature in %s at %s", settings.CITY_NAME, timezone.now())
