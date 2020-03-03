import socket

server_name = '127.0.0.1'
server_port = 12000

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Input lowercase sentence:\n")
message = message.encode()

clientSocket.sendto(message, (server_name, server_port))

modified_message, server_address = clientSocket.recvfrom(2048)

print(f'modified_message: {modified_message}')
clientSocket.close()
