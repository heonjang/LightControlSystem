from rest_framework import serializers

from data.models import LightIntensityPoint


class LightIntensityPointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LightIntensityPoint
        fields = ["sensor", "datetime", "value"]
