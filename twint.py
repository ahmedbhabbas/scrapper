tweets = []
# importing libraries and packages
import snscrape.modules.twitter as sntwitter
import pandas as pd
import json


def get_specific_tweet(tweet_id):
    print(tweet_id)
    tweets_list = []
    # Using TwitterSearchScraper to scrape data and append tweets to list

    for i, tweet in enumerate(sntwitter.TwitterTweetScraper(tweetId=tweet_id,
                                                            mode=sntwitter.TwitterTweetScraperMode.SINGLE).get_items()):
        print(tweet.content)
        tweets.append([tweet.date, tweet.user.username, tweet_id, tweet.content])
        return 0
tweet_ids=[1248823193869135872, 1248823194464575488,1248823196238970881]

for id in tweet_ids:


        try:

            get_specific_tweet(id)
        except:
             print('error')




df = pd.DataFrame(tweets, columns=['Date', 'User','Tweet_id', 'Tweet'])
print(df)
df.to_csv('e:/tweets.csv')
import pandas as pd
data = pd.read_csv('e:/tweets.csv')
data.head()
