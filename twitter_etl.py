import pandas as pd
import tweepy
import json
from datetime import datetime
import s3fs

access_key = "oR8uGA7oO2cHRM8OYhqBQANVm"
access_secret = "F7ds2KKlwy00Nn9gwYx5nXMYOvp9qfq7Gv6Ht8IpxZ0pMRNFeb"
consumer_key = "978844159-FacGvu290OWoheUTyBMwrsEbCRmJdR2xMX2GAsSf"
consumer_token = "4qlEzahh5CmOY4O1hos7GOg4cTwucT8gA0R1Oa6rnL53g"

#Twitter Authentication
auth = tweepy.OAuthHandler(access_key,access_secret)
auth.set_access_token(consumer_key,consumer_token)

#Creating API object
api = tweepy.API(auth)
tweets = api.user_timeline(screen_name='@elonmusk', 
                        # 200 is the maximum allowed count
                        count=10,
                        include_rts = False,
                        # Necessary to keep full_text 
                        # otherwise only the first 140 words are extracted
                        tweet_mode = 'extended'
                        )

list = []
for tweet in tweets:
    text = tweet._json["full_text"]

    refined_tweet = {"user": tweet.user.screen_name,
                    'text' : text,
                    'favorite_count' : tweet.favorite_count,
                    'retweet_count' : tweet.retweet_count,
                    'created_at' : tweet.created_at}
    
    list.append(refined_tweet)

df = pd.DataFrame(list)
df.to_csv('refined_tweets.csv')