import pytest
from functions.level_2.three_first import first, NOT_SET


def test__first__correct_items_no_default():
    items = [1, 2, 3, 4, 5]

    result = first(items)

    assert result == 1


def test__first__default_not_set():
    items = []

    with pytest.raises(AttributeError):
        first(items)


def test__first__default_equals_int():
    items = []
    default = 6

    result = first(items, default)

    assert result == 6


def test__first__default_equals_none():
    items = []
    default = None

    result = first(items, default)

    assert result is None


def test__first__wrong_items():
    items = 12

    with pytest.raises(TypeError):
        first(items)
