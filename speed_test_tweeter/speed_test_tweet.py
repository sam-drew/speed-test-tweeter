import time
import datetime
from speedtest import *
from tweet import *
from log import *

def testTweet(tweetThresh, speed, tweet):
    if speed[1] < tweetThresh:
        print(speed[1])
        tweet = tweet.format(speed[1])
        print(tweet)
        writeTweet(accessToken, accessTokenSecret, consumerSecret, consumerKey, tweet)
        print("Tweet complete!")
    elif speed[1] >= tweetThresh:
        print("Speed satisfactory, no tweet.")
    else:
        print("Something has gone wrong, sorry.")

if __name__ == "__main__":
    dateTime = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")

    # Get the path for the speedtest_cli.py file.
    speedtestPath = input("Enter the root path of your speedtest_cli.py file: ")

    # Ask if log should be written.
    log = False
    writeToLog = input("Do you want to log each test's data to file? (y/n) ")
    if writeToLog == "y":
        log = True
        fileName = (str(("Speedtest log", dateTime )))
    else:
        log = False

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

    # Get the wait time between speed test attempts.
    wait = input("Enter the time to wait (a number, in seconds) betweeen speed test attempts: ")
    while wait.isdigit() == False:
        wait = input("Enter the time to wait (a number, in seconds) betweeen speed test attempts: ")
    wait = int(wait)

    # Get the user's personalised tweet for their ISP.
    tweet = input("Enter the message you would like to tweet to your ISP.\nBe sure to include their twitter handle, and even more importantly, the symbols '{}' where you\nwould like your down speed to be substituted: ")
    while len(tweet) > 280:
        tweet = input("Enter the message you would like to tweet to your ISP.\nBe sure to include their twitter handle, and even more importantly, the symbols '{}' where you\nwould like your down speed to be substituted: ")
        while "{}" not in tweet:
            tweet = input("Enter the message you would like to tweet to your ISP.\nBe sure to include their twitter handle, and even more importantly, the symbols '{}' where you\nwould like your down speed to be substituted: ")

    counter = 1

    while True:
        currentDateTime = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")
        # Get speed data.
        speed = getSpeed("all", speedtestPath,)
        # Run speedtest and tweet function.
        testTweet(tweetThresh, speed, tweet)
        print("Test number", counter)
        counter += 1
        # Log test data to file.
        if log == True:
            writeLog(fileName, (str((currentDateTime + "\n" + (str(speed)) + "\n"))))
            print("Log successful.")
        # Wait 15 minutes before testing again.
        time.sleep(wait)
