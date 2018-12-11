# -*- coding: utf-8 -*-
import config
import tweepy
import os

# API Authentication
auth = tweepy.OAuthHandler(config['QIqgjITOfksfMW4lRLDacQ'], config['R8x0xN9iSKXGNxUtGKA2hgnlIhh5INZIOdgEfxzk'])
auth.set_access_token(config['1401204486-BeLUAuruh294KeJX8NXvdqjCeZOQcLl6HWmMlgA'], config['pwjiLF42TbORaXtkCS5Oc24qywOU0eFN0esVcibA'])
api = tweepy.API(auth)

# Fetch tweets by username
def getTweets(username, count=10):
    timeline = api.user_timeline(username, count=count)
    tweets = [tweet.text.encode('utf-8').translate(None, '!.,?') for tweet in timeline]
    return tweets

# Remove hashtags, mentions, links
def cleanTweets(tweets):
	clean_data = []
	for tweet in tweets:
	    item = ' '.join(word.lower() for word in tweet.split() \
	    	if not word.startswith('#') and \
	    	   not word.startswith('@') and \
	    	   not word.startswith('http') and \
	    	   not word.startswith('RT'))
	    if item == "" or item == "RT":
	        continue
	    clean_data.append(item)
	return clean_data

def getTrainData():
	positives, negatives, traindata = [], [], []
	for filename in os.listdir("train"):
	    if filename == "positives.txt":
		    with open('train/'+filename) as f:
			    positives = [(tweet, 'pos') for tweet in f.readlines()]
	    if filename == "negatives.txt":
		    with open('train/'+filename) as f:
			    negatives = [(tweet, 'neg') for tweet in f.readlines()]

	for (words, sentiment) in negatives + positives:
		words_filtered = [e for e in words.split() if len(e) > 2]
		traindata.append((words_filtered, sentiment))

	return traindata

def export(filename, data, p):
    with open(filename, p) as output:
    	for line in data:
        	output.write(line)
