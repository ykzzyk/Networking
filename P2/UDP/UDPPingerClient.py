import time
from socket import *

# Set the server name and port
serverName = 'localhost'
serverPort = 12000

# Configure the client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Set the timeout 1s
clientSocket.settimeout(1)

# Store the received messages
received_message = []

times = 0
# Limit to 10 PINGs
while times < 10:
    try:
        message = "ping"
        start = time.time()
        
        # Send message to server
        clientSocket.sendto(message, (serverName, serverPort))
        
        # Package number
        request_times = times+1
        print('Package' + ' ' + str(request_times) + ' ' + 'ping' + ' start at ' + str(start))
        try:
            # Receive the modified message
            modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
            end = time.time()
            
            # Round-trip-time
            RTT = end - start
            print(modifiedMessage)
            print('RTT: {}\n'.format(RTT))
        except timeout:
            print("Request timed out\n")
            times += 1
            continue
        times += 1
        
    # KeyboardInterrupt: Ctrl-C
    except KeyboardInterrupt:
        break
    
#print(received_message)
clientSocket.close()
