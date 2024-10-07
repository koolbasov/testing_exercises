import pytest
import datetime
from functions.level_1.two_date_parser import compose_datetime_from


@pytest.mark.parametrize(
    "date, time, expected_datetime",
    [
        ("Today", "23:55", datetime.datetime.combine(datetime.date.today(), datetime.time(23, 55))),
        ("12.04.2024", "0:55", datetime.datetime.combine(datetime.date.today(), datetime.time(0, 55))),
        ("alarm", "7:00", datetime.datetime.combine(datetime.date.today(), datetime.time(7, 0))),
        (
            "tomorrow",
            "8:00",
            datetime.datetime.combine((datetime.date.today() + datetime.timedelta(days=1)), datetime.time(8, 0)),
        ),
    ],
)
def test__compose_datetime_from(date, time, expected_datetime):
    assert compose_datetime_from(date, time) == expected_datetime
