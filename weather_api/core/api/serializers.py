from rest_framework import serializers

from weather_api.core.models import Temperature


class TemperatureSerializer(serializers.ModelSerializer):
    temperature = serializers.ReadOnlyField(source="value")

    class Meta:
        model = Temperature
        fields = ["temperature", "timestamp"]
