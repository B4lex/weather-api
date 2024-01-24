from django.contrib import admin

from weather_api.core.models import Temperature


@admin.register(Temperature)
class TemperatureAdmin(admin.ModelAdmin):
    list_display = ("value", "timestamp")
