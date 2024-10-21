import datetime
import decimal
import pytest
from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense


@pytest.fixture()
def bank_cards():
    return [BankCard("1234", "Ivan Petrov"), BankCard("5678", "Petr Ivanov")]


@pytest.fixture()
def sms1():
    return SmsMessage(
        "984.89 руб., 1234123412341234 12.10.24 20:33 OKEY authcode 5432", "InecoBank", datetime.datetime.now()
    )


@pytest.fixture()
def sms2():
    return SmsMessage(
        "99.99 руб., 1234123412345678 12.10.24 14:33 AppStore authcode 2321", "InecoBank", datetime.datetime.now()
    )


@pytest.fixture()
def expense1():
    return Expense(
        amount=decimal.Decimal("984.89"),
        card=BankCard("1234", "Ivan Petrov"),
        spent_in="OKEY",
        spent_at=datetime.datetime.strptime("12.10.24 20:33", "%d.%m.%y %H:%M"),
    )


@pytest.fixture()
def expense2():
    return Expense(
        amount=decimal.Decimal("99.99"),
        card=BankCard("5678", "Petr Ivanov"),
        spent_in="AppStore",
        spent_at=datetime.datetime.strptime("12.10.24 14:33", "%d.%m.%y %H:%M"),
    )
