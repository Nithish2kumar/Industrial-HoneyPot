def parse(data):
    b=data
    tranID=int.from_bytes(b[0:2], "big")
    print("Transaction ID: ",tranID)
    protocolID = int.from_bytes(b[2:4], "big")
    print("Protocol ID: ",protocolID)
    length = int.from_bytes(b[4:6], "big")
    print("Length:", length)
    unit = b[6]
    print("Unit ID: ", unit)
    fncode = b[7]
    print("Function Code: ", fncode)
    addr= int.from_bytes(b[8:10], "big")
    print("Address:", addr)
    count = int.from_bytes(b[10:12], "big")
    print("Count: ", count)
    print("--------------------")