address=[1,2,3,4]

def malformFN(res):
    if len(res)<12:
        return "MALFORM"
    elif res["protocol_id"] !=0:
        return "MALFORM"
    elif res["length"]!=len(res)-6:
        return "MALFORM"
    elif res["function_code"]==3 and res["address"] not in address:
        return  "MALFORM"
    elif res["function_code"]==6 and res["address"] not in address and not res["value"]:
        return  "MALFORM"

    else:
        return "NO"