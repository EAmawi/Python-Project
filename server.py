


from socket import *

serverHost = '127.0.0.1'
serverPort = 5555

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverHost, serverPort))

serverSocket.listen(1)
print('Ready to recieve...')

while 1:
    connectionSocket, addr = serverSocket.accept()

    num1 = connectionSocket.recv(1024)
    op = connectionSocket.recv(1024)
    num2 = connectionSocket.recv(1204)

    connectionSocket.send(result)
    
    connectionSocket.close()

