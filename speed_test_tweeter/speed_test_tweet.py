from speedtest import *
from tweet import *
import time

def testTweet():
    if speed[1] < 15.00:
        print(speed[1])
        tweet = ("Hey, my ISP, why is my internet speed " + str(speed[1]) + "mb/s, when I pay for 50mb/s??")
        writeTweet(accessToken, accessTokenSecret, consumerSecret, consumerKey, tweet)

if __name__ == "__main__":
    accessToken = input("Enter the accessToken: ")
    accessTokenSecret = input("Enter the accessTokenSecret: ")
    consumerSecret = input("Enter the consumerSecret: ")
    consumerKey = input("Enter the consumerKey: ")
    speed = getSpeed("all")
    run = True
    counter = 1
    while run == True:
        testTweet()
        print(counter)
        counter += 1
        time.sleep(60)
