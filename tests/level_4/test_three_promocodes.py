import pytest
from unittest.mock import patch

from functions.level_4.three_promocodes import generate_promocode


@pytest.mark.parametrize(
    "promocode_len, expected_len",
    [
        (8, 8),
        (1, 1),
        (0, 0),
        (-8, 0),
    ],
)
def test__generate_promocode__expected_behavior(promocode_len, expected_len):
    assert len(generate_promocode(promocode_len)) == expected_len


def test__generate_promocode__expected_result_no_argument():
    with patch("random.choice") as random_choice_mock:
        random_choice_mock.return_value = "A"
        assert generate_promocode() == "AAAAAAAA"


def test__generate_promocode__expected_result_with_argument():
    with patch("random.choice") as random_choice_mock:
        random_choice_mock.return_value = "A"
        assert generate_promocode(5) == "AAAAA"


def test__generate_promocode__expected_error():
    with pytest.raises(TypeError):
        generate_promocode("jhkjhkj")
