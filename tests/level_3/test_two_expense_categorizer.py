import pytest

from functions.level_3.two_expense_categorizer import guess_expense_category, is_string_contains_trigger
from functions.level_3.models import ExpenseCategory


@pytest.mark.parametrize(
    "expense, expected_result",
    [
        ("expense_1_october_12_24", ExpenseCategory.BAR_RESTAURANT),
        ("expense_1_october_13_24", ExpenseCategory.SUPERMARKET),
        ("expense_apple_october_1_24", ExpenseCategory.ONLINE_SUBSCRIPTIONS),
        ("expense_pharmacy", ExpenseCategory.MEDICINE_PHARMACY),
        ("expense_culture", ExpenseCategory.THEATRES_MOVIES_CULTURE),
        ("expense_taxi", ExpenseCategory.TRANSPORT),
        ("expense_1_october_14_24", None),
    ],
)
def test__guess_expense_category__expected_behavior(expense, expected_result, request):
    assert guess_expense_category(request.getfixturevalue(expense)) is expected_result


def test__guess_expense_category__wrong_expense():
    with pytest.raises(AttributeError):
        guess_expense_category(123)


# тут решил, что если использовать фикстуры, то получится больше кода, поэтому сделал через parametrize
@pytest.mark.parametrize(
    "string, trigger, expected_result",
    [
        ("ABC", "abc", True),
        ("abc,DEFG", "abc", True),
        ("DEFG.abc", "abc", True),
        ("DEFG abc KFDG", "abc", True),
        ("DEFG-abc-KFDG", "abc", True),
        ("DEFG/abc/KFDG", "abc", True),
        ("DEFG\\abc\\KFDG", "abc", True),
        ("DEFG+abc KFDG", "abc", False),
        ("ABC", "ABC", False),
        ("DEFGKFDG", "abc", False),
    ],
)
def test__is_string_contains_trigger__expected_behavior(string, trigger, expected_result):
    assert is_string_contains_trigger(string, trigger) is expected_result


def test__is_string_contains_trigger__wrong_string():
    with pytest.raises(AttributeError):
        is_string_contains_trigger(124, "abc")
