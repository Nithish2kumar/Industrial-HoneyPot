import  socket

from malform import malformFN
from unauthwrite import unauth
from excessivePolling import polling
from regScan import *
from detector import detect
from parser import parse

host="0.0.0.0"
port=502

def startProxy():
    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Gateway is listening on {host}:{port}")
    while True:
        clientSocket, clientAddress = server.accept()
        clientIP=clientAddress[0]
        print(f"Client Connected: {clientAddress}")
        plcSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        fakeplcSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        plcSocket.connect(("127.0.0.1", 1502))
        print("✅ Connected to Real PLC")
        print("---------------")
        handleRequest(clientSocket, plcSocket,fakeplcSocket,clientIP)


def handleRequest(clientSocket,plcSocket,fakeplcSocket,clientIP):
    while True:
        request = clientSocket.recv(1024)
        detres=detectScan(clientIP)

        if not request:
            print("❌  Client Disconnected")
            print("---------------")
            break
        plcSocket.sendall(request)
        response = plcSocket.recv(1024)
        res = parse(request)
        malres=malformFN(res)
        fc=res["function_code"]
        ad=res["address"]
        unauthres=unauth(clientIP,fc)
        pollingRes=polling(clientIP,ad)
        print("--------------------")
        print(f"Transaction ID: {res["transaction_id"]}")
        print(f"Protocol ID: {res["protocol_id"]}")
        print(f"Length : {res["length"]}")
        print(f"Unit ID: {res["unit_id"]}")
        print(f"Function code: {res["function_code"]}")
        print(f"Address: {res["address"]}")
        if res["function_code"] == 3:
            print(f"Count: {res["count"]}")
        else:
            print(f"Value: {res["value"]}")

        decision=detect(res)
        if decision=="ALLOW" and not malres=="MALFORM" and not pollingRes=="Polling" and not detres=="Possible" and not unauthres=="UNAUTH" :
            clientSocket.sendall(response)
        else:
            if unauthres=="UNAUTH":
                print("⚠️  Redirecting to Honeypot due to Unauthorized write.")
            elif malres=="MALFORM":
                print("⚠️  Redirecting to Honeypot due to Malformed packets.")
            elif pollingRes=="Polling":
                print("⚠️  Redirecting to Honeypot due to Excessive polling.")
            elif decision=="REDIRECT":
                print("⚠️  Redirecting to Honeypot due to High risk.")
            elif detres=="Possible":
                print("⚠️  Redirecting to Honeypot due to Register scan.")
            fakeplcSocket.connect(("127.0.0.1",2502))
            fakeplcSocket.sendall(request)
            fakeresponse = fakeplcSocket.recv(1024)
            clientSocket.sendall(fakeresponse)
            print("--------------------")
            print(f"Transaction ID: {res["transaction_id"]}")
            print(f"Protocol ID: {res["protocol_id"]}")
            print(f"Length : {res["length"]}")
            print(f"Unit ID: {res["unit_id"]}")
            print(f"Function code: {res["function_code"]}")
            print(f"Address: {res["address"]}")
            if res["function_code"]==3:
                print(f"Count: {res["count"]}")
            else:
                print(f"Value: {res["value"]}")
            while True:
                request = clientSocket.recv(1024)
                if not request:
                    print("Client Disconnected")
                    break
                fakeplcSocket.sendall(request)
                fakeresponse = fakeplcSocket.recv(1024)
                clientSocket.sendall(fakeresponse)
                res = parse(request)
                print("--------------------")
                print(f"Transaction ID: {res["transaction_id"]}")
                print(f"Protocol ID: {res["protocol_id"]}")
                print(f"Length : {res["length"]}")
                print(f"Unit ID: {res["unit_id"]}")
                print(f"Function code: {res["function_code"]}")
                print(f"Address: {res["address"]}")
                if res["function_code"] == 3:
                    print(f"Count: {res["count"]}")
                else:
                    print(f"Value: {res["value"]}")




    clientSocket.close()
    plcSocket.close()


if __name__=="__main__":
    startProxy()