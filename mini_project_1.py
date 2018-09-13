#Copyright Emily Stern, emistern@bu.edu

#This script will download images from a given twitter handle 
#and then create a video made up of all of the images.
#It will then use googles video cloud thing to give a 
#tag to each image.


#Import tweepy libraries need to interface with twitter API 
import tweepy

#Read in the consumer key, consumer secrete, acces token, 
#and secret access token from the file twitter_keys.txt
my_file = open('twitter_keys.txt', 'r')
my_keys = my_file.read().split('-')

#File is in this order:
consumer_key = my_keys[0]
consumer_secret = my_keys[1]
access_token = my_keys[2]
access_secret = my_keys[3]




# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text