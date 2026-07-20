risk=0
restrictedReg=[0,3]

def calculate(packet):
    global risk
    if packet["funciton_code"]==3:
        risk+=0
    elif packet["funciton_code"]==6:
        risk+=20
    elif packet["funciton_code"]==6 and packet["address"] in restricedReg:
        risk+=40
    elif packet["function_code"]!=3 or 6:
        risk+=50
        
    return risk