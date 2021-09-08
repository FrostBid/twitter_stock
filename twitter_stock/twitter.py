import tweepy
from tqdm import tqdm
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

from sentinment_analysis import sa
from secret import *


class TwitterData():
    def __init__(self,stock):
        self.stock = stock
        auth = tweepy.OAuthHandler(consumerkey, consumersecret)
        auth.set_access_token(accesstoken, accesstokensecret)
        api = tweepy.API(auth)
        self.results = []
        print('Twitter authentication successful, fetching tweets...')
        for tweet in tqdm(tweepy.Cursor(api.search, q=f'{self.stock} -filter:retweets min_faves:1', tweet_mode='extended', lang='en',
                                   wait_on_rate_limit=True, wait_on_rate_limit_notify=True).items(2500), total=2500):
          tweet.text = str(tweet.full_text.lower())
          # Filter out spam and tweets from small twitter accounts
          if tweet.user.followers_count > 25 and tweet.text.count('$') <= 5:
              self.results.append(tweet)

        self.tweets_df()
        print('Tweets collected.')

    def tweets_df(self):
        id_list = [tweet.id for tweet in self.results]
        self.data_set = pd.DataFrame(id_list, columns=["id"])
        self.data_set["username"] = [tweet.user.screen_name for tweet in self.results]
        self.data_set["text"] = [tweet.text for tweet in self.results]
        self.data_set["date"] = [tweet.created_at for tweet in self.results]
        self.data_set["follower_count"] = [tweet.user.followers_count for tweet in self.results]

        # Data cleaning (Remove links, twitter handles and extra spaces)
        self.data_set['text'] = self.data_set['text'].str.replace('http\S+|www.\S+', '', regex=True)
        self.data_set['text'] = np.vectorize(self.remove_pattern)(self.data_set['text'], "@[\w]*")
        self.data_set['text'] = self.data_set['text'].str.replace(r'\n', ' ', regex=True)
        self.data_set['text'] = self.data_set['text'].str.encode('ascii', errors='ignore')
        self.data_set['text'] = self.data_set['text'].str.decode("utf-8")
        sa(self.data_set)
        return self.data_set

    def remove_pattern(self, input_txt, pattern):
      r = re.findall(pattern, input_txt)
      for i in r:
        input_txt = re.sub(i, '', input_txt)
      return input_txt

    def csv(self):
        # Export to csv
        self.data_set.to_csv(f'{self.stock}_tweets.csv')
        return self.data_set

    def wordcloud(self):
        # Generate a wordcloud
        all_words = ' '.join([text for text in self.data_set['text']])
        wordcloud = WordCloud(width=800, height=500, random_state=21, background_color='white',
                              max_font_size=110).generate(all_words)
        plt.figure(figsize=(10, 7))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()
        plt.savefig(f'{self.stock} wordcloud.png')
