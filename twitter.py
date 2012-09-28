"""
Module handling the communication with the Twitter API.
"""

import tweepy
import re

import config as cf


class API(object):
    """ A wrapper around the tweepy Twitter API, allowing to pull certain
        information from the tweets coming from the user home timeline.
    """
    def __init__(self):
        self.consumer_key = cf.CONSUMER_KEY
        self.consumer_secret = cf.CONSUMER_SECRET
        self.access_token = cf.ACCESS_TOKEN
        self.access_token_secret = cf.ACCESS_TOKEN_SECRET
        self.api = self.login()
        self.api.secure = True

    def login(self):
        """ Logs into the Twitter API using the user OAuth keys. """
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        return tweepy.API(auth)

    def home_timeline(self, count=200):
        """ Returns a list of the last tweets found in the user home timeline.
            Each tweet will be stored as a dictionary, with the following structure:
                    'source': # source of the tweet
                    'source_url': # url of the source
                    'author': # screen name of the author
                    'text':  # text of the tweet
                    'truncated': # boolean, has the tweet been truncated?
                    'hashtags': # a list of hashtags extracted from the text
                    'created_at': # date and hour of the creation of the tweet
                    '_id': id of the tweet
                }
        """
        timeline = self.api.home_timeline(count=count)
        tweets = []
        for status in timeline:
            # hashtags : '#' followed by a string with no whitespace
            # It can be found after a \s character or at the beginning of a line
            # '#hashtag it is'        # should match => ["hashtag"]
            # 'this is a #hashtag'    # should match => ["hashtag"]
            # 'this is not a#hashtag' # should not match => []
            hashtags = re.findall(r'(?:\A|\s)#(\w+)', status.text)
            tweets.append(
                {
                    'source': status.source,
                    'source_url': status.source_url,
                    'author': status.author.screen_name,
                    'text': status.text,
                    'truncated': status.truncated,
                    'hashtags': hashtags,
                    'created_at': status.created_at,
                    '_id': status.id,
                })
        return tweets


def checks():
    """ Check if the API is working properly by testing the name
        of the user, and printing a couple of exctracted tweets.
    """
    # Initialize API
    twitter = API()

    # check if API is correclt working
    assert twitter.api.me().name == "Balthazar Rouberol"

    # print a couple of tweets
    import pprint
    pprint.pprint(twitter.home_timeline(count=2))

if __name__ == '__main__':
    checks()
