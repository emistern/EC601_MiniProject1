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

#Import wget and OS and io
import wget, os, io

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


#Authorize with the twitter keys/tokens
auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#Verifies that you can reach twitter
try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print('Error! Failed to get request token.')


#Check if username exists
valid_name = False
while valid_name == False:
	username = input("What username would you like to download images from? ")
	try:
	    u=api.get_user(username)
	    print (u.id_str)
	    print (u.screen_name)
	    break
	except Exception:
	    print("That was not a valid username")
	    continue

#Last 200 tweets from the given username
new_tweets = api.user_timeline(screen_name = username,count=0)

#Move all of the tweets with images to a new list.
tweets_with_pics = []
for tweet in new_tweets:
	#print(tweet)
	media = tweet.entities.get('media',[])
	if (len(media)>0):
		tweets_with_pics.append(media[0]['media_url'])

#Check if a directory for the pictures exists. If not, make one. 
try:
	os.mkdir('twitter_images')
	os.chdir('twitter_images')
except:
	os.chdir('twitter_images')

#Download all of the pictures to the directory twitter_images.
for pic_url in tweets_with_pics:
	wget.download(pic_url)

#Return back to the working directory
os.chdir("..")

#Convert images to video here

#Skip the images to video section for now. 
#Add the google vision api and checkout labels for each image to start.

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    './twitter_images/DlJrqiMWsAAcEvX.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)



