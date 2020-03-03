from socket import *

server_port = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', server_port))

print("Greeting from the server")

while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    modified_message = message.upper()
    serverSocket.sendto(modified_message, clientAddress)