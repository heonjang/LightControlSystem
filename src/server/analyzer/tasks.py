import datetime
import logging

from analyzer.models import IlluminationDifferenceFromTarget
from configuration.calculator.default import DefaultCalculator
from common.time import time_add
from data.models import LightIntensityPoint

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def run_analyzer(
    sensor,
    target_average_illumination,
    sunrise_str: str,
    sunset_str: str,
    period_in_seconds: int,
    now: datetime.datetime,
    speed: int = 1,
):
    assert period_in_seconds > speed
    assert period_in_seconds / speed == 0

    day_in_seconds = 24 * 60 * 60

    for i in range(0, day_in_seconds, speed):
        current = now + datetime.timedelta(seconds=i)
        if i % period_in_seconds == 0:
            calculate_current_difference_and_save(
                sensor=sensor,
                target_average_illumination=target_average_illumination,
                sunrise_str=sunrise_str,
                sunset_str=sunset_str,
                period_in_seconds=period_in_seconds,
                now=current,
            )


def calculate_current_difference_and_save(
    sensor: str,
    target_average_illumination: int,
    sunrise_str: str,
    sunset_str: str,
    period_in_seconds: int,
    now: datetime.datetime,
):
    datetime_str = "2022-10-23 {time_str}"
    sunrise = datetime.datetime.strptime(
        datetime_str.format(time_str=sunrise_str), "%Y-%m-%d %H:%M:%S"
    ).time()
    sunset = datetime.datetime.strptime(
        datetime_str.format(time_str=sunset_str), "%Y-%m-%d %H:%M:%S"
    ).time()

    calculator = DefaultCalculator(
        target_average_illumination, sunrise, sunset, period_in_seconds
    )
    analyer = IlluminationDifferenceAnalyzer(calculator, sensor=sensor)

    analyer.calculate_current_difference_and_save(now)


class IlluminationDifferenceAnalyzer:
    def __init__(self, calculator, sensor):
        self.calculator = calculator
        self.sensor = sensor

    def calculate_difference(self, dt: datetime.datetime):
        period_in_seconds = self.calculator.period_in_seconds

        dt_lte = dt
        dt_gte = dt - datetime.timedelta(seconds=period_in_seconds)

        average_value = (
            LightIntensityPoint.get_average_value(self.sensor, dt_lte, dt_gte) or 0
        )

        target_illumination = self.calculator.calculate_target_illumination(dt.time())

        return target_illumination - average_value

    def calculate_current_difference_and_save(self, now: datetime.datetime):
        sensor = self.sensor
        difference = self.calculate_difference(now)

        return IlluminationDifferenceFromTarget.objects.create(
            sensor=sensor, time=now, value=difference
        )
