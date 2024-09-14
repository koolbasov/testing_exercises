from functions.level_1.five_title import change_copy_item


def test_change_copy_item():
    long_title = (
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's"
        " standard dummy text ever since the 1500s"
    )
    short_title = "Lorem Ipsum"
    title_with_text0 = "Copy of Lorem ipsum dolor sit"
    title_with_text1 = "Copy of Lorem ipsum dolor sit (67)"
    title_with_text2 = "Copy of Lorem ipsum dolor sit (68)"

    assert change_copy_item(long_title) == long_title
    assert change_copy_item(short_title) == "Copy of Lorem Ipsum"
    assert change_copy_item(title_with_text0) == "Copy of Lorem ipsum dolor sit (2)"
    assert change_copy_item(title_with_text1) == "Copy of Lorem ipsum dolor sit (68)"
    assert change_copy_item(title_with_text2) == "Copy of Lorem ipsum dolor sit (69)"
