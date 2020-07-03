import tweepy

# API and Tokens from Twitter Developer
api_key = ''
api_secret = ''
token_key = ''
token_secret = ''

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(token_key, token_secret)
api = tweepy.API(auth)

# Arbitrary username
test = api.get_user("elonmusk")

#Choose username
choice = input("Whose tweets would you like to see")

# Function to return n number of tweets from a specified user
def get_tweet(num_tweets):
    for status in tweepy.Cursor(api.user_timeline, screen_name= choice, tweet_mode="extended").items(num_tweets):
        print(status.full_text)

#Running Function
num = 10
get_tweet(num)