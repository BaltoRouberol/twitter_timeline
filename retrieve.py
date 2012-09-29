"""
Retrieve and store all new tweets from the user home timeline.
"""
import traceback

import db
import log
import twitter


def main():
    """ Retrieve and store all new tweets from the user home timeline.
    """
    # Logger
    logger = log.file_console_log()

    # Connect to the MongoDB database
    stored_tweets = db.twitter_collection()

    # Retrieve tweets from user timeline and store new ones in database
    # If any error occurs, log it in log file
    try:
        timeline_tweets = twitter.home_timeline()
    except Exception, error:
        logger.error(traceback.format_exc()[:-1])  # log error
        raise error
    else:
        before = db.size(stored_tweets)  # initial collection size
        # Insert each tweet in database
        # If any error occurs, log it in log file
        for tweet in timeline_tweets:
            try:
                db.insert(tweet, stored_tweets)  # insert in mongoDB collection
                # Note: if tweet already in DB, the insertion will fail silently
            except db.DBError, error:
                logger.error(traceback.format_exc()[:-1])  # log error
                raise error

        after = db.size(stored_tweets)  # new collection size

        # log insertion information
        message = "[%s] +%d new, %d stored" % (db.name(stored_tweets),
                                                after - before,
                                                after)
        logger.info(message)


if __name__ == '__main__':
    main()
