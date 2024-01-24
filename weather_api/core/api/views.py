from datetime import datetime

from django.db.models import QuerySet
from django.utils.decorators import method_decorator
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView

from weather_api.core.api.serializers import TemperatureSerializer
from weather_api.core.decorators import enforce_anti_spam_token_check
from weather_api.core.models import Temperature


@extend_schema(
    parameters=[
        OpenApiParameter("day", type=OpenApiTypes.DATE),
        OpenApiParameter("X-Token", location=OpenApiParameter.HEADER),
    ]
)
@method_decorator(enforce_anti_spam_token_check, "get")
class TemperatureListView(ListAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

    def get_queryset(self) -> QuerySet[Temperature]:
        qs = super().get_queryset()
        date = self.request.query_params.get("day")
        if date:
            try:
                date = datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                raise ValidationError("'day' query parameter is invalid.")

            qs = qs.filter(timestamp__date=date)

        return qs
