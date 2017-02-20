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

DUB_WOE_ID = 560743
LON_WOE_ID = 44418

dub_trends = api.trends_place(DUB_WOE_ID)
LON_TRENDS = api.trends_place(LON_WOE_ID)

print json.dumps(dub_trends, indent=1)
print json.dumps(lon_trends, indent=1)

