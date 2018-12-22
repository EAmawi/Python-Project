from socket import *

serverHost = '127.0.0.1'
serverPort = 5555

while 1:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverHost, serverPort))

    msg1 = clientSocket.recv(1024).decode()
    num1 = input(msg1)
    clientSocket.sendall(num1.encode())

    msg2 = clientSocket.recv(1024).decode()
    op = input(msg2)
    clientSocket.sendall(op.encode())

    msg3 = clientSocket.recv(1024).decode()
    num2 = input(msg3)
    clientSocket.sendall(num2.encode())

    result = clientSocket.recv(1024).decode()
    print('Result: ', result)

clientSocket.close()