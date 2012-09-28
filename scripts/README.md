### retrieve_tweets.sh
This bash script executes the `../retrieve.py` python script, 
which retrieves tweets from the user's timeline, and store them in
a database.


### backup.sh
This bash script creates a backup of the [mongoDB](http://www.mongodb.org/) database, and store it in a 
`./backup/$DATE-$HOUR` directory.


### Planned execution
These scripts are intended to be executed regularly, using `cron` (or equivalent).
I personally execute `retrieve_tweets.sh` hourly during a week, with the following `crontab` line (in `/etc/crontab`):

``` 
01 * 21-29 Sep * balto   bash $SCRIPTS/retrieve_tweets.sh 2>/dev/null
```
and `backup.sh` daily, with the following `crontab` line:

```
00 12 21-29 Sep * balto   bash $SCRIPTS/retrieve_tweets.sh 2>/dev/null
```

**Important**: If you're using [mongoDB](http://www.mongodb.org/), note that the `mongod` process has to be running for the scripts to succeed.