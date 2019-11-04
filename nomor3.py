# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 10:32:15 2019

@author: Andi Sitti Fahmi
"""

import tweepy
consumer_key = "tntJNfRejksUyXRDDHlTr0clH"
consumer_secret = "RbLkZlWfxC9Jdpx85U6MY4UjBEzbPGBkHwOj0YJ6db0XtwiUhl"
access_token = "1017256700695404544-Np2aKaVJgmZxWbyevaKdweEG3m5dJI"
access_token_secret = "BU4dJMQhRIbpPbMMlhw1h6ePSO9MhULP2YPH1p1z6ZH50"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

hashtags = ["#got7","#kabinetbalasbudi","#jokowi","#vagabond","#minggu"]
for hashtag in hashtags:
    for tweet in tweepy.Cursor(api.search,q=hashtag, count=200, lang="id", since="2019-10-23", until="2019-10-24").items():
        print (tweet.created_at, tweet.text)
        