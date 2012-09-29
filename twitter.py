"""
Module handling the communication with the Twitter API.
"""

import tweepy
import re

import config as cf


def login():
    """ Logs into the Twitter API using the user OAuth keys. """
    auth = tweepy.OAuthHandler(cf.CONSUMER_KEY, cf.CONSUMER_SECRET)
    auth.set_access_token(cf.ACCESS_TOKEN, cf.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    api.secure = True
    return api


def home_timeline(count=200):
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
    api = login()
    timeline = api.home_timeline(count=count)
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

