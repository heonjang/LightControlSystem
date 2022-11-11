import datetime
import time

from django.db import models

from data.models import LightIntensityPoint
from decision.command import adjust_blind, adjust_LED


class DecisionMaker:
    BLIND_ANGLE_CEILING = 90  # blind cannot have its angle greater than this
    BLIND_ANGLE_UNIT = 10  # blind adjust its angle this much at once
    LIGHT_POWER_CEILING = 1000  # LED lights cannot have power greater than this
    LIGHT_POWER_UNIT = 100  # LED lights cannot adjust power this much at once

    @classmethod
    def decide(cls, blind: float, light: float, intensity_diff: float):
        # light's intensity has to increase
        if intensity_diff > 0:
            if blind + cls.BLIND_ANGLE_UNIT > cls.BLIND_ANGLE_CEILING:
                if light >= cls.LIGHT_POWER_CEILING:
                    # both blind and light hit the maximum
                    pass
                else:
                    light += cls.LIGHT_POWER_UNIT
                    adjust_LED(cls.LIGHT_POWER_UNIT)
            else:
                blind += cls.BLIND_ANGLE_UNIT
                adjust_blind(cls.BLIND_ANGLE_UNIT)

        if intensity_diff < 0:
            if light <= 0:
                if blind <= 0:
                    # both blind and light hit the minimum
                    pass
                else:
                    blind -= cls.BLIND_ANGLE_UNIT
                    adjust_blind(-cls.BLIND_ANGLE_UNIT)
            else:
                light -= cls.LIGHT_POWER_UNIT
                adjust_LED(-cls.LIGHT_POWER_UNIT)

        return blind, light


class Decision(models.Model):
    INTENSITY_ERROR_MARGIN = 100

    sensor = models.CharField(db_index=True, max_length=20)
    time = models.DateTimeField(db_index=True, null=False)
    blind = models.FloatField(null=False)
    light = models.FloatField(null=False)

    @classmethod
    def get_previous_blind_and_light(cls, sensor: str, dt: datetime.datetime):
        previous_decision = (
            Decision.objects.filter(sensor=sensor, time__lt=dt)
            .order_by("-time")
            .first()
        )

        if not previous_decision:
            return 0, 0
        else:
            return previous_decision.blind, previous_decision.light

    @classmethod
    def make_decision(
        cls,
        sensor: str,
        dt: datetime.datetime,
        timeout_sec: int,
        adjustment_period: int,
        calculator,
    ):
        blind, light = cls.get_previous_blind_and_light(sensor=sensor, dt=dt)

        i = 0

        dt_gte = dt - datetime.timedelta(seconds=adjustment_period)
        dt_lte = dt

        while i < timeout_sec:
            average_illumination = LightIntensityPoint.get_average_value(
                sensor, dt_gte, dt_lte
            )
            target_illumination = calculator.calculate_target_illumination(
                dt_lte.time()
            )
            illumination_diff = target_illumination - average_illumination
            if abs(illumination_diff) < cls.INTENSITY_ERROR_MARGIN:
                break

            blind, light = DecisionMaker.decide(blind, light, illumination_diff)

            i += adjustment_period
            dt_gte += datetime.timedelta(seconds=adjustment_period)
            dt_lte += datetime.timedelta(seconds=adjustment_period)
            time.sleep(adjustment_period)

        Decision.objects.create(sensor=sensor, time=dt, blind=blind, light=light)
