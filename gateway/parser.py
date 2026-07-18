def parse(data):
    b=data
    tranID=int.from_bytes(b[0:2], "big")
    protocolID = int.from_bytes(b[2:4], "big")
    length = int.from_bytes(b[4:6], "big")
    unit = b[6]
    fncode = b[7]
    addr= int.from_bytes(b[8:10], "big")
    count = int.from_bytes(b[10:12], "big")
    if fncode==3:
        return {
            "transaction_id": tranID,
            "protocol_id": protocolID,
            "length": length,
            "unit_id":unit,
            "function_code":fncode,
            "address":addr,
            "count":count
        }
    else:
        return {
            "transaction_id": tranID,
            "protocol_id": protocolID,
            "length": length,
            "unit_id": unit,
            "function_code": fncode,
            "address": addr,
            "value": count
        }