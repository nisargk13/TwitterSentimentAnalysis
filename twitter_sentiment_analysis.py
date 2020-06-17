# -*- coding: utf-8 -*-
"""Twitter_Sentiment_Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xIti2k0gFWYCbeX_qkLO8otn1jDFQKUV
"""

import tweepy
import pandas as pd
import numpy as np
import re
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

# Load the data
from google.colab import files
uploaded = files.upload()

# Get the data
log = pd.read_csv("Login.csv")

# Twitter Api Credentials
consumerKey = "ADD YOURS CONSUMER KEY"
consumerSecret ="ADD YOURS CONSUMER SECRET"
accessToken = "ADD YOURS ACCESS TOKEN"
accessTokenSecret =  "ADD YOURS ACCESS TOKEN SECRET"

# Create the authentication object
authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret) 
    
# Set the access token and access token secret
authenticate.set_access_token(accessToken, accessTokenSecret) 
    
# Creating the API object while passing in auth information
api = tweepy.API(authenticate, wait_on_rate_limit = True)

# Extract 100 tweets from the twitter user
posts = api.user_timeline(screen_name="realDonaldTrump", count = 100, lang ="en", tweet_mode="extended")

#  Print the last 5 tweets
print("Show the 5 recent tweets:\n")
i=1
for tweet in posts[:5]:
    print(str(i) +') '+ tweet.full_text + '\n')
    i= i+1

#create dataframe 
df = pd.DataFrame([tweet.full_text for tweet in posts], columns=['Tweets'])
#show the first 5 data frame
df.head()

#clean data

#function for cleaning
def cleanText(text):
  text = re.sub(r'@[A-Za-z0-9]+','',text) #removed @
  text = re.sub(r'#','',text) #Removing #
  text = re.sub(r'RT[\s]+','',text)
  text = re.sub('https?:\/\/\S+', '', text) # Removing hyperlink
  return text

df['Tweets'] = df['Tweets'].apply(cleanText)

df

#create function to get subjectivity
def get_sub(text):
  return TextBlob(text).sentiment.subjectivity

#create function to get polarity
def get_polar(text):
    return TextBlob(text).sentiment.polarity

#create two new colums
df['Subjectivity'] = df['Tweets'].apply(get_sub)  
df['Polarity'] = df['Tweets'].apply(get_polar)

#show ne dataframe with two columns
df

#Plot Wordcloud
allwords = ''.join([twts for twts in df['Tweets']])
wordcloud = WordCloud(width=500, height=300, random_state=21, max_font_size=120).generate(allwords)

plt.imshow(wordcloud, interpolation= "bilinear")
plt.axis('off')
plt.show()

#create function for negative and positive analysis
def getAnalysis(score):
  if score <0:
    return 'Negative'
  elif score ==0:
    return 'Neutral'
  else:
    return 'Positive'

df['Analysis'] = df['Polarity'].apply(getAnalysis)

df

#Print Positive tweet
j = 1
sortedDf = df.sort_values(by = ['Polarity'])
for i in range(0, sortedDf.shape[0]):
  if (sortedDf['Analysis'][i] == 'Positive'):
      print(str(j) + ')'+sortedDf['Tweets'][i])
      print()
      j=j+1

#Print Negative tweets
j = 1
sortedDf = df.sort_values(by = ['Polarity'], ascending='False')
for i in range(0, sortedDf.shape[0]):
  if (sortedDf['Analysis'][i] == 'Negative'):
      print(str(j) + ')'+sortedDf['Tweets'][i])
      print()
      j=j+1

#plot polarity and subjectivity
plt.figure(figsize=(8,6))
for i in range (0, df.shape[0]):
  plt.scatter(df['Polarity'][i], df['Subjectivity'][i],color = 'Red')

plt.title('Sentiment Analysis')
plt.xlabel('Polarity')
plt.ylabel('Subjectivity')
plt.show()

#Percentage of Positive tweets
ptweets = df[df.Analysis == 'Positive']
ptweets = ptweets['Tweets']
round((ptweets.shape[0]/df.shape[0])*100,1)

#Percentage of Negative tweets
ntweets = df[df.Analysis == 'Negative']
ntweets = ntweets['Tweets']
round((ntweets.shape[0]/df.shape[0])*100,1)

#Percentage of Negative tweets
nttweets = df[df.Analysis == 'Neutral']
nttweets = nttweets['Tweets']
round((nttweets.shape[0]/df.shape[0])*100,1)

#Value Counts
df['Analysis'].value_counts()

plt.title('Sentiment Analysis')
plt.xlabel('Polarity')
plt.ylabel('Counts')
df['Analysis'].value_counts().plot(kind = 'bar')
plt.show()