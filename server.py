from socket import *

serverHost = '127.0.0.1'
serverPort = 5555

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverHost, serverPort))

serverSocket.listen(1)
print('Ready...')

msg1 = 'Enter First Number: '
msg2 = 'Enter Operation ( + or - or * or / ): '
msg3 = 'Enter Second Number: '

while 1:
    connectionSocket, addr = serverSocket.accept()

    connectionSocket.send(msg1.encode())
    num1 = connectionSocket.recv(1024).decode()

    connectionSocket.send(msg2.encode())
    op = connectionSocket.recv(1024).decode()

    connectionSocket.send(msg3.encode())
    num2 = connectionSocket.recv(1204).decode()

    result = eval(num1 + op + num2)
    result = str(result)
    connectionSocket.send(result.encode())

    connectionSocket.close()

