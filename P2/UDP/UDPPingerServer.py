import random
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', 12000))

while True:
    try:
        rand = random.randint(0, 10)
        message, address = serverSocket.recvfrom(1024)
        message = message.upper()
        if rand > 4:
            continue
        serverSocket.sendto(message, address)
    except KeyboardInterrupt:
        break
    
serverSocket.close()