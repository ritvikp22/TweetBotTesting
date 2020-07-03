import tweepy

# API and Tokens from Twitter Developer
api_key = 'erTHMRjhyCS7Y9cori61BFgqp'
api_secret = 'DnlnPVULx4Z1Ph4LBJ6h33sjWgbOkGmkWyMScCRuasI7ny1yNR'
token_key = '1079439987395842049-pRZbnS4hCLJmrqHEKsmMlUpbnil9VB'
token_secret = 'UuOdtFSo4n40v1mdkWXMeb1EigQdVHeHg3kCwx67lZqJo'

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(token_key, token_secret)
api = tweepy.API(auth)

# Arbitrary username
test = api.get_user("elonmusk")

# Function to return n number of tweets from a specified user
def get_tweet(num_tweets):
    for status in tweepy.Cursor(api.user_timeline, screen_name="elonmusk", tweet_mode="extended").items(num_tweets):
        print(status.full_text)

#Running Function
get_tweet(10)