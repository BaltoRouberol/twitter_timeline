"""
Tests for the tweets retrieval suite.
"""

import unittest

import twitter
import db


class TwitterAPITest(unittest.TestCase):
    """ Tests ensuring that the Twitter API wrapper behaves correctly. """

    def test_api_connection(self):
        """ Test that the API can be reached and user is correclt autenticated.
        """
        api = twitter.login()
        self.assertEqual(api.me().name, "Balthazar Rouberol")

    def test_home_timeline(self):
        """ Test that the `twitter.API.home_timeline` returns the expected
            number of tweets.
        """
        timeline = twitter.home_timeline(count=2)
        self.assertEqual(len(timeline), 2)

    def test_tweet_structure(self):
        """ Test the structure of a tweet (stored as a Python dictionary).
            Ensure that all mandatory keys are presents.
        """
        tweet = twitter.home_timeline(count=1)[0]
        self.assertTrue("source" in tweet)
        self.assertNotEqual(tweet['source'], '')
        self.assertTrue("source_url" in tweet)
        self.assertNotEqual(tweet['source_url'], '')
        self.assertTrue("author" in tweet)
        self.assertNotEqual(tweet['author'], '')
        self.assertTrue("text" in tweet)
        self.assertNotEqual(tweet['text'], '')
        self.assertTrue("truncated" in tweet)
        self.assertTrue("hashtags" in tweet)
        self.assertTrue("_id" in tweet)
        assert tweet['_id'] is not None


class MongoTest(unittest.TestCase):
    """ Test suite ensuring all operations involving mongoDB are
        correctly executed.
    """

    def setUp(self):
        self.connection = db.connect()
        self.tweets_collection = db.twitter_collection('test_db', 'test_collection')

    def tearDown(self):
        self.connection.drop_database('test')

    def test_insertion_mongo(self):
        """ Tests that fetched tweets are correclty inserted in mongo. """
        timeline = twitter.home_timeline()
        for tweet in timeline:
            db.insert(tweet, self.tweets_collection)
        self.assertEqual(db.size(self.tweets_collection), len(timeline))

    def test_full_name(self):
        """ Tests that the `db.name` function returns {db_name}.{collection_name}."""
        self.assertEqual(db.name(self.tweets_collection), "test_db.test_collection")


if __name__ == '__main__':
    unittest.main()
