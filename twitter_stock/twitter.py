import requests
import os
import json
import pandas as pd
import csv
import datetime
import dateutil.parser
import unicodedata
import time
import tweepy
import csv
import tweepy

Class TwitterData():
    def __init__(self,stock):
        self.stock = stock
    def getdata():
        auth = tweepy.auth.OAuthHandler('XXXXXX', 'XXXXXXX')
        auth.set_access_token('XXX-XXX', 'XXX')

    api = tweepy.API(auth)
    for tweet in tweepy.Cursor(api.search,
                               q="google",
                               since="2014-02-14",
                               until="2014-02-15",
                               lang="en").items():
        print tweet.created_at, tweet.text

