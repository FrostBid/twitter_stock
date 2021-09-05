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

    def gettweets(self):
        auth = tweepy.auth.OAuthHandler(consumerkey, consumersecret)
        auth.set_access_token(accesstoken, accesstokensecret)
        api = tweepy.API(auth, wait_on_rate_limit = True)

        tweetlist = [tweets for tweets in tweepy.Cursor(api.search,
                                                          q=stocksymbol,
                                                          lang="en",
                                                          since_id=since_id_num2,
                                                          tweet_mode='extended').items(num_tweets2)]

        for tweet in tweet_list2[::-1]:
            tweet_id = tweet.id  # get Tweet ID result
            created_at = tweet.created_at  # get time tweet was created
            text = tweet.full_text  # retrieve full tweet text
            with open('stockdata', 'a', newline='', encoding='utf-8') as csvFile2:
                csv_writer2 = csv.writer(csvFile2, delimiter=',')  # create an instance of csv object
                csv_writer2.writerow([tweet_id, created_at, text])  # write each row


        stocksymbol = "$TSLA"
        search_query2 = search_words2 + " -filter:links AND -filter:retweets AND -filter:replies"
        with open('stockdata.csv', encoding='utf-8') as data:
            latest_tweet = int(list(csv.reader(data))[-1][0])  # Return the most recent tweet ID

        return gettweets(search_query2, 10000, latest_tweet)
