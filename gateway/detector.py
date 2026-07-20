
def detect(parse):
    packet=parse
    print(packet)
    restrictedReg=[0,3]
    if packet["function_code"]==6 and packet["address"] in restrictedReg:
        print("ALERT: Attempt to modify restricted register.")
        return "DROP"
    return "OK"
