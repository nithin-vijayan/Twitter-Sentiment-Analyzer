from twython import Twython
from decouple import config
from textblob import TextBlob
from twython.exceptions import TwythonAuthError

class Twitter(object):
	def __init__(self):
		TWITTER_APP_KEY = config('TWITTER_APP_KEY')
		TWITTER_APP_KEY_SECRET = config('TWITTER_APP_KEY_SECRET')
		TWITTER_ACCESS_TOKEN = config('TWITTER_ACCESS_TOKEN')
		TWITTER_ACCESS_TOKEN_SECRET = config('TWITTER_ACCESS_TOKEN_SECRET')

		self.api = Twython(TWITTER_APP_KEY, TWITTER_APP_KEY_SECRET,
                  TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
		try:
			self.api.verify_credentials()
		except TwythonAuthError:
			print "Authentication with the api failed"

	def get_tweets(self, query, count, lang):
		twitterFeed = {}
		try:
			twitterFeed = self.api.search(q=query+" -filter:retweets", lang=lang, count=count, ) #Filter out retweets and query for the new feeds
		except TwythonAuthError:
			print "Authentication with the api failed"
		return twitterFeed

	def clean_tweets(self, twitterFeed):		
		tweetsRaw = twitterFeed["statuses"]
		tweets = []
		for eachTweet in tweetsRaw:
			if not eachTweet["retweeted"] and ('RT @' not in eachTweet["text"]): #Filter any retweets, if any ,which still managed to show up
				tweets.append(eachTweet["text"])
		return tweets

class SentimentAnalyzer(object):
	def __init__(self):
		pass

	def analyze(self, cleanedTweets):
		analyzedTweets = []
		for tweets in cleanedTweets:
			analysis = TextBlob(tweets)
			polarity = analysis.sentiment.polarity
			if polarity>0:
				sentiment = 'positive'
			elif polarity==0:
				sentiment = 'neutral'
			else:
				sentiment = 'negative'
			analyzedTweets.append((tweets, sentiment))
		return analyzedTweets

