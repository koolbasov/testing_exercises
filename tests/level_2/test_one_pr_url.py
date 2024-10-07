import pytest
from functions.level_2.one_pr_url import is_github_pull_request_url


def test__is_github_pull_request_url__correct_url_pr():
    url = "https://github.com/learnpythonru/testing_exercises/pull/40"

    pull_request_url = is_github_pull_request_url(url)

    assert pull_request_url is True


def test__is_github_pull_request_url__correct_url_not_pr():
    url = "https://github.com/learnpythonru/testing_exercises"

    pull_request_url = is_github_pull_request_url(url)

    assert pull_request_url is False


def test__is_github_pull_request_url__incorrect_url():
    url = "https://gitpub.com/learnpythonru/testing_exercises"

    pull_request_url = is_github_pull_request_url(url)

    assert pull_request_url is False


def test__is_github_pull_request_url__not_url():
    url = "testing_exercises"

    pull_request_url = is_github_pull_request_url(url)

    assert pull_request_url is False


def test__is_github_pull_request_url__not_string():
    url = 12345

    with pytest.raises(AttributeError):
        is_github_pull_request_url(url)
