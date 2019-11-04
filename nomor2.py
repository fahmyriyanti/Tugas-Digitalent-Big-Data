# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 10:40:05 2019

@author: Andi Sitti Fahmi
"""

import tweepy
import csv
from tweepy import OAuthHandler, Stream, StreamListener
consumer_key = "tntJNfRejksUyXRDDHlTr0clH"
consumer_secret = "RbLkZlWfxC9Jdpx85U6MY4UjBEzbPGBkHwOj0YJ6db0XtwiUhl"
access_token = "1017256700695404544-Np2aKaVJgmZxWbyevaKdweEG3m5dJI"
access_token_secret = "BU4dJMQhRIbpPbMMlhw1h6ePSO9MhULP2YPH1p1z6ZH50"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret,)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
csvfile = open('file.csv','a')
csvWriter = csv.writer(csvfile)
for tweet in tweepy.Cursor(api.search,q="#PasukanRebahan", lang = "en", count=20).items():
    print(tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])