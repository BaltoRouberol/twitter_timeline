## Retrieve tweets from your home timeline
Regularly fetch tweets from
your twitter timeline, using the [GET statuses/home_timeline](https://dev.twitter.com/docs/api/1.1/get/statuses/home_timeline)
API and store them in a mongoDB database.

### Important
Before running the `retrieve.py` script, you need to create a twitter app at [https://dev.twitter.com/apps](https://dev.twitter.com/apps)
to obtain OAuth credentials, and you need to add a `config.py` in this directory, defining the following constants:
```python
# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
CONSUMER_KEY = ""
CONSUMER_SECRET = ""

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""


# == mongoDB ==
HOST = ""  # default 'localhost'
PORT =  # default 27017
TW_DB_NAME = ""  
TW_COLLECTION_NAME = ""
```

### Tweet structure
Each tweet will be stored in database with the following structure:

* `'source'`: # source of the tweet
* `'source_url'`: # url of the source
* `'author'`: # screen name of the author
* `'text'`:  # text of the tweet
* `'truncated'`: # boolean, has the tweet been truncated?
* `'hashtags'`: # a list of hashtags extracted from the text
* `'created_at'`: # date and hour of the creation of the tweet
* `'_id'`: id of the tweet. **The valude of the id is the one used by Twitter, so you can retrieve it in their database too.**


### Read the code
To ensure readability, we divided the logic of the operation between several scripts:

* `twitter.py`: Interaction with the twitter API.
* `db.py`: Interaction with the [mongoDB](http://www.mongodb.org/) database. Change it if you wish to use another database. 
* `log.py` Configuration of the logger.
* `retrieve.py` Main script patching-up all the retrieval and DB-storage operations.
    Execute it with the command
    ```bash
    $ python retrieve.py
    ```
