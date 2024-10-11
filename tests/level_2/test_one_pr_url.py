import pytest
from functions.level_2.one_pr_url import is_github_pull_request_url


@pytest.mark.parametrize(
    "url, expected_result",
    [
        ("https://github.com/learnpythonru/testing_exercises/pull/40", True),
        ("https://github.com/learnpythonru/testing_exercises", False),
        ("https://gitpub.com/learnpythonru/testing_exercises", False),
        ("testing_exercises", False),
    ],
)
def test__is_github_pull_request_url(url, expected_result):
    assert is_github_pull_request_url(url) is expected_result


def test__is_github_pull_request_url__not_string():
    url = 12345

    with pytest.raises(AttributeError):
        is_github_pull_request_url(url)
