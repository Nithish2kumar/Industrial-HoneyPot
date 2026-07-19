
def detect(parse):
    packet=parse
    print(packet)
    if packet["function_code"]==6:
        return "DROP"
    return "OK"