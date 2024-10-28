import configparser
import os
import pytest

from functions.level_4.two_students import Student


@pytest.fixture()
def student_1():
    return Student(first_name="Ivan", last_name="Petrov", telegram_account="@ivan_petrov")


@pytest.fixture()
def student_2():
    return Student(first_name="Petr", last_name="Ivanov", telegram_account="@petr_ivanov")


@pytest.fixture()
def student_3():
    return Student(first_name="Ivan", last_name="Ivanov", telegram_account="@ivan_ivanov")


@pytest.fixture()
def student_4():
    return Student(first_name="Petr", last_name="Petrov", telegram_account="@petr_petrov")


@pytest.fixture()
def student_5():
    return Student(first_name="Igor", last_name="Smirnov", telegram_account=None)


@pytest.fixture()
def list_of_students(student_1, student_2, student_3, student_4, student_5):
    return [student_1, student_2, student_3, student_4, student_5]


@pytest.fixture()
def return_none():
    return None


@pytest.fixture()
def empty_list():
    return []


@pytest.fixture()
def empty_dict():
    return {}


@pytest.fixture()
def empty_tuple():
    return ()


@pytest.fixture()
def integer():
    return 12345


@pytest.fixture()
def filepath_no_file():
    return "not_a_file"


@pytest.fixture()
def filepath_two_lines():
    path_to_file = os.path.join("tests", "level_4", "test_file.txt")
    with open(path_to_file, "w") as file_handler:
        file_handler.writelines(["1\n", "2\n"])

    yield path_to_file

    os.remove(path_to_file)


@pytest.fixture()
def filepath_three_lines_three_sharps():
    path_to_file = os.path.join("tests", "level_4", "test_file.txt")
    with open(path_to_file, "w") as file_handler:
        file_handler.writelines(["1\n", "#\n", "2\n", "#\n", "3\n", "#\n"])

    yield path_to_file

    os.remove(path_to_file)


@pytest.fixture()
def filepath_no_lines():
    path_to_file = os.path.join("tests", "level_4", "test_file.txt")
    with open(path_to_file, "w"):
        pass
    yield path_to_file

    os.remove(path_to_file)


@pytest.fixture()
def config_file_path_extra_fields():
    path_to_file = os.path.join("tests", "level_4", "config.ini")
    config = configparser.ConfigParser()
    config["DEFAULT"] = {"ServerAliveInterval": "45", "Compression": "yes", "CompressionLevel": "9"}
    config["tool:app-config"] = {}
    tool = config["tool:app-config"]
    tool["extra_fields"] = "field1: 42\nfield2: 'hello'\nfield3: [1, 2, 3]"
    with open(path_to_file, "w") as configfile:
        config.write(configfile)

    yield path_to_file

    os.remove(path_to_file)


@pytest.fixture()
def config_file_path_no_extra_fields():
    path_to_file = os.path.join("tests", "level_4", "config.ini")
    config = configparser.ConfigParser()
    config["DEFAULT"] = {"ServerAliveInterval": "45", "Compression": "yes", "CompressionLevel": "9"}
    with open(path_to_file, "w") as configfile:
        config.write(configfile)

    yield path_to_file

    os.remove(path_to_file)


@pytest.fixture()
def expected_extra_fields():
    return {"field1": 42, "field2": "hello", "field3": [1, 2, 3]}


@pytest.fixture()
def expected_extra_fields_string():
    return "field1: 42\nfield2: 'hello'\nfield3: [1, 2, 3]"


@pytest.fixture()
def extra_fields():
    return "extra_fields"
