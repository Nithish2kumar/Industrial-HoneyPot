import time

from gateway.proxy import startProxy

clientIP = startProxy()


lastIP={

}

def detectScan():
    now = time.time()


    if clientIP in lastIP:
        interval=now-lastIP[clientIP]
        print(f"{clientIP}:{interval:.3f} sec")
    else:
        print(f"{clientIP}: First packet")
    lastIP[clientIP]=now
