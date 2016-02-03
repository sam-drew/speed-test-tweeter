from speedtest import *
from tweet import *

accessToken = input("Enter the accessToken: ")
accessTokenSecret = input("Enter the accessTokenSecret: ")
consumerSecret = input("Enter the consumerSecret: ")
consumerKey = input("Enter the consumerKey: ")
speed = getSpeed("all")

if speed[1] < 15.0:
    tweet = ("Hey, my ISP, why is my internet speed " + speed[1] + " when I pay for 50mb/s??")
    writeTweet(accessToken, accessTokenSecret, consumerSecret, consumerKey)
