"""
Logic of the mongoDB interaction.
If you wish to use another databse, modify this file
and this file only.
"""

import pymongo

from pymongo.errors import PyMongoError

import config as cf


class DBError(PyMongoError):
    """ Base class for Database errors, inheriting from
        the base class for all pymongo errors.
    """


def connect(host=cf.HOST, port=cf.PORT):
    """ Connect to mongoDB using the parameters
        specified in the config.py module.
    """
    return pymongo.Connection(host, port)


def twitter_collection(db_name=cf.TW_DB_NAME, collection_name=cf.TW_COLLECTION_NAME):
    """ Return the twitter collection specified in the
        config.py module.
    """
    return connect()[db_name][collection_name]


def insert(item, collection):
    """ Insert the argument item in the argument mongoDB collection.
        If the item already is in the collection, the insertion will
        fail silently (default behaviour of mongoDB).
    """
    try:
        collection.insert(item)
    except PyMongoError, error:
        raise DBError(error)


def size(collection):
    """ Returns the size of the argument mongoDB collection. """
    return collection.find().count()


def name(collection):
    """ Returns the full name (db_name.collection_name) of a
        mongoDB collection.
    """
    return collection.full_name
