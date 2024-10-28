import pytest

from functions.level_3.three_is_subscription import is_subscription


@pytest.mark.parametrize(
    "expense, expenses, expected_result",
    [
        ("expense_apple_april_1_24", "expenses_ten_months", True),
        ("expense_metro_march_1_24", "expenses_ten_months", False),
        ("expense_pharmacy", "expenses_ten_months", False),
        ("expense_apple_april_1_24", "expenses_three_months", True),
        ("expense_apple_april_1_24", "expenses_two_months", False),
    ],
)
def test__is_subscription__expected_behavior(expense, expenses, expected_result, request):
    assert is_subscription(request.getfixturevalue(expense), request.getfixturevalue(expenses)) is expected_result


def test__is_subscription__wrong_expense(expenses_ten_months):
    with pytest.raises(AttributeError):
        is_subscription("1345", expenses_ten_months)


def test__is_subscription__wrong_expenses_list(expense_apple_april_1_24):
    with pytest.raises(AttributeError):
        is_subscription(expense_apple_april_1_24, "12345")
