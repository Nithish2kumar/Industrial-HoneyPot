import  socket

host="0.0.0.0"
port=5020

def startProxy():
    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Gateway is listening on {host}:{port}")
    while True:
        clientSocket, clientAddress=server.accept()
        print(f"Client Connected: {clientAddress}")
        plcSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        plcSocket.connect(("127.0.0.1",502))
        print("Connected to Real PLC")
        while True:
            request=clientSocket.recv(1024)
            plcSocket.sendall(request)
            response=plcSocket.recv(1024)
            clientSocket.sendall(response)
        
        
        

if __name__=="__main__":
    startProxy()