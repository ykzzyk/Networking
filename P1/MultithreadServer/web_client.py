from socket import *

# Parameters
TCP_IP = '10.102.19.207'
TCP_PORT = 12007
BUFFER_SIZE = 1024

# Prepare a client socket
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((TCP_IP, TCP_PORT))

# Send message to GET HTML file
MESSAGE = b'GET HelloWorld.html'
clientSocket.send(MESSAGE)

# GET the full content from the HTML file
full_content = ''
while True:
    data = clientSocket.recv(BUFFER_SIZE)
    if not data:
        break
    data = data.decode('utf-8')
    full_content += data
    
print("received data:", full_content)

# Close Client
print("\n\nClient close successfully!")
clientSocket.close()

