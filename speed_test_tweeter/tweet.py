import twitter

# Hard code all tokens / keys here.
accessToken = ""
accessTokenSecret = ""
consumerKey = ""
consumerSecret = ""

# Authorise this application, and 'test tweet'.
myAuth = twitter.OAuth(accessToken, accessTokenSecret, consumerSecret, consumerKey)
twit = twitter.Twitter(auth = myAuth)
twit.statuses.update(status = "Test tweet")
