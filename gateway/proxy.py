import  socket

from detector import detect
from parser import parse

host="0.0.0.0"
port=5020

def startProxy():
    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Gateway is listening on {host}:{port}")
    while True:
        clientSocket, clientAddress = server.accept()
        print(f"Client Connected: {clientAddress}")
        plcSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        plcSocket.connect(("127.0.0.1", 502))
        print("Connected to Real PLC")
        handleRequest(clientSocket, plcSocket)


def handleRequest(clientSocket,plcSocket):
    while True:
        request = clientSocket.recv(1024)
        if not request:
            print("Client Disconnected")
            break
        plcSocket.sendall(request)
        response = plcSocket.recv(1024)
        res = parse(request)
        manual=detect(res)
        if manual=="OK":
            clientSocket.sendall(response)
        else:
            print("Request dropped")


    clientSocket.close()
    plcSocket.close()
    print("Connection Closed")

if __name__=="__main__":
    startProxy()