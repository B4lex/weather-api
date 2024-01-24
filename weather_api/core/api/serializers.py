from rest_framework import serializers

from weather_api.core.models import Temperature


class TemperatureSerializer(serializers.ModelSerializer):
    temperature = serializers.DecimalField(
        read_only=True, source="value", max_digits=5, decimal_places=2
    )

    class Meta:
        model = Temperature
        fields = ["temperature"]
