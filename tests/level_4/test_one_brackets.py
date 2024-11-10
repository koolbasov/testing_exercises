import pytest
from functions.level_4.one_brackets import delete_remove_brackets_quotes


@pytest.mark.parametrize(
    "name, expected_result",
    [
        ("OTTO", "OTTO"),
        ("{ OTTO }", "OTTO"),
        ("{OTTO}", "TT"),
        ("{OTTO", "T"),
        ("OTTO}", "OTTO}"),
        (" ", " "),
        ("{}", ""),
        ("{", ""),
        ("}", "}"),
        (["{", "}"], []),
        (("{", "}"), ()),
    ],
)
def test__delete_remove_brackets_quotes__expected_behavior(name, expected_result):
    assert delete_remove_brackets_quotes(name) == expected_result


@pytest.mark.parametrize(
    "name, expected_error",
    [
        ("", IndexError),
        (123, TypeError),
        ({"{": "}"}, KeyError),
    ],
)
def test_delete_remove_brackets_quotes_expected_errors(name, expected_error):
    with pytest.raises(expected_error):
        delete_remove_brackets_quotes(name)
