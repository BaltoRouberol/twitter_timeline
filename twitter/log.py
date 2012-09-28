"""
Logging logic.
"""

import logging

from os.path import join, dirname


def file_console_log():
    """ Return a logger handling two different streams:
        * a file in which all events with level >= INFO
          are displayed.
        * the console stdout stream, in which all events
          are displayed.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)  # redirect all events to handlers

    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # File handler: only display events with level >= INFO
    log_path = join(dirname(__file__), '..', 'scripts', 'retrieve_tweets.log')
    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(logging.INFO)  # debug messages will not be logged
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Stream handler: display all events
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)  # debug messages will de displayed
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger
