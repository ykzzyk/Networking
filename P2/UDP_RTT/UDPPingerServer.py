import random
from socket import *

# Configure the server socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))

while True:
    try:
        rand = random.randint(0, 10)
        # Reveive the message from client
        message, address = serverSocket.recvfrom(1024)
        message = message.upper()
        if rand < 4:
            continue
        
        # Send the message to client
        serverSocket.sendto(message, address)
    
    # KeyboardInterrupt: Ctrl-C
    except KeyboardInterrupt:
        break
    
# Close the server socket
serverSocket.close()