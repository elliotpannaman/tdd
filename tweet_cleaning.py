import re

class Tweet(object):

    def __init__(self, tweet=""):
        self.text = tweet
        
    def set_tweet(self, text):
        self.text = text

    def clean_mentions(self, clean_out="@[a-zA-Z]{,}"):
        return re.sub(clean_out, "", self.text)
    
    def detect_retweet(self, retweet_txt="RE:"):
        return self.text.startswith("RT:")
    
    def clean_nonalphanumeric(self, alphanum="[^a-zA-Z0-9]"):
        return re.sub(alphanum, "", self.text)
    
    def clean_rude_words(self, rude_wds=["fuck", "shit"]):
        return re.sub('|'.join(rude_wds), "", self.text)
    
    def detect_empty_tweet(self):
        return self.text == ""