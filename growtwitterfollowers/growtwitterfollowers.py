import tweepy
import time
import random

api_key = "<ADD IT HERE>"
api_secret = "<ADD IT HERE>"
bearer_token = "<ADD IT HERE>"
access_token = "<ADD IT HERE>"
access_token_secret = "<ADD IT HERE>"


# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)

api = tweepy.API(auth)

# Bot searches for tweets containing certain keywords
class MyStream(tweepy.StreamingClient):

    # This function gets called when a tweet passes the stream
    def on_tweet(self, tweet):

        #Liking the tweet
        try:
            client.like(tweet.id)
            print(tweet.text)

        except Exception as error:
            print(error)
        
        # delay between tweets
        sleepTime = random.randint(20,70)
        print("Sleep for", sleepTime, "seconds")
        time.sleep(sleepTime)

# Creating Stream object
stream = MyStream(bearer_token=bearer_token)

#Deleting terms to search rules
# stream.delete_rules(ids = 1556327631053721601)
# rules = stream.get_rules()
# print(rules)

# Adding rules - Eric
stream.add_rules(tweepy.StreamRule("(bio:nft bio:crypto lang:en followers_count:100..1000) (-is:retweet -is:reply)"))

# Adding rules - wwt
# stream.add_rules(tweepy.StreamRule("(bio:web3 lang:en followers_count:100..1000) (-is:retweet -is:reply)"))

# stream.add_rules(tweepy.StreamRule("(#Python OR #programming) (-is:retweet -is:reply)"))
# print("completed add rules")

# Starting stream
stream.filter()
print('completed filter')
