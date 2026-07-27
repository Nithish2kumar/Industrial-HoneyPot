import time

lastrequest={}

def polling(clientIP,register):
    now = time.time()
    key=(clientIP,register)

    if key in lastrequest:
        interval=now-lastrequest[key]
        if interval<0.1:
            return "Polling"

    lastrequest[clientIP]=now
    return None


