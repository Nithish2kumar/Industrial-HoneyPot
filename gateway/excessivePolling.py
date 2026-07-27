import time

lastrequest={}

def polling(clientIP,register):
    now = time.time()
    key=(clientIP,register)

    if key in lastrequest:
        interval=now-lastrequest[key]
        if interval<3 and register:
            return "Polling"

    lastrequest[clientIP]=now
    return None


