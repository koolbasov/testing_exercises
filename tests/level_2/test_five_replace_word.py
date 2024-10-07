import pytest
from functions.level_2.five_replace_word import replace_word


@pytest.mark.parametrize(
    "text, replace_from, replace_to, new_text",
    [
        ("Белка залезла на дерево", "белка", "Кошка", "Кошка залезла на дерево"),
        ("Белка залезла на дерево", "Белка", "Белка", "Белка залезла на дерево"),
        ("Белка залезла на дерево", "", "кошка", "Белка залезла на дерево"),
        ("Белка залезла на дерево", "Белка", "", " залезла на дерево"),
    ],
)
def test__replace_word__different_cases(text, replace_from, replace_to, new_text):
    assert replace_word(text, replace_from, replace_to) == new_text


@pytest.mark.parametrize(
    "text, replace_from, replace_to, expected_exception",
    [
        (123, "Белка", "Кошка", AttributeError),
        ("Белка залезла на дерево", 123, "Кошка", AttributeError),
        ("Белка залезла на дерево", "Белка", 123, TypeError),
    ],
)
def test__replace_word__exceptions(text, replace_from, replace_to, expected_exception):
    with pytest.raises(expected_exception):
        replace_word(text, replace_from, replace_to)
