import time
from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
times = 0
received_message = []


while times < 10:
    try:
        #clientSocket = socket(AF_INET, SOCK_DGRAM)
        message = "ping"
        start = time.time()
        clientSocket.sendto(message, (serverName, serverPort))
        request_times = times+1
        if request_times == 1:
            print('ping' + ' ' + str(request_times) + ' ' + "time:" + ' start at ' + str(start))
        else:
            print('ping' + ' ' + str(request_times) + ' ' + "times:" + ' start at ' + str(start))
        try:
            modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
            end = time.time()
            RTT = end - start
            print(modifiedMessage)
            print('RTT: {}\n'.format(RTT))
        except timeout:
            print("Request timed out\n")
            times += 1
            continue
        times += 1
    except KeyboardInterrupt:
        break
    
#print(received_message)
clientSocket.close()
