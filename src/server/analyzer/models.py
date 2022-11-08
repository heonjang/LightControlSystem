from django.db import models
from django.db.models import Avg


class IlluminationDifferenceFromTarget(models.Model):
    sensor = models.CharField(db_index=True, max_length=20)
    time = models.DateTimeField(auto_now_add=True, db_index=True, null=False)
    value = models.FloatField(null=False)

    def __str__(self):
        return f"{self.sensor}-{self.time.strftime('%m-%d-%Y %H:%M:%S')}-{self.value}"
