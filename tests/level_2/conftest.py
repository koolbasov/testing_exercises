import pytest


@pytest.fixture()
def good_words():
    return set(("милые", "пушистые", "красивые"))


@pytest.fixture()
def bad_words():
    return set(("противные", "вонючие", "мерзкие"))
