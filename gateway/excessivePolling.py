import time

lastrequest={}

def polling(clientIP,register):
    now = time.time()
    key=(clientIP,register)

    if key in lastrequest:
        interval=now-lastrequest[key]
        print(interval)
        if interval<2:
            return "Polling"

    lastrequest[key]=now

