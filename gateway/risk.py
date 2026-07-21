risk=0
restrictedReg=[0,3]

def calculate(packet):
    global risk
    if packet["function_code"] not in [3,6]:
        risk+=50
    elif packet["function_code"]==6 and packet["address"] in restrictedReg:
        risk+=40
    elif packet["function_code"]==6:
        risk+=20
    elif packet["function_code"]==3:
        risk+=0
        
    return risk