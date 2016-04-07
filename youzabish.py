import tweepy
import sys
import credentials


auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_secret)
api = tweepy.API(auth)

class CustomStreamListener(tweepy.StreamListener):
	def on_status(self, status):
		print status.text
	def on_data(self, data):
		try:
			mention = json.loads(data.strip())
			if mention['user']['screen_name'] != 'aibishtweets':
				print mention
				print 'mentioned: ' + mention['entities']['user_mentions'][0]['screen_name']
				print 'mentioned tweet ID: ' + mention.get('id_str')
				print 'mentioned by: ' + mention['user']['screen_name']
				tweetid = mention.get('id_str')
				mentionedby = '@' + mention['user']['screen_name']
			if mention['entities']['user_mentions'][0]['screen_name'] == 'aibishtweets' and mention['user']['screen_name'] != 'aibishtweets':
				api.update_with_media(status=mentionedby, filename="youzabish.gif", in_reply_to_status_id=tweetid)
		except:
			print "Unexpected error:", sys.exc_info()[0]
	def on_error(self, status_code):
		print >> sys.stderr, 'Encountered error with status code:', status_code
		return True # Don't kill the stream
	def on_timeout(self):
		print >> sys.stderr, 'Timeout...'
		return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(track=['aibishtweets'])