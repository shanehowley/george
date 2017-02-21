import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter

CONSUMER_KEY = 'UhMYzaahXMWMgaKKp48SXzCTY'
CONSUMER_SECRET = 'Ncs34KGdQowzd2hvUlL0NBjx9p0V41JDdxUjHLNZomSrFB0Tlu'
OAUTH_TOKEN = '341704733-SXQeQtb3VC8Oy9iYrmCpl0ExAe7gdIQLYmggQ8Hv'
OAUTH_TOKEN_SECRET = 'vRBeS8IyEbG1IsjHiQNu3uqyNm4eJEQZe0c9LPbWvtO8u'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 150
query = 'Ireland'

results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

min_retweets = 10

pop_tweets = [status
              for status in results
              if status._json['retweet_count'] > min_retweets]


tweets_tup = tuple([(tweet._json['text'].encode('utf-8'), tweet._json['retweet_count']) for tweet in pop_tweets])

pop_tweets_set = set(tweets_tup)

sorted_tweets_tup = sorted(pop_tweets_set, key=itemgetter(1), reverse=True)[:5]

table = PrettyTable(field_names=['Text', 'Retweet Count'])
for key, val in sorted_tweets_tup:
    table.add_row([key, val])
table.max_width['Text'] = 50
table.align['Text'], table.align['Retweet Count'] = 'l', 'r' # align the columns
print table