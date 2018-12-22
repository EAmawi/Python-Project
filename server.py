from socket import *

serverHost = '127.0.0.1'
serverPort = 5555

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverHost, serverPort))

serverSocket.listen(1)
print('Ready...')

msg1 = 'Enter First Number: '
msg1 = 'Enter Operation ( + or - or * or / ): '
msg1 = 'Enter Second Number: '

while 1:
    connectionSocket, addr = serverSocket.accept()

    connectionSocket.send(str.encode(msg1))
    num1 = connectionSocket.recv.(1024).decode()

    connectionSocket.send(str.encode(msg2))
    op = connectionSocket.recv(1024).decode()

    connectionSocket.send(str.encode(msg3))
    num2 = connectionSocket.recv(1204).decode()

    result = 0;
    connectionSocket.send(str.encode(result))

    connectionSocket.close()

