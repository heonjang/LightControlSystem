import datetime
import math


def time_in_seconds(t: datetime.time) -> int:
    SECOND = 1
    MINUTE = 60 * SECOND
    HOUR = 60 * MINUTE

    return t.hour * HOUR + t.minute * MINUTE + t.second * SECOND


# This calculator will create a desired graph to offer average illumination of
# `target_average_illummination` from sunrise to sunset
# In order to maximize the efficiency, it will try to follow the Sun's solar isolation trend.
# The caculator will first calculate what would the trend be like if sun offers
# the average illumination of `target_average_illummination` betweeb sunrise and sunset
# Then, it will calculate the difference between the actual illumination and the optimal illumination
# Solar Insolation function: F = F0 * cos(theta): https://sciencing.com/calculate-solar-insolation-8435082.html
class DefaultCalculator:
    SUNRISE_ANGLE = -180
    SUNSET_ANGLE = 180

    def __init__(
        self,
        target_average_illumination: int,
        sunrise: datetime.time,
        sunset: datetime.time,
        period_in_seconds: int = 1,
    ) -> None:
        self.sunrise = sunrise
        self.sunset = sunset
        self.target_average_illumination = target_average_illumination
        self.period_in_seconds = period_in_seconds

        self.f0 = self.calculate_f0()

    def target_total_illumination(self):
        return self.target_average_illumination * self.total_number_of_points()

    def angle_change_with_one_point(self):
        return (self.SUNSET_ANGLE - self.SUNRISE_ANGLE) / self.total_number_of_points()

    def points_difference(self, t1: datetime.time, t2: datetime.time):
        seconds_difference = time_in_seconds(t2) - time_in_seconds(t1)

        return int(seconds_difference / self.period_in_seconds)

    def total_number_of_points(self):
        return self.points_difference(self.sunrise, self.sunset)

    def angle_at_one_point(self, t: datetime.time):
        if t < self.sunrise:
            return self.SUNRISE_ANGLE
        if t > self.sunset:
            return self.SUNSET_ANGLE

        points_after_sunrise = self.points_difference(self.sunrise, t)

        return (
            self.SUNRISE_ANGLE
            + points_after_sunrise * self.angle_change_with_one_point()
        )

    def calculate_f0(self):
        angles = (
            self.SUNSET_ANGLE + self.angle_change_with_one_point() * i
            for i in range(self.total_number_of_points())
        )
        cosine_sum = sum(math.cos(math.radians(angle)) + 1 for angle in angles)

        return self.target_total_illumination() / cosine_sum

    def calculate_target_illumination(self, t: datetime.time):
        angle = self.angle_at_one_point(t)

        return self.f0 * (math.cos(math.radians(angle)) + 1)

    def get_all_target_illumination(self):
        sunrise = datetime.datetime.combine(datetime.date.today(), self.sunrise)
        sunset = datetime.datetime.combine(datetime.date.today(), self.sunset)
        current = sunrise

        targets = {}

        while current < sunset:
            t = current.time()
            targets[t] = self.calculate_target_illumination(t)
            current += datetime.timedelta(seconds=self.period_in_seconds)

        return targets


if __name__ == "__main__":
    target_average_illumination = 100
    sunrise = datetime.time(8, 0, 0)
    sunset = datetime.time(19, 0, 0)
    period_in_seconds = 60

    calculator = DefaultCalculator(
        target_average_illumination, sunrise, sunset, period_in_seconds
    )

    targets = calculator.get_all_target_illumination()

    for k, v in targets.items():
        print(k, v)
