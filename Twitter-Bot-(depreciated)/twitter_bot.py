import tweepy

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)





# import tweepy

# consumer_key= ''
# consumer_secret= ''
# access_token= ''
# access_token_secret= ''


# # Authenticate with Twitter
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)    

# # Create a Tweepy API object
# api = tweepy.API(auth, wait_on_rate_limit=True,
#                   )

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)