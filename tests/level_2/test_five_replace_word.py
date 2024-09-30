import pytest
from functions.level_2.five_replace_word import replace_word


def test__replace_word__different_word():
    text = "Белка залезла на дерево"
    replace_from = "белка"
    replace_to = "Кошка"

    new_text = replace_word(text, replace_from, replace_to)

    assert new_text == "Кошка залезла на дерево"


def test__replace_word__same_word():
    text = "Белка залезла на дерево"
    replace_from = "Белка"
    replace_to = "Белка"

    new_text = replace_word(text, replace_from, replace_to)

    assert new_text == "Белка залезла на дерево"


def test__replace_word__no_replace_from():
    text = "Белка залезла на дерево"
    replace_from = ""
    replace_to = "кошка"

    new_text = replace_word(text, replace_from, replace_to)

    assert new_text == "Белка залезла на дерево"


def test__replace_word__no_replace_to():
    text = "Белка залезла на дерево"
    replace_from = "Белка"
    replace_to = ""

    new_text = replace_word(text, replace_from, replace_to)

    assert new_text == " залезла на дерево"


def test__replace_word__wrong_type_text():
    text = 123
    replace_from = "Белка"
    replace_to = "Кошка"

    with pytest.raises(AttributeError):
        replace_word(text, replace_from, replace_to)


def test__replace_word__wrong_type_replace_from():
    text = "Белка залезла на дерево"
    replace_from = 123
    replace_to = "Кошка"

    with pytest.raises(AttributeError):
        replace_word(text, replace_from, replace_to)


def test__replace_word__wrong_type_replace_to():
    text = "Белка залезла на дерево"
    replace_from = "Белка"
    replace_to = 123

    with pytest.raises(TypeError):
        replace_word(text, replace_from, replace_to)
