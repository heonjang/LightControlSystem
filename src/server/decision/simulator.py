import datetime

from decision.models import Decision
from configuration.calculator.default import DefaultCalculator
from data.models import LightIntensityPoint


TEST_SENSOR = "test"
calculator = DefaultCalculator(1000, datetime.time(7, 0), datetime.time(17, 0), 10)


def test_make_decision(dt):
    Decision.make_decision(
        "test",
        dt=dt,
        timeout_sec=5,
        adjustment_period=1,
        calculator=calculator,
    )


def test_1():
    dt1 = datetime.datetime(2022, 11, 11, 11, 11, 11)
    dt2 = dt1 + datetime.timedelta(minutes=1)

    Decision.objects.create(sensor=TEST_SENSOR, time=dt1, blind=10, light=0)
    test_make_decision(dt2)

    d = Decision.objects.filter(sensor=TEST_SENSOR, time=dt2).last()

    assert d.blind > 10
    assert d.light == 0


def test_2():
    dt1 = datetime.datetime(2022, 11, 12, 11, 11, 11)
    dt2 = dt1 + datetime.timedelta(minutes=1)

    temp_dt = dt2
    for i in range(5):
        temp_dt += datetime.timedelta(seconds=1)
        LightIntensityPoint.objects.create(
            sensor=TEST_SENSOR, datetime=temp_dt, value=2000
        )
    Decision.objects.create(sensor=TEST_SENSOR, time=dt1, blind=10, light=0)
    test_make_decision(dt2)

    d = Decision.objects.filter(sensor=TEST_SENSOR, time=dt2).last()

    assert d.blind == 0
    assert d.light == 0


def test_3():
    dt1 = datetime.datetime(2022, 11, 13, 11, 11, 11)
    dt2 = dt1 + datetime.timedelta(minutes=1)

    Decision.objects.create(sensor=TEST_SENSOR, time=dt1, blind=80, light=0)
    test_make_decision(dt2)

    d = Decision.objects.filter(sensor=TEST_SENSOR, time=dt2).last()

    assert d.blind == 90
    assert d.light > 0


def test_4():
    dt1 = datetime.datetime(2022, 11, 14, 11, 11, 11)
    dt2 = dt1 + datetime.timedelta(minutes=1)

    Decision.objects.create(sensor=TEST_SENSOR, time=dt1, blind=90, light=1000)
    test_make_decision(dt2)

    d = Decision.objects.filter(sensor=TEST_SENSOR, time=dt2).last()

    assert d.blind == 90
    assert d.light == 1000
