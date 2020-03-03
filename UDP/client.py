from socket import *

server_name = 'Server'
server_port = 12000

clientSocket = socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Input lowercase sentence")

clientSocket.sendto(message, (server_name, server_port))

modified_message, server_address = clientSocket.recvfrom(2048)

clientSocket.close()
