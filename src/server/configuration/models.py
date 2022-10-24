from django.db import models

from configuration.modes import Modes


class SystemConfiguration(models.Model):
    name = models.CharField(db_index=True, primary_key=True, max_length=20)
    target_average_illumination = models.IntegerField(null=False)
    sunrise = models.TimeField(null=False)
    sunset = models.TimeField(null=False)
    mode = models.IntegerField(choices=Modes.choices)

    def __str__(self):
        return f"{self.name}-{self.target_total_illumination}-{self.sunrise.strftime('%m-%d-%Y %H:%M:%S')}~{self.sunset.strftime('%m-%d-%Y %H:%M:%S')}-{self.mode}"
