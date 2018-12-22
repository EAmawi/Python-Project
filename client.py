from socket import *

serverHost = '127.0.0.1'
serverPort = 5555

print('start...')

while 1:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverHost, serverPort))

    msg1 = clientSocket.recv(1024)
    num1 = input(msg1)
    clientSocket.sendall(str.encode(num1))

    msg2 = clientSocket.recv(1024)
    op = input(msg2)
    clientSocket.sendall(str.encode(op))

    msg3 = clientSocket.recv(1024)
    num2 = input(msg3)
    clientSocket.sendall(str.encode(num2))

    result = clientSocket.recv(1024)
    print('Result: ', result)

clientSocket.close()