#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
 
#argfile = str(sys.argv[1])
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = '' #keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '' #keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '' #keep the quotes, replace this with your access token
ACCESS_SECRET = '' #keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#mentions = api.mentions_timeline(since_id='1',count=20)

#for mention in mentions:
#    print mention.text
#    print mention.user.screen_name


while 1:
    for mention in tweepy.Cursor(api.mentions_timeline).items():
        # process status here
        print mention.text
        print mention.user.screen_name
    time.sleep(10)   #Tweet every 15 minutes
