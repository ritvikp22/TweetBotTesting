import tweepy

# API and Tokens from Twitter Developer
api_key = ''
api_secret = ''
token_key = ''
token_secret = ''

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(token_key, token_secret)
api = tweepy.API(auth)

#Tweets the user input and likes it depending on the user's choice
def create_tweet(user_input):
    tweet = api.update_status(user_input)
    print("Tweet complete")
    choice = input("Wold you like to heart your tweet? ")
    if(choice.lower() == "yes"):
        api.create_favorite(tweet.id)
        print("Liked!")


tweet_info = input("What would you like to tweet? : ")

#Prints all of user tweets and allows deletion
def delete_tweet(num_tweets):
    tweets = []
    for status in tweepy.Cursor(api.home_timeline, tweet_mode="extended").items(num_tweets):
        tweets.append(status)
        for tweet in tweets:
            index = input("Which tweet would you like to delete: ")
            api.destroy_status(tweet[index].id)

tweetNum = 10
delete_tweet(tweetNum)
