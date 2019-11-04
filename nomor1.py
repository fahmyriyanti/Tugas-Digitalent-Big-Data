import tweepy
from tweepy import OAuthHandler, Stream, StreamListener
import datetime
consumer_key = "tntJNfRejksUyXRDDHlTr0clH"
consumer_secret = "RbLkZlWfxC9Jdpx85U6MY4UjBEzbPGBkHwOj0YJ6db0XtwiUhl"
access_token = "1017256700695404544-Np2aKaVJgmZxWbyevaKdweEG3m5dJI"
access_token_secret = "BU4dJMQhRIbpPbMMlhw1h6ePSO9MhULP2YPH1p1z6ZH50"
auth = OAuthHandler(consumer_key, consumer_secret,)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
the_list = []
tweet_blackpink = api.user_timeline(screen_name = 'ygofficialblink', count = 200, tweet_mode = "extended")
start_date = datetime.datetime(2019, 10, 22, 00, 00, 00)
end_date = datetime.datetime(2019, 10, 23, 23, 59, 59)
for tweet in tweet_blackpink:
    if tweet.created_at < end_date and tweet.created_at > start_date:
        the_list.append(tweet)
import pandas
myData = pandas.DataFrame(the_list)
myData