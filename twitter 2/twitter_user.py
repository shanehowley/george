import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = 'UhMYzaahXMWMgaKKp48SXzCTY'
CONSUMER_SECRET = 'Ncs34KGdQowzd2hvUlL0NBjx9p0V41JDdxUjHLNZomSrFB0Tlu'
OAUTH_TOKEN = '341704733-SXQeQtb3VC8Oy9iYrmCpl0ExAe7gdIQLYmggQ8Hv'
OAUTH_TOKEN_SECRET = 'vRBeS8IyEbG1IsjHiQNu3uqyNm4eJEQZe0c9LPbWvtO8u'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

user = api.get_user('@madonna')

for status in tweepy.Cursor(api.home_timeline).items(10):
    print status.text


# print user.screen_name
# print user.followers_count

# for friend in user.friends():
#     print
#     print friend.screen_name
#     print friend.followers_count

