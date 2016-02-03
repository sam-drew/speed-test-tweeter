import os

def getSpeed():
    # Run the speed test
    speed = os.popen("python3 /home/sam/.local/lib/python3.4/site-packages/speedtest_cli.py --simple")

    # Split the returned data into it's constituents.
    speed = speed.split("\n")
    pingSpeed = speed[0]
    downSpeed = speed[1]
    upSpeed = speed[2]

    return(pingSpeed, downSpeed, upSpeed)
    
if __name__ == "__main__":
    print(getSpeed())
