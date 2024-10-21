import pytest
import decimal
from statistics import StatisticsError

from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses


@pytest.mark.parametrize(
    "expenses, expected_result",
    [
        ("expenses_three_days", decimal.Decimal("596.02")),
        ("expenses_one_day", decimal.Decimal("94")),
        ("zero_expense", decimal.Decimal("0")),
    ],
)
def test__calculate_average_daily_expenses__expected_behavior(expenses, expected_result, request):
    assert calculate_average_daily_expenses(request.getfixturevalue(expenses)) == expected_result


def test__calculate_average_daily_expenses__no_expenses(no_expenses):
    with pytest.raises(StatisticsError):
        calculate_average_daily_expenses(no_expenses)


def test__calculate_average_daily_expenses__wrong_data():
    with pytest.raises(TypeError):
        calculate_average_daily_expenses(123)
