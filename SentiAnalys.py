###Sentimental Analysis with Twitter
#-----Importing Libraries-----------`   `
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import csv
import textblob
from textblob import TextBlob
import sys
import re
import matplotlib.pyplot as plt


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
keyword = input("Enter your Search Keyword: ")
n_tweets = int(input('enter the number of tweets: '))

#----------------Defining function percentage------------
def percentage(part, whole):
    temp = 100*float(part) / float(whole)
    return format(temp, '.2f')

#----------sentiment variables-------------------
positive = 0
negative = 0
neutral = 0
polarity = 0

#-----------------Cursor Method to pull data out of twitter
tweets = tweepy.Cursor(api.search, q=keyword, lang ='en').items(n_tweets)

#---------Performing sentimental analysis over twitter data-----
for tweet in tweets:
    #print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(tweet.text)
    polarity += analysis.sentiment.polarity

    if(analysis.sentiment.polarity == 0):
        neutral += 1
    elif(analysis.sentiment.polarity < 0.00):
        negative += 1
    elif(analysis.sentiment.polarity > 0.00):
        positive += 1


#----------calculating sentiment percentages------------
positive = percentage(positive, n_tweets )
negative = percentage(negative, n_tweets )
neutral = percentage(neutral, n_tweets )

positive = format(float(positive), '.2f')
negative = format(float(negative), '.2f')
neutral = format(float(neutral), '.2f')

#----judging the sentiment---------------------
print('How people reacting on '+ keyword + ' by analizing '+ str(n_tweets) +' Tweets')
if(polarity == 0):
    print('Neutral')
elif(polarity < 0):
    print('Negative')
elif(polarity > 0):
    print('Positive')


#------------Output chart with Matplotlib------------------------
labels = ['Positve['+ str(positive)+ '%]', 'Neutral['+ str(neutral)+ '%]', 'negative['+ str(negative)+ '%]']
sizes = [positive, neutral, negative]
colors = ['yellowgreen', 'gold', 'red']
patches, texts = plt.pie(sizes, colors = colors, startangle=90)
plt.legend(patches, labels, loc='best')
plt.title('How people reacting on '+ keyword + ' by analyzing '+ str(n_tweets) +' Tweets')
plt.axis('equal')
plt.tight_layout()
plt.show()


"""
for tweet in tweets:
    tweet = tweet.split(',"text":"')[1].split('","source')[0]
print(tweet)
"""

"""
###Sentimental Analysis with Twitter

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import csv

#--------Authentication Variables-------------------
consumer_key = 'Kwz2vDa2ELvLE4PxlT1Fk46X1'
consumer_secret = 'wYc74pP03WKULBK7YoE0yuf2v5wACaWjXfVzFU338IpRY7GhpQ'
access_token = '1040115221770260481-Dkp5awYVXfidVwTGaMFCzG8cZA9R7T'
access_token_secret = 'cI9nwtql9au9QyWZPuDTruuM5WXVCsded5hnCcZbwR442'


#--------------Twitter Authentication------------------
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterStream = Stream(auth, listener())


keyword = []
keyword = [input('Enter your Search Keyword or Hashtag: ')]
twitterStream.filter(track=keyword, languages = ['en'])
api = tweepy.API(auth)





class listener(StreamListener):
    limit = int(input("Enter the Streaming time Limit: "))

    def __init__(self, time_limit = limit):
        self.start_time = time.time()
        self.limit = time_limit


    def on_data(self, data):
        try:
            with open('TwitterStream.csv', 'a') as file:
                file.write(data)
                return True
        except BaseException as e:
            print("Error on data: %s" %str(e))
        return True


    def on_error(self, status):
        print(status)
        return True

twitter_stream = stream(auth, listener())
twitter

"""
