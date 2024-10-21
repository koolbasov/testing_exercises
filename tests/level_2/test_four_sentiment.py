import pytest
from functions.level_2.four_sentiment import check_tweet_sentiment


@pytest.mark.parametrize(
    "text, expected_result",
    [
        ("Просто нейтральный твит", None),
        ("Скунсы красивые но вонючие", None),
        ("Попугаи красивые и пушистые но иногда бывают мерзкие", "GOOD"),
        ("Тараканы вообще не красивые они противные вонючие и мерзкие", "BAD"),
    ],
)
def test__check_tweet_sentiment_different_cases(text, good_words, bad_words, expected_result):
    assert check_tweet_sentiment(text, good_words, bad_words) is expected_result


def test__check_tweet_sentiment__fails_on_text(good_words, bad_words):
    with pytest.raises(AttributeError):
        check_tweet_sentiment(123, good_words, bad_words)


def test__check_tweet_sentiment__fails_on_good_words(good_words, bad_words):
    with pytest.raises(TypeError):
        check_tweet_sentiment("Просто текст", 123, bad_words)


def test__check_tweet_sentiment__fails_on_bad_words_words(good_words, bad_words):
    with pytest.raises(TypeError):
        check_tweet_sentiment("Просто текст", good_words, 345)
