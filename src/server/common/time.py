import datetime


def time_add(t: datetime.time, timedelta: datetime.timedelta):
    dt = datetime.datetime.combine(datetime.date.today(), t)
    dt += timedelta

    return dt.time()
