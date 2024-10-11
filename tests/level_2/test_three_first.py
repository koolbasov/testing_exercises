import pytest
from functions.level_2.three_first import first, NOT_SET


@pytest.mark.parametrize(
    "items, default, expected_result",
    [
        ([], 6, 6),
        ([], None, None),
        ([1, 2, 3, 4, 5], None, 1),
    ],
)
def test__first__no_items_different_defaults(items, default, expected_result):
    assert first(items, default) == expected_result


@pytest.mark.parametrize(
    "items, exception",
    [
        ([], AttributeError),
        (12, TypeError),
    ],
)
def test__first__exceptions(items, exception):
    with pytest.raises(exception):
        first(items)
