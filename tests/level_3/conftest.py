import datetime
import decimal
import pytest

from functions.level_3.models import Expense, Currency, ExpenseCategory, BankCard

bank_card_1 = BankCard(last_digits="1234", owner="Ivan Petrov")


@pytest.fixture()
def expense_apple_january_1_24():
    return Expense(
        amount=decimal.Decimal("199.99"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="apple.com/bill",
        spent_at=datetime.datetime(2024, 1, 1, 12, 00, 00),
        category=ExpenseCategory.ONLINE_SUBSCRIPTIONS,
    )


@pytest.fixture()
def expense_metro_january_1_24():
    return Expense(
        amount=decimal.Decimal("47"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="METRO",
        spent_at=datetime.datetime(2024, 1, 1, 15, 39, 00),
        category=ExpenseCategory.TRANSPORT,
    )


@pytest.fixture()
def expense_metro_january_2_24():
    return Expense(
        amount=decimal.Decimal("47"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="METRO",
        spent_at=datetime.datetime(2024, 1, 2, 15, 39, 00),
        category=ExpenseCategory.TRANSPORT,
    )


@pytest.fixture()
def expense_metro_january_3_24():
    return Expense(
        amount=decimal.Decimal("47"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="METRO",
        spent_at=datetime.datetime(2024, 1, 3, 15, 39, 00),
        category=ExpenseCategory.TRANSPORT,
    )


@pytest.fixture()
def expense_apple_february_1_24():
    return Expense(
        amount=decimal.Decimal("199.99"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="apple.com/bill",
        spent_at=datetime.datetime(2024, 2, 1, 12, 00, 00),
        category=ExpenseCategory.ONLINE_SUBSCRIPTIONS,
    )


@pytest.fixture()
def expense_metro_february_1_24():
    return Expense(
        amount=decimal.Decimal("47"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="METRO",
        spent_at=datetime.datetime(2024, 2, 1, 15, 39, 00),
        category=ExpenseCategory.TRANSPORT,
    )


@pytest.fixture()
def expense_metro_february_2_24():
    return Expense(
        amount=decimal.Decimal("47"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="METRO",
        spent_at=datetime.datetime(2024, 2, 2, 15, 39, 00),
        category=ExpenseCategory.TRANSPORT,
    )


@pytest.fixture()
def expense_metro_february_3_24():
    return Expense(
        amount=decimal.Decimal("47"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="METRO",
        spent_at=datetime.datetime(2024, 2, 3, 15, 39, 00),
        category=ExpenseCategory.TRANSPORT,
    )


@pytest.fixture()
def expense_apple_march_1_24():
    return Expense(
        amount=decimal.Decimal("199.99"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="apple.com/bill",
        spent_at=datetime.datetime(2024, 3, 1, 12, 00, 00),
        category=ExpenseCategory.ONLINE_SUBSCRIPTIONS,
    )


@pytest.fixture()
def expense_metro_march_1_24():
    return Expense(
        amount=decimal.Decimal("47"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="METRO",
        spent_at=datetime.datetime(2024, 3, 1, 15, 39, 00),
        category=ExpenseCategory.TRANSPORT,
    )


@pytest.fixture()
def expense_metro_march_2_24():
    return Expense(
        amount=decimal.Decimal("47"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="METRO",
        spent_at=datetime.datetime(2024, 3, 2, 15, 39, 00),
        category=ExpenseCategory.TRANSPORT,
    )


@pytest.fixture()
def expense_metro_march_3_24():
    return Expense(
        amount=decimal.Decimal("47"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="METRO",
        spent_at=datetime.datetime(2024, 3, 3, 15, 39, 00),
        category=ExpenseCategory.TRANSPORT,
    )


@pytest.fixture()
def expense_apple_april_1_24():
    return Expense(
        amount=decimal.Decimal("199.99"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="apple.com/bill",
        spent_at=datetime.datetime(2024, 4, 1, 12, 00, 00),
        category=ExpenseCategory.ONLINE_SUBSCRIPTIONS,
    )


@pytest.fixture()
def expense_metro_april_1_24():
    return Expense(
        amount=decimal.Decimal("47"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="METRO",
        spent_at=datetime.datetime(2024, 4, 1, 15, 39, 00),
        category=ExpenseCategory.TRANSPORT,
    )


@pytest.fixture()
def expense_metro_april_2_24():
    return Expense(
        amount=decimal.Decimal("47"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="METRO",
        spent_at=datetime.datetime(2024, 4, 2, 15, 39, 00),
        category=ExpenseCategory.TRANSPORT,
    )


@pytest.fixture()
def expense_metro_april_3_24():
    return Expense(
        amount=decimal.Decimal("47"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="METRO",
        spent_at=datetime.datetime(2024, 4, 3, 15, 39, 00),
        category=ExpenseCategory.TRANSPORT,
    )


@pytest.fixture()
def expense_apple_may_1_24():
    return Expense(
        amount=decimal.Decimal("199.99"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="apple.com/bill",
        spent_at=datetime.datetime(2024, 5, 1, 12, 00, 00),
        category=ExpenseCategory.ONLINE_SUBSCRIPTIONS,
    )


@pytest.fixture()
def expense_metro_may_1_24():
    return Expense(
        amount=decimal.Decimal("47"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="METRO",
        spent_at=datetime.datetime(2024, 5, 1, 15, 39, 00),
        category=ExpenseCategory.TRANSPORT,
    )


@pytest.fixture()
def expense_metro_may_2_24():
    return Expense(
        amount=decimal.Decimal("47"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="METRO",
        spent_at=datetime.datetime(2024, 5, 2, 15, 39, 00),
        category=ExpenseCategory.TRANSPORT,
    )


@pytest.fixture()
def expense_metro_may_3_24():
    return Expense(
        amount=decimal.Decimal("47"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="METRO",
        spent_at=datetime.datetime(2024, 5, 3, 15, 39, 00),
        category=ExpenseCategory.TRANSPORT,
    )


@pytest.fixture()
def expense_apple_jun_1_24():
    return Expense(
        amount=decimal.Decimal("199.99"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="apple.com/bill",
        spent_at=datetime.datetime(2024, 6, 1, 12, 00, 00),
        category=ExpenseCategory.ONLINE_SUBSCRIPTIONS,
    )


@pytest.fixture()
def expense_apple_july_1_24():
    return Expense(
        amount=decimal.Decimal("199.99"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="apple.com/bill",
        spent_at=datetime.datetime(2024, 7, 1, 12, 00, 00),
        category=ExpenseCategory.ONLINE_SUBSCRIPTIONS,
    )


@pytest.fixture()
def expense_apple_august_1_24():
    return Expense(
        amount=decimal.Decimal("199.99"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="apple.com/bill",
        spent_at=datetime.datetime(2024, 8, 1, 12, 00, 00),
        category=ExpenseCategory.ONLINE_SUBSCRIPTIONS,
    )


@pytest.fixture()
def expense_apple_september_1_24():
    return Expense(
        amount=decimal.Decimal("199.99"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="apple.com/bill",
        spent_at=datetime.datetime(2024, 9, 1, 12, 00, 00),
        category=ExpenseCategory.ONLINE_SUBSCRIPTIONS,
    )


@pytest.fixture()
def expense_apple_october_1_24():
    return Expense(
        amount=decimal.Decimal("199.99"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="apple.com/bill",
        spent_at=datetime.datetime(2024, 10, 1, 12, 00, 00),
        category=ExpenseCategory.ONLINE_SUBSCRIPTIONS,
    )


@pytest.fixture()
def expense_1_october_12_24():
    return Expense(
        amount=decimal.Decimal("420.13"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="CHEBURECHNAYA SET",
        spent_at=datetime.datetime(2024, 10, 12, 12, 53, 00),
        category=ExpenseCategory.BAR_RESTAURANT,
    )


@pytest.fixture()
def expense_2_october_12_24():
    return Expense(
        amount=decimal.Decimal("223.39"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="OZERKI",
        spent_at=datetime.datetime(2024, 10, 12, 12, 53, 00),
        category=ExpenseCategory.MEDICINE_PHARMACY,
    )


@pytest.fixture()
def expense_1_october_13_24():
    return Expense(
        amount=decimal.Decimal("1003.54"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="Green Apple Shop",
        spent_at=datetime.datetime(2024, 10, 13, 11, 59, 00),
        category=ExpenseCategory.SUPERMARKET,
    )


@pytest.fixture()
def expense_2_october_13_24():
    return Expense(
        amount=decimal.Decimal("47"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="METRO",
        spent_at=datetime.datetime(2024, 10, 14, 15, 39, 00),
        category=ExpenseCategory.TRANSPORT,
    )


@pytest.fixture()
def expense_1_october_14_24():
    return Expense(
        amount=decimal.Decimal("47"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="METRO",
        spent_at=datetime.datetime(2024, 10, 14, 9, 39, 00),
        category=ExpenseCategory.TRANSPORT,
    )


@pytest.fixture()
def expense_2_october_14_24():
    return Expense(
        amount=decimal.Decimal("47"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="METRO",
        spent_at=datetime.datetime(2024, 10, 14, 18, 39, 00),
        category=ExpenseCategory.TRANSPORT,
    )


@pytest.fixture()
def expense_2_october_15_24():
    return Expense(
        amount=decimal.Decimal("0"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="METRO",
        spent_at=datetime.datetime(2024, 10, 15, 18, 39, 00),
        category=ExpenseCategory.TRANSPORT,
    )


@pytest.fixture()
def expense_pharmacy():
    return Expense(
        amount=decimal.Decimal("500"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="STOLICHKI farm",
        spent_at=datetime.datetime(2024, 10, 16, 12, 39, 00),
        category=ExpenseCategory.MEDICINE_PHARMACY,
    )


@pytest.fixture()
def expense_taxi():
    return Expense(
        amount=decimal.Decimal("480"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="www.taxi.yandex.ru",
        spent_at=datetime.datetime(2024, 10, 14, 18, 39, 00),
        category=ExpenseCategory.TRANSPORT,
    )


@pytest.fixture()
def expense_culture():
    return Expense(
        amount=decimal.Decimal("900"),
        currency=Currency.RUB,
        card=bank_card_1,
        spent_in="CINEMA GALLERIA",
        spent_at=datetime.datetime(2024, 10, 17, 21, 00, 00),
        category=ExpenseCategory.THEATRES_MOVIES_CULTURE,
    )


@pytest.fixture()
def expenses_three_days(
    expense_1_october_12_24,
    expense_2_october_12_24,
    expense_1_october_13_24,
    expense_2_october_13_24,
    expense_1_october_14_24,
    expense_2_october_14_24,
):
    return [
        expense_1_october_12_24,
        expense_2_october_12_24,
        expense_1_october_13_24,
        expense_2_october_13_24,
        expense_1_october_14_24,
        expense_2_october_14_24,
    ]


@pytest.fixture()
def expenses_ten_months(
    expense_apple_january_1_24,
    expense_metro_january_1_24,
    expense_metro_january_2_24,
    expense_metro_january_3_24,
    expense_apple_february_1_24,
    expense_metro_february_1_24,
    expense_metro_february_2_24,
    expense_metro_february_3_24,
    expense_apple_march_1_24,
    expense_metro_march_1_24,
    expense_metro_march_2_24,
    expense_metro_march_3_24,
    expense_apple_april_1_24,
    expense_metro_april_1_24,
    expense_metro_april_2_24,
    expense_metro_april_3_24,
    expense_apple_may_1_24,
    expense_metro_may_1_24,
    expense_metro_may_2_24,
    expense_metro_may_3_24,
    expense_apple_jun_1_24,
    expense_apple_july_1_24,
    expense_apple_august_1_24,
    expense_apple_september_1_24,
    expense_apple_october_1_24,
    expense_1_october_12_24,
    expense_2_october_12_24,
    expense_1_october_13_24,
    expense_2_october_13_24,
    expense_1_october_14_24,
    expense_2_october_14_24,
    expense_2_october_15_24,
    expense_pharmacy,
    expense_taxi,
    expense_culture,
):
    return [
        expense_apple_january_1_24,
        expense_metro_january_1_24,
        expense_metro_january_2_24,
        expense_metro_january_3_24,
        expense_apple_february_1_24,
        expense_metro_february_1_24,
        expense_metro_february_2_24,
        expense_metro_february_3_24,
        expense_apple_march_1_24,
        expense_metro_march_1_24,
        expense_metro_march_2_24,
        expense_metro_march_3_24,
        expense_apple_april_1_24,
        expense_metro_april_1_24,
        expense_metro_april_2_24,
        expense_metro_april_3_24,
        expense_apple_may_1_24,
        expense_metro_may_1_24,
        expense_metro_may_2_24,
        expense_metro_may_3_24,
        expense_apple_jun_1_24,
        expense_apple_july_1_24,
        expense_apple_august_1_24,
        expense_apple_september_1_24,
        expense_apple_october_1_24,
        expense_1_october_12_24,
        expense_2_october_12_24,
        expense_1_october_13_24,
        expense_2_october_13_24,
        expense_1_october_14_24,
        expense_2_october_14_24,
        expense_2_october_15_24,
        expense_pharmacy,
        expense_taxi,
        expense_culture,
    ]


@pytest.fixture()
def expenses_three_months(
    expense_apple_january_1_24,
    expense_metro_january_1_24,
    expense_metro_january_2_24,
    expense_metro_january_3_24,
    expense_apple_february_1_24,
    expense_metro_february_1_24,
    expense_metro_february_2_24,
    expense_metro_february_3_24,
    expense_apple_march_1_24,
    expense_metro_march_1_24,
    expense_metro_march_2_24,
    expense_metro_march_3_24,
):
    return [
        expense_apple_january_1_24,
        expense_metro_january_1_24,
        expense_metro_january_2_24,
        expense_metro_january_3_24,
        expense_apple_february_1_24,
        expense_metro_february_1_24,
        expense_metro_february_2_24,
        expense_metro_february_3_24,
        expense_apple_march_1_24,
        expense_metro_march_1_24,
        expense_metro_march_2_24,
        expense_metro_march_3_24,
    ]


@pytest.fixture()
def expenses_two_months(
    expense_apple_january_1_24,
    expense_metro_january_1_24,
    expense_metro_january_2_24,
    expense_metro_january_3_24,
    expense_apple_february_1_24,
    expense_metro_february_1_24,
    expense_metro_february_2_24,
    expense_metro_february_3_24,
):
    return [
        expense_apple_january_1_24,
        expense_metro_january_1_24,
        expense_metro_january_2_24,
        expense_metro_january_3_24,
        expense_apple_february_1_24,
        expense_metro_february_1_24,
        expense_metro_february_2_24,
        expense_metro_february_3_24,
    ]


@pytest.fixture()
def expenses_one_day(expense_1_october_14_24, expense_2_october_14_24):
    return [
        expense_1_october_14_24,
        expense_2_october_14_24,
    ]


@pytest.fixture()
def no_expenses():
    return []


@pytest.fixture()
def zero_expense(expense_2_october_15_24):
    return [
        expense_2_october_15_24,
    ]
