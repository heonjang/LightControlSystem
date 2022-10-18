from django.db import models

from configuration.modes import Modes


class SystemConfiguration(models.Model):
    name = models.CharField(db_index=True, primary_key=True, max_length=20)
    target_average_illumination = models.IntegerField(null=False)
    sun_rise = models.TimeField(null=False)
    sun_set = models.TimeField(null=False)
    mode = models.IntegerChoices(choices=Modes.choices)

    def __str__(self):
        return f"{self.name}-{self.target_total_illumination}-{self.sun_rise.strftime('%m-%d-%Y %H:%M:%S')}~{self.sun_set.strftime('%m-%d-%Y %H:%M:%S')}-{self.mode}"
