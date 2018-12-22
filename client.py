from socket import *

serverHost = '127.0.0.1'
serverPort = 5555

while 1:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverHost, serverPort))

    msg1 = clientSocket.recv(1024).decode()
    num1 = input(msg1)
    clientSocket.sendall(str.encode(num1))

    msg2 = clientSocket.recv(1024).decode()
    op = input(msg2)
    clientSocket.sendall(str.encode(op))

    msg3 = clientSocket.recv(1024).decode()
    num2 = input(msg3)
    clientSocket.sendall(str.encode(num2))

    result = clientSocket.recv(1024).decode()
    print('Result: ', result)

clientSocket.close()