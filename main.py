from twitterAnalyzer import Twitter, SentimentAnalyzer

def main():
	cleanedTweets = []
	twitter = Twitter()
	twitterFeed = twitter.get_tweets(query='#InnovationKiBaatPMKeSaath', count=100, lang='en', )

	if twitterFeed:
		cleanedTweets = twitter.clean_tweets(twitterFeed)

	tweetAnalyzer = SentimentAnalyzer()
	analysis = tweetAnalyzer.analyze(cleanedTweets)
	sentiment = {
		'positive': 0,
		'neutral': 0,
		'negative': 0,
	}

	for each in analysis:
		sentiment[each[1]] += 1
		print each

	print "\nPositive : %s \nNegative : %s \nNeutral: %s" % (sentiment['positive'], sentiment['negative'], sentiment['neutral'])


if __name__ == '__main__':
	main()


