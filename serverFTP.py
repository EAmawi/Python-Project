from socket import *

serverName = '127.0.0.1' #server host
serverPort = 5555        #server port

serverSocket = socket(AF_INET, SOCK_STREAM) #create server socket
serverSocket.bind((serverName, serverPort)) # give server socket host and port
serverSocket.listen(1)

print ('Server listening....') #print that server is ready


serverSocket.close() #colse server socket