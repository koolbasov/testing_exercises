import datetime
from functions.level_1.two_date_parser import compose_datetime_from


def test_compose_datetime_from():
    assert compose_datetime_from("Today", "23:55") == datetime.datetime.combine(
        datetime.date.today(), datetime.time(23, 55)
    )
    assert compose_datetime_from("12.04.2024", "0:55") == datetime.datetime.combine(
        datetime.date.today(), datetime.time(0, 55)
    )
    assert compose_datetime_from("alarm", "7:00") == datetime.datetime.combine(
        datetime.date.today(), datetime.time(7, 0)
    )
    assert compose_datetime_from("tomorrow", "8:00") == datetime.datetime.combine(
        (datetime.date.today() + datetime.timedelta(days=1)), datetime.time(8, 0)
    )
