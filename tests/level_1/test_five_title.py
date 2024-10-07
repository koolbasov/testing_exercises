import pytest
from functions.level_1.five_title import change_copy_item

long_title = (
    "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's"
    " standard dummy text ever since the 1500s"
)


@pytest.mark.parametrize(
    "input_title,expected_title",
    [
        (long_title, long_title),
        ("Lorem Ipsum", "Copy of Lorem Ipsum"),
        ("Copy of Lorem ipsum dolor sit", "Copy of Lorem ipsum dolor sit (2)"),
        ("Copy of Lorem ipsum dolor sit (67)", "Copy of Lorem ipsum dolor sit (68)"),
        ("Copy of Lorem ipsum dolor sit (68)", "Copy of Lorem ipsum dolor sit (69)"),
    ],
)
def test__change_copy_item(input_title, expected_title):
    assert change_copy_item(input_title) == expected_title
