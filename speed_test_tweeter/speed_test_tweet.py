from speedtest import *
from tweet import *
import time

def testTweet(tweetThresh):
    if speed[1] < tweetThresh:
        print(speed[1])
        tweet = ("Hey, @virginmedia, why is my internet speed " + str(speed[1]) + "mb/s, when I pay for 50mb/s??")
        writeTweet(accessToken, accessTokenSecret, consumerSecret, consumerKey, tweet)
        print("Tweet complete!")
    elif speed[1] >= tweetThresh:
        print("Speed satisfactory, no tweet.")
    else:
        print("Something has gone wrong, sorry.")

if __name__ == "__main__":
    # Get all keys/secrets.
    accessToken = input("Enter the accessToken: ")
    accessTokenSecret = input("Enter the accessTokenSecret: ")
    consumerSecret = input("Enter the consumerSecret: ")
    consumerKey = input("Enter the consumerKey: ")

    # Get the user's speed threshold for tweeting.
    tweetThresh = input("Enter the speed threshold at which to tweet (just the number): ")
    while tweetThresh.isdigit() == False:
        tweetThresh = input("Enter the speed threshold at which to tweet (just the number): ")
    tweetThresh = float(tweetThresh)

    # Get internet speed data, and set loop counter.
    speed = getSpeed("all")
    counter = 1

    while True:
        testTweet(tweetThresh)
        print(counter)
        counter += 1
        # Wait 15 minutes before testing again.
        time.sleep(900)
