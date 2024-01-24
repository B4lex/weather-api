from django.db import migrations
from django_celery_beat.models import HOURS, MINUTES


def create_periodic_task(apps, _):
    PeriodicTask = apps.get_model("django_celery_beat", "PeriodicTask")
    IntervalSchedule = apps.get_model("django_celery_beat", "IntervalSchedule")

    hourly_interval, _ = IntervalSchedule.objects.get_or_create(every=1, period=MINUTES)

    PeriodicTask.objects.get_or_create(
        task="weather_api.core.tasks.retrieve_temperature_data",
        name="Periodic task to retrieve historical temperatures data from OpenWeather API",
        interval=hourly_interval,
    )


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            create_periodic_task,
            migrations.RunPython.noop,
            elidable=True
        )
    ]
