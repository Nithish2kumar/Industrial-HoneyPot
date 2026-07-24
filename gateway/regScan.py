import time

lastIP={}
def detectScan(clientIP):
    now = time.time()

    if clientIP in lastIP:
        interval=now-lastIP[clientIP]
        if interval<3:
            return "Possible"
    else:
        print(f"{clientIP}: First packet")
    lastIP[clientIP]=now


