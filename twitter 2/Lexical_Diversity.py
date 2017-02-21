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
query = 'Dublin'

def search(query, count):
    return [status for status in tweepy.Cursor(api.search, q=query).items(count)]


def get_tweet_texts(tweets):
    return [status._json['text'].encode('utf-8') for status in tweets]


def get_screen_names(tweets):
    return [status._json['user']['screen_name'].encode('utf-8')
                for status in tweets
                for mention in status._json['entities']['user_mentions']]


def get_words(tweet_texts):
    return [word
        for tweet_text in tweet_texts
        for word in tweet_text.split()]

def get_hashtags(tweets):
    return [hashtag['text'].encode('utf-8')
        for status in tweets
        for hashtag in
        status._json['entities']['hashtags']]



results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]
print json.dumps(results[0]._json, indent=4)


def get_lexical_diversity(items):
    return 1.0 * len(set(items)) / len(items)


def get_average_words(tweets):
    total_words = sum([len(tweet.split()) for tweet in tweets])
    return 1.0 * total_words / len(tweets)


tweets = search('Dublin', 100)
texts = get_tweet_texts(tweets)
words = get_words(texts)
screen_names = get_screen_names(tweets)
hashtags = get_hashtags(tweets)



print "Average words: %s" % get_average_words(texts)
print "Word Diversity: %s" % get_lexical_diversity(words)
print "Screen Name Diversity: %s" % get_lexical_diversity(screen_names)
print "HashTag Diversity: %s" % get_lexical_diversity(hashtags)
