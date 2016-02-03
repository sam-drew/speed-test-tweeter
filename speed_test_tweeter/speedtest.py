import os

def getSpeed(x):
    # Get speedtest-cli path from user.
    speedtestPath = input("Enter the root path of your speedtest_cli.py file: ")
    # Run the speed test
    speed = os.popen((str("python3 " + speedtestPath + " --simple"))).read()

    # Split the returned data into it's constituents.
    speed = speed.split("\n")
    pingSpeed = float(speed[0][6:11])
    downSpeed = float(speed[1][10:15])
    upSpeed = float(speed[2][8:12])

    return[pingSpeed, downSpeed, upSpeed]

    # Allow user to select which speed they would like returned, or all of them.
    # Acceptable arguments are: "all", "down", "up", or "ping".
    if x == "all":
        return(pingSpeed, downSpeed, upSpeed)
    elif x == "down":
        return downSpeed
    elif x == "up":
        return upSpeed
    elif x == "ping":
        return pingSpeed
    else:
        return("Argument not accepted")

if __name__ == "__main__":
    print(getSpeed(input("Enter the argument for getSpeed(): ")))
