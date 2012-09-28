#!/bin/bash

# Retrieve and store tweets from my twitter timeline by executing the ../twitter/retrieve.py
# python script.
# The command output is stored in the ./retrieve_tweets.log file
# WARNING: the mongoDB daemon (`mongod`) has to be running


ABSPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )" # absolute path of the directory containing this script
ROOT_DIR="$ABSPATH/../"  # directory containing the retrieval python script
BIN="$ROOT_DIR/bin"  # virtualenv bin folder
PYTHON="$BIN/python"  # virtualenv python binary


# activate virtualenv
source "$BIN"/activate

# execute retrieve.py script (retrieve and store new tweets)
cd "ROOT_DIR"
$PYTHON retrieve.py