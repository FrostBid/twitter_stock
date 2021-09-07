import pandas as pd
import datetime
import dateutil.parser
import unicodedata
import time
import tweepy
import csv
import re
from tqdm import tqdm


from secret import consumerkey
from secret import consumersecret
from secret import accesstoken
from secret import accesstokensecret

class TwitterData():
    def __init__(self,stock):
        self.stock = stock
        auth = tweepy.OAuthHandler(consumerkey, consumersecret)
        auth.set_access_token(accesstoken, accesstokensecret)
        api = tweepy.API(auth)
        self.results = []
        print('Twitter authentication completed, fetching tweets...')
        for tweet in tqdm(tweepy.Cursor(api.search, q=f'{self.stock} -filter:retweets min_faves:1', lang='en',
                                   wait_on_rate_limit=True).items(5000), total=5000):
            if tweet.user.followers_count > 25:
                self.results.append(tweet)
        print('Tweets collected, exporting to CSV.')
        self.datacsv()

    def tweets_df(self):
        id_list = [tweet.id for tweet in self.results]
        self.data_set = pd.DataFrame(id_list, columns=["id"])
        self.data_set["text"] = [tweet.text for tweet in self.results]
        self.data_set["Hashtags"] = [tweet.entities['hashtags'] for tweet in self.results]
        self.data_set["date"] = [tweet.created_at for tweet in self.results]
        self.data_set["follower_count"] = [tweet.user.followers_count for tweet in self.results]
        return self.data_set

    def datacsv(self):
        self.tweets_df()
        self.data_set['text'] = self.data_set['text'].str.replace('http\S+|www.\S+', '', case=False)
        self.data_set['text'].replace({r'[^\x00-\x7F]+': ''}, regex=True, inplace=True)
        self.data_set["text"] = self.data_set["text"].apply(lambda x: ' '.join([w for w in x.split() if len(w) > 2]))
        # Export to csv
        self.data_set.to_csv('scraped_user_tweets.csv', index=False)
        return self.data_set
