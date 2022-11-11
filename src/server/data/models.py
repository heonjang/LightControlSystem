from django.db import models
from django.db.models import Avg


class LightIntensityPoint(models.Model):
    sensor = models.CharField(db_index=True, max_length=20)
    datetime = models.DateTimeField(db_index=True, null=False)
    value = models.FloatField(null=False)

    def __str__(self):
        return (
            f"{self.sensor}-{self.datetime.strftime('%m-%d-%Y %H:%M:%S')}-{self.value}"
        )

    @classmethod
    def get_average_value(cls, sensor, dt_gte, dt_lte):
        qs = cls.objects.filter(
            sensor=sensor, datetime__gte=dt_gte, datetime__lte=dt_lte
        ).aggregate(Avg("value"))

        return qs["value__avg"] or 0
