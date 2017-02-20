import json
import tweepy
from tweepy import OAuthHandler


CONSUMER_KEY = 'UhMYzaahXMWMgaKKp48SXzCTY'
CONSUMER_SECRET = 'Ncs34KGdQowzd2hvUlL0NBjx9p0V41JDdxUjHLNZomSrFB0Tlu'
OAUTH_TOKEN = '341704733-SXQeQtb3VC8Oy9iYrmCpl0ExAe7gdIQLYmggQ8Hv'
OAUTH_TOKEN_SECRET = 'vRBeS8IyEbG1IsjHiQNu3uqyNm4eJEQZe0c9LPbWvtO8u'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 10
query = 'bosco ireland'


results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

for result in results:
    print json.dumps(result._json, indent=2)