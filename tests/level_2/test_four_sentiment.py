import pytest
from functions.level_2.four_sentiment import check_tweet_sentiment

good_words = set(("милые", "пушистые", "красивые"))
bad_words = set(("противные", "вонючие", "мерзкие"))


@pytest.mark.parametrize(
    "text, good_words, bad_words, expected_result",
    [
        ("Просто нейтральный твит", good_words, bad_words, None),
        ("Скунсы красивые но вонючие", good_words, bad_words, None),
        ("Попугаи красивые и пушистые но иногда бывают мерзкие", good_words, bad_words, "GOOD"),
        ("Тараканы вообще не красивые они противные вонючие и мерзкие", good_words, bad_words, "BAD"),
    ],
)
def test__check_tweet_sentiment_different_cases(text, good_words, bad_words, expected_result):
    assert check_tweet_sentiment(text, good_words, bad_words) is expected_result


@pytest.mark.parametrize(
    "text, good_words, bad_words, expected_exception",
    [
        (12345, good_words, bad_words, AttributeError),
        ("Есть только противные слова", 123, bad_words, TypeError),
        ("Есть только милые слова", good_words, 456, TypeError),
    ],
)
def test__check_tweet_sentiment__exceptions(text, good_words, bad_words, expected_exception):
    with pytest.raises(expected_exception):
        check_tweet_sentiment(text, good_words, bad_words)
