import pytest
from functions.level_1.one_gender import genderalize


@pytest.mark.parametrize(
    "verb_male, verb_female, gender, expected_verb",
    [
        ("программировал", "программировала", "male", "программировал"),
        ("тестировал", "тестировала", "female", "тестировала"),
    ],
)
def test__genderalize(verb_male, verb_female, gender, expected_verb):
    assert genderalize(verb_male, verb_female, gender) == expected_verb
