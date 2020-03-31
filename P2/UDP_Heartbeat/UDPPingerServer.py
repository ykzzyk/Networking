import time
import random
from socket import *

# Configure the server socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))

# Set timeout 10s
serverSocket.settimeout(10)
while True:
    try:
        rand = random.randint(0, 10)
        start = time.time()
        try:
            # Reveive the message from client
            message, address = serverSocket.recvfrom(1024)
        except timeout:
            print("\nThe client application has stopped\n")
            break
        end = time.time()
        # Calculate the time difference
        diff_time = end - start
        if rand < 4:
            # To get the package number
            num = message.split(" ")[0]
            text = "The package {} loss".format(num)
            # Send the text to client
            serverSocket.sendto(text, address)
            continue
        # Send the time difference to client
        serverSocket.sendto(str(diff_time), address)
    
    # KeyboardInterrupt: Ctrl-C
    except KeyboardInterrupt:
        break
    
# Close the server socket
serverSocket.close()