import requests
import os
import json
import pandas as pd
import datetime
import dateutil.parser
import unicodedata
import time
import tweepy
import csv


from secret import consumerkey
from secret import consumersecret
from secret import accesstoken
from secret import accesstokensecret

Class TwitterData():
    def __init__(self,stock):
        self.stock = stock
        data_set = tweets_df(results)
        auth = tweepy.OAuthHandler(consumerkey, consumersecret)
        auth.set_access_token(accesstoken, accesstokensecret)
        api = tweepy.API(auth)
        self.results = []
        for tweet in tweepy.Cursor(api.search, q=f'{self.stock} -filter:retweets min_faves:1', lang='en',
                                   wait_on_rate_limit=True).items(5000):
            if tweet.user.followers_count > 25:
                self.results.append(tweet)

    def tweets_df(self):
        id_list = [tweet.id for tweet in self.results]
        data_set = pd.DataFrame(id_list, columns=["id"])
        data_set["text"] = [tweet.text for tweet in self.results]
        data_set["Hashtags"] = [tweet.entities['hashtags'] for tweet in self.results]
        data_set["date"] = [tweet.created_at for tweet in self.results]
        data_set["follower_count"] = [tweet.user.followers_count for tweet in self.results]
        return data_set
