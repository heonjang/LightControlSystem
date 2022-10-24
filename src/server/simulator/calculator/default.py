import datetime

from configuration.calculator.default import DefaultCalculator


def test1():
    target_average_illumination = 100
    sunrise = datetime.time(8, 0, 0)
    sunset = datetime.time(19, 0, 0)
    period_in_seconds = 60

    calculator = DefaultCalculator(
        target_average_illumination, sunrise, sunset, period_in_seconds
    )

    targets = calculator.get_all_target_illumination()

    for k, v in targets.items():
        assert v >= 0

    average = sum(v for _, v in targets.items()) / len(targets)
    assert abs(average - target_average_illumination) < 0.1

    print("test1 passed")


def test2():
    target_average_illumination = 100
    sunrise = datetime.time(8, 0, 0)
    sunset = datetime.time(19, 0, 0)
    period_in_seconds = 1

    calculator = DefaultCalculator(
        target_average_illumination, sunrise, sunset, period_in_seconds
    )

    targets = calculator.get_all_target_illumination()

    for k, v in targets.items():
        assert v >= 0

    average = sum(v for _, v in targets.items()) / len(targets)
    assert abs(average - target_average_illumination) < 0.1

    print("test2 passed")


if __name__ == "__main__":
    test1()
    test2()
