import pytest
import datetime
import decimal
from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense

cards = [BankCard("1234", "Ivan Petrov"), BankCard("5678", "Petr Ivanov")]
sms1 = SmsMessage(
    "984.89 руб., 1234123412341234 12.10.24 20:33 OKEY authcode 5432", "InecoBank", datetime.datetime.now()
)
sms2 = SmsMessage(
    "99.99 руб., 1234123412345678 12.10.24 14:33 AppStore authcode 2321", "InecoBank", datetime.datetime.now()
)
expense1 = Expense(
    amount=decimal.Decimal("984.89"),
    card=BankCard("1234", "Ivan Petrov"),
    spent_in="OKEY",
    spent_at=datetime.datetime.strptime("12.10.24 20:33", "%d.%m.%y %H:%M"),
)
expense2 = Expense(
    amount=decimal.Decimal("99.99"),
    card=BankCard("5678", "Petr Ivanov"),
    spent_in="AppStore",
    spent_at=datetime.datetime.strptime("12.10.24 14:33", "%d.%m.%y %H:%M"),
)


@pytest.mark.parametrize("sms, cards, expense", [(sms1, cards, expense1), (sms2, cards, expense2)])
def test__parse_ineco_expense(sms, cards, expense):
    assert parse_ineco_expense(sms, cards) == expense
