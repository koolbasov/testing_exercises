import configparser
import pytest
from functions.level_4.five_extra_fields import fetch_extra_fields_configuration, fetch_app_config_field


@pytest.mark.parametrize(
    "config_file_path, expected_result",
    [
        ("config_file_path_extra_fields", "expected_extra_fields"),
        ("config_file_path_no_extra_fields", "empty_dict"),
        ("filepath_no_file", "empty_dict"),
    ],
)
def test__fetch_extra_fields_configuration__expected_behavior(config_file_path, expected_result, request):
    assert fetch_extra_fields_configuration(request.getfixturevalue(config_file_path)) == request.getfixturevalue(
        expected_result
    )


@pytest.mark.parametrize(
    "config_file_path, expected_exception",
    [
        ("filepath_three_lines_three_sharps", configparser.MissingSectionHeaderError),
        ("integer", TypeError),
    ],
)
def test__fetch_extra_fields_configuration__expected_exceptions(config_file_path, expected_exception, request):
    with pytest.raises(expected_exception):
        fetch_extra_fields_configuration(request.getfixturevalue(config_file_path))


@pytest.mark.parametrize(
    "config_file_path, field_name, expected_result",
    [
        ("config_file_path_extra_fields", "extra_fields", "expected_extra_fields_string"),
        ("config_file_path_no_extra_fields", "field_name", "return_none"),
    ],
)
def test__fetch_app_config_field__expected_behavior(config_file_path, field_name, expected_result, request):
    assert fetch_app_config_field(
        request.getfixturevalue(config_file_path), request.getfixturevalue(field_name)
    ) == request.getfixturevalue(expected_result)


@pytest.mark.parametrize(
    "config_file_path, field_name, expected_exception",
    [
        ("filepath_three_lines_three_sharps", "field_name", configparser.MissingSectionHeaderError),
        ("integer", "extra_fields", TypeError),
        ("config_file_path_extra_fields", "integer", AttributeError),
    ],
)
def test__fetch_app_config_field__test3(config_file_path, field_name, expected_exception, request):
    with pytest.raises(expected_exception):
        fetch_app_config_field(request.getfixturevalue(config_file_path), request.getfixturevalue(field_name))
