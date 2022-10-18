import datetime
import math


def time_in_seconds(t: datetime.time) -> int:
    SECOND = 1
    MINUTE = 60 * SECOND
    HOUR = 60 * MINUTE

    return t.hour * HOUR + t.minute * MINUTE + t.second * SECOND


# This calculator will create a desired graph to offer average illumination of
# `target_average_illummination` from sun_rise to sun_set
# In order to maximize the efficiency, it will try to follow the Sun's solar isolation trend.
# The caculator will first calculate what would the trend be like if sun offers
# the average illumination of `target_average_illummination` betweeb sun_rise and sun_set
# Then, it will calculate the difference between the actual illumination and the optimal illumination
# Solar Insolation function: F = F0 * cos(theta): https://sciencing.com/calculate-solar-insolation-8435082.html
class DefaultCalculator:
    SUN_RISE_ANGLE = -180
    SUN_SET_ANGLE = 180

    def __init__(
        self,
        target_average_illumination: int,
        sun_rise: datetime.time,
        sun_set: datetime.time,
        period_in_seconds: int = 1,
    ) -> None:
        self.sun_rise = sun_rise
        self.sun_set = sun_set
        self.target_average_illumination = target_average_illumination
        self.period_in_seconds = period_in_seconds

        self.f0 = self.calculate_f0()

    def target_total_illumination(self):
        return self.target_average_illumination * self.total_number_of_points()

    def angle_change_with_one_point(self):
        return (
            self.SUN_SET_ANGLE - self.SUN_RISE_ANGLE
        ) / self.total_number_of_points()

    def points_difference(self, t1: datetime.time, t2: datetime.time):
        seconds_difference = time_in_seconds(t2) - time_in_seconds(t1)

        return int(seconds_difference / self.period_in_seconds)

    def total_number_of_points(self):
        return self.points_difference(self.sun_rise, self.sun_set)

    def angle_at_one_point(self, t: datetime.time):
        if t < self.sun_rise:
            raise ValueError
        if t > self.sun_set:
            raise ValueError

        points_after_sun_rise = self.points_difference(self.sun_rise, t)

        return (
            self.SUN_RISE_ANGLE
            + points_after_sun_rise * self.angle_change_with_one_point()
        )

    def calculate_f0(self):
        angles = (
            self.SUN_SET_ANGLE + self.angle_change_with_one_point() * i
            for i in range(self.total_number_of_points())
        )
        cosine_sum = sum(math.cos(math.radians(angle)) + 1 for angle in angles)

        return self.target_total_illumination() / cosine_sum

    def calculate_target_illumination(self, t: datetime.time):
        angle = self.angle_at_one_point(t)

        return self.f0 * (math.cos(math.radians(angle)) + 1)

    def get_all_target_illumination(self):
        sun_rise = datetime.datetime.combine(datetime.date.today(), self.sun_rise)
        sun_set = datetime.datetime.combine(datetime.date.today(), self.sun_set)
        current = sun_rise

        targets = {}

        while current < sun_set:
            t = current.time()
            targets[t] = self.calculate_target_illumination(t)
            current += datetime.timedelta(seconds=self.period_in_seconds)

        return targets


if __name__ == "__main__":
    target_average_illumination = 100
    sun_rise = datetime.time(8, 0, 0)
    sun_set = datetime.time(19, 0, 0)
    period_in_seconds = 60

    calculator = DefaultCalculator(
        target_average_illumination, sun_rise, sun_set, period_in_seconds
    )

    targets = calculator.get_all_target_illumination()

    for k, v in targets.items():
        print(k, v)
