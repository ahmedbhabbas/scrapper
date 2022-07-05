import snscrape.modules.twitter as sntwitter
import pandas as pd
import snscrape.modules.twitter as sntwitter
query = "python"
tweets = []
limit = 10
xx = sntwitter.TwitterTweetScraper(10765432100123456789)
print(xx[0])
for tweet in sntwitter.TwitterSearchScraper(query).get_items():

      #print(vars(tweet))
      #break

    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)

# to save to csv
# df.to_csv('tweets.csv')