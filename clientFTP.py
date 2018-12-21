from socket import *

serverName = '127.0.0.1'  #server host
serverPort = 5555         #server port

clientSocket = socket(AF_INET, SOCK_STREAM) #create client socket
clientSocket.connect((serverName, serverPort)) #connect to server

clientSocket.close() #close cleint socket
