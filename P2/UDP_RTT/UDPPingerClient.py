import time
from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
times = 0
received_message = []


RTT_response = []
cnt = 0
while times < 10:
    try:
        #clientSocket = socket(AF_INET, SOCK_DGRAM)
        message = "ping"
        start = time.time()
        clientSocket.sendto(message, (serverName, serverPort))
        request_times = times+1
        print('Package' + ' ' + str(request_times) + ' ' + 'ping' + ' start at ' + str(start))
        try:
            modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
            end = time.time()
            RTT = end - start
            RTT_response.append(RTT)
            print(modifiedMessage)
            print('RTT: {}\n'.format(RTT))
        except timeout:
            print("\nRequest timed out\n")
            times += 1
            cnt += 1
            continue
        times += 1
    except KeyboardInterrupt:
        break
    
min_RTT = min(RTT_response)
max_RTT = max(RTT_response)
total = 0
for num in RTT_response:
    total += num
average_RTT = total / len(RTT_response)
print("The minimal RTT response is: {}s\nThe maximum RTT response is: {}s\nThe average RTT response is: {}s\n".format(min_RTT, max_RTT, average_RTT))

loss_rate = float(cnt) / 10
print("The packet loss rate is: {:.0%}\n".format(loss_rate))
clientSocket.close()
