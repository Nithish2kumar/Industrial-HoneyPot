trustedIP=["10.104.176.53","127.0.0.1"]

def unauth(IP,FC):

    if IP not in trustedIP and FC==03:
        return "UNAUTH"