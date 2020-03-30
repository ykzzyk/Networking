import time
import random
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', 12000))

serverSocket.settimeout(10)
while True:
    try:
        rand = random.randint(0, 10)
        start = time.time()
        try:
            message, address = serverSocket.recvfrom(1024)
        except timeout:
            print("\nThe client application has stopped\n")
            break
        end = time.time()
        diff_time = end - start
        if rand < 4:
            num = message.split(" ")[0]
            text = "The package {} loss".format(num)
            serverSocket.sendto(text, address)
            continue
        serverSocket.sendto(str(diff_time), address)
    except KeyboardInterrupt:
        break
    
serverSocket.close()