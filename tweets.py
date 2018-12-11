#-----Importing Libraries-----------
# coding = <utf-8>
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import csv
import json
import sys



######## twitter client #############
#--------Authentication Variables-------------------
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


#--------------Twitter Authentication------------------
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#-------------variable to store our key word-----------
csvFile = open('test.csv', 'a')
csvWriter = csv.writer(csvFile)
keyword = input("Enter your Search Keyword: ")
n_tweets = int(input('enter the number of tweets: '))
for tweet in tweepy.Cursor(api.search, q=keyword, lang ='en').items(n_tweets):
    csvWriter.writerow([tweet.text.encode('utf-8', 'ignore')])
csvFile.close()
#------------------Twitter Advanced Search------------
# coding = <utf-8>
Tweets containing all words in any position (“Twitter” and “search”)
Tweets containing exact phrases (“Twitter search”)
Tweets containing any of the words (“Twitter” or “search”)
Tweets excluding specific words (“Twitter” but not “search”)
Tweets with a specific hashtag (#twitter)
