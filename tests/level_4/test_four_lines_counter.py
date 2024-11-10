import pytest

from functions.level_4.four_lines_counter import count_lines_in


@pytest.mark.parametrize(
    "filepath, expected_result",
    [
        ("filepath_no_file", None),
        ("filepath_two_lines", 2),
        ("filepath_three_lines_three_sharps", 3),
        ("filepath_no_lines", 0),
    ],
)
def test__count_lines_in__no_lines(filepath, expected_result, request):
    assert count_lines_in(request.getfixturevalue(filepath)) is expected_result


def test__count_lines_in__type_error():
    with pytest.raises(TypeError):
        count_lines_in(["file.txt", "file2.txt"])
