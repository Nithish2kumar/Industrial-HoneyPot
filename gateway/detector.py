from risk import calculate
def detect(parse):
    packet=parse
    print(packet)
    risk=calculate(packet)
    if risk>=40:
        return "REDIRECT"
    
    return "ALLOW"
