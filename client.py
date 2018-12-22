


from socket import *

serverHost = '127.0.0.1'
serverPort = 5555

while 1:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverHost, serverPort))

    num1 = input('Enter First Number: ')
    clientSocket.sendall(str.encode(num1))

    op = input('Enter Operation: ')
    clientSocket.sendall(str.encode(op))

    num2 = input('Enter Second Number: ')
    clientSocket.sendall(str.encode(num2))

    result = clientSocket.recv(1024)
    print('Result: ', result)

clientSocket.close()