from django.db import models
from django.utils.translation import gettext_lazy as _


class Temperature(models.Model):
    value = models.DecimalField(
        _("Value"), help_text=_("Value is in Celsius."), max_digits=5, decimal_places=2
    )
    timestamp = models.DateTimeField(
        _("Time"), help_text=_("Date and time when measurement is taken."), auto_now_add=True
    )
