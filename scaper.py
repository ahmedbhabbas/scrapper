# Imports
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Setting variables to be used below
maxTweets = 500

# Creating list to append tweet data to
tweets_list1 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:@Artemisness80').get_items()):
    if i>maxTweets:
        break
    tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
print(tweets_list1)
df = pd.DataFrame(tweets_list1, columns=['Date', 'ID','Tweet', 'user_name'])
print(df)
df.to_csv('e:/tweets_fake.csv')