from functions.level_1.four_bank_parser import parse_ineco_expense


def test__parse_ineco_expense1(sms1, bank_cards, expense1):
    assert parse_ineco_expense(sms1, bank_cards) == expense1


def test__parse_ineco_expense2(sms2, bank_cards, expense2):
    assert parse_ineco_expense(sms2, bank_cards) == expense2
