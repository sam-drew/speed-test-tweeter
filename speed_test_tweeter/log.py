def writeLog(fileName, data):
    f = open((str(fileName + ".txt")), "a")
    f.write((str((data + "\n"))))
    f.close()
