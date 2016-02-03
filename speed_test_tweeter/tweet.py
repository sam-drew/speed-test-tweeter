import twitter

def writeTweet(accessToken, accessTokenSecret, consumerSecret, consumerKey, tweet):
    # Authorise this application.
    myAuth = twitter.OAuth(accessToken, accessTokenSecret, consumerSecret, consumerKey)
    twit = twitter.Twitter(auth = myAuth)
    twit.statuses.update(status = tweet)

if __name__ == "__main__":
    # Take input of all tokens/keys.
    accessToken = input("Enter the accessToken: ")
    accessTokenSecret = input("Enter the accessTokenSecret: ")
    consumerSecret = input("Enter the consumerSecret: ")
    consumerKey = input("Enter the consumerKey: ")
    # Take input of the desired tweet.
    tweet = input("What would you like to tweet? ")
    writeTweet(accessToken, accessTokenSecret, consumerSecret, consumerKey, tweet)
