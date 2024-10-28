import pytest
from functions.level_4.two_students import get_student_by_tg_nickname


@pytest.mark.parametrize(
    "telegram_username, students, expected_result",
    [
        ("ivan_petrov", "list_of_students", "student_1"),
        ("@ivan_petrov", "list_of_students", "return_none"),
        ("igor_smirnov", "list_of_students", "return_none"),
        (12345, "list_of_students", "return_none"),
        ({}, "list_of_students", "return_none"),
        ([], "list_of_students", "return_none"),
        ("igor_smirnov", "empty_list", "return_none"),
        ("igor_smirnov", "empty_dict", "return_none"),
        ("igor_smirnov", "empty_tuple", "return_none"),
    ],
)
def test__get_student_by_tg_nickname__expected_behavior(telegram_username, students, expected_result, request):
    assert get_student_by_tg_nickname(telegram_username, request.getfixturevalue(students)) is request.getfixturevalue(
        expected_result
    )


def test__get_student_by_tg_nickname__expect_type_error():
    with pytest.raises(TypeError):
        get_student_by_tg_nickname("ivan_petrov", 123)


def test__get_student_by_tg_nickname__expect_attribute_error():
    with pytest.raises(AttributeError):
        get_student_by_tg_nickname("ivan_petrov", [1, 2])
