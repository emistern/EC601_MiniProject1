#Copyright Emily Stern, emistern@bu.edu

#This script will download images from a given twitter handle 
#and then create a video made up of all of the images.
#It will then use googles video cloud thing to give a 
#tag to each image.

import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'YOUR-CONSUMER-KEY'
consumer_secret = 'YOUR-CONSUMER-SECRET'
access_token = 'YOUR-ACCESS-TOKEN'
access_secret = 'YOUR-ACCESS-SECRET'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)