from django.urls import path

from weather_api.core.api.views import TemperatureListView

urlpatterns = [path("temperatures/", TemperatureListView.as_view(), name="temperature-list")]
