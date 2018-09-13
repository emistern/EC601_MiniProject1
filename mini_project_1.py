#Copyright Emily Stern, emistern@bu.edu

#This script will download images from a given twitter handle 
#and then create a video made up of all of the images.
#It will then use googles video cloud thing to give a 
#tag to each image.


#Import tweepy libraries need to interface with twitter API 
import tweepy
from tweepy import OAuthHandler

#Import the twitter credentials
import twitter_credentials

#Authorize with the twitter keys/tokens
auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#Verifies that you can reach twitter
try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print('Error! Failed to get request token.')

new_tweets = api.user_timeline(screen_name = "FRCTeams",count=200)
for tweet in new_tweets:
	print(tweet)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet)