#!/bin/bash

ABSPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )" # absolute path of the directory containing this script
BACKUP="$ABSPATH/backup"

# create directory ../backup/$CURRENTDATE with date of format YYYY-MM-DD
CURRENTDATE=`date +%F-%R`
mkdir -p "$BACKUP/$CURRENTDATE"
if [ $? -eq 0 ]; then
  mongodump --db twitter_nlp --collection home_timeline --out - | tail -n+2 > "$BACKUP/$CURRENTDATE/home_timeline.bson" 
fi
