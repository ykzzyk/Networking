#import socket module
from socket import *

# Parameters
TCP_IP = '10.102.19.207'
TCP_PORT = 12003
BUFFER_SIZE = 1024

# Prepare a server socket
serverSocket = socket(AF_INET, SOCK_STREAM)


# Bind IP address and port
serverSocket.bind((TCP_IP, TCP_PORT))

#listening for  Client
serverSocket.listen(1)
print('Ready to serve..')
serverSocket.settimeout(20)

#Establish the connection
connectionSocket, addr = serverSocket.accept()

while True:
    try:
        # Receive the message from the Client
        message = connectionSocket.recv(1024)
        
        filename = message.split()[1].decode('utf-8')
        
        # filename = 'HelloWorld.html'
        with open(filename) as f:
            outputdata = f.read()
        
        # Send one HTTP header line into socket
        connectionSocket.send(b'HTTP/1.1 200 OK\r\n\r\n')

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(bytes(outputdata[i], 'utf-8'))
        
        #Close client socket
        connectionSocket.close()
        break
        
    except IOError:
        #Send response message for file not found
        connectionSocket.send(b'404 Not Found')
        
        #Close client socket
        connectionSocket.close()
        break

# Close Server
serverSocket.close()
print("\n\nServer Quit Successfully!")     