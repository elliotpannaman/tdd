import pytest
from tweet_cleaning import Tweet

@pytest.fixture
def dirty_tweets():
    """
    Tweets with problems that need to be cleaned:
        - Delete mentions --> @xxxx
        - Detect retweets --> Starting with "RT:"
        - Clean all non-alphanumeric characters
        - Detect rude words
        - Detect empty tweets --> Might happen after cleaning
    """
    
    problematic_tweets = ["Hello @Somebody",
                          "RT: Now you're just @Somebody that I used to know",
                          "あなたは私が知っていた誰かです",
                          "fuck them, they think they know that shit bro.",
                          ""]

    return problematic_tweets

@pytest.fixture
def tweet_gen():
    '''Generates an empty tweet object'''
    return Tweet()

def test_mentions_gone(tweet_gen, dirty_tweets):
    tweet_gen.set_tweet(dirty_tweets[0])
    assert tweet_gen.clean_mentions() == "Hello "
    
def test_detect_rt(tweet_gen, dirty_tweets):
    tweet_gen.set_tweet(dirty_tweets[1])
    assert tweet_gen.detect_retweet()

def test_nonalphanumeric_gone(tweet_gen, dirty_tweets):
    tweet_gen.set_tweet(dirty_tweets[2])
    assert tweet_gen.clean_nonalphanumeric() == ""

def test_rude_words_gone(tweet_gen, dirty_tweets):
    tweet_gen.set_tweet(dirty_tweets[3])
    assert tweet_gen.clean_rude_words() == " them, they think they know that  bro."
    
def test_detect_empty_tweets(tweet_gen, dirty_tweets):
    tweet_gen.set_tweet(dirty_tweets[4])
    assert tweet_gen.detect_empty_tweet()