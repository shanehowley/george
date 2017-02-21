import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable

CONSUMER_KEY = 'UhMYzaahXMWMgaKKp48SXzCTY'
CONSUMER_SECRET = 'Ncs34KGdQowzd2hvUlL0NBjx9p0V41JDdxUjHLNZomSrFB0Tlu'
OAUTH_TOKEN = '341704733-SXQeQtb3VC8Oy9iYrmCpl0ExAe7gdIQLYmggQ8Hv'
OAUTH_TOKEN_SECRET = 'vRBeS8IyEbG1IsjHiQNu3uqyNm4eJEQZe0c9LPbWvtO8u'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 50
query = 'Weather'

results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

status_texts = [status._json['text'] for status in results]

screen_names = [status._json['user']['screen_name']
                for status in results
                for mention in status._json['entities']['user_mentions']]

hashtags = [hashtag['text']
            for status in results
            for hashtag in status._json['entities']['hashtags']]

words = [w for t in status_texts
         for w in t.split()]

for label, data in (('Text', status_texts),
                    ('Screen Name', screen_names),
                    ('Word', words)):
    table = PrettyTable(field_names=[label, 'Count'])
    counter = Counter(data)
    [ table.add_row(entry) for entry in counter.most_common()[:10] ]
    table.align[label], table.align['Count'] = 'l', 'r' # align the columns
    print table

