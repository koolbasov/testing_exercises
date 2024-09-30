import pytest
from functions.level_2.four_sentiment import check_tweet_sentiment

good_words = set(("милые", "пушистые", "красивые"))
bad_words = set(("противные", "вонючие", "мерзкие"))


def test__check_tweet_sentiment__neutral_tweet():
    text = "Просто нейтральный твит"

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result is None


def test__check_tweet_sentiment__good_words_equal_bad_words():
    text = "Скунсы красивые но вонючие"

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result is None


def test__check_tweet_sentiment__good_words_more_than_bad_words():
    text = "Попугаи красивые и пушистые но иногда бывают мерзкие"

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == "GOOD"


def test__check_tweet_sentiment__good_words_less_than_bad_words():
    text = "Тараканы вообще не красивые они противные вонючие и мерзкие"

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == "BAD"


def test__check_tweet_sentiment__no_text_but_integer():
    text = 12345

    with pytest.raises(AttributeError):
        check_tweet_sentiment(text, good_words, bad_words)


def test__check_tweet_sentiment__no_good_words_to_compare_but_integer():
    text = "Есть только противные слова"
    good_words = 123

    with pytest.raises(TypeError):
        check_tweet_sentiment(text, good_words, bad_words)
