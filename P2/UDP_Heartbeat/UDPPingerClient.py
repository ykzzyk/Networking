import time
from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
times = 0
received_message = []


RTT_response = []
cnt = 0
while times < 10:
    try:
        request_times = times+1
        message = str(request_times) + " " + str(time.ctime())
        clientSocket.sendto(message, (serverName, serverPort))
        
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        print("\nPackage {}".format(request_times))
        try:
            modifiedMessage = float(modifiedMessage)
            print("The time difference is: " + str(modifiedMessage) + "s")
            RTT_response.append(modifiedMessage)
        except:
            cnt += 1
            print(modifiedMessage)
        times += 1
    except KeyboardInterrupt:
        break

min_RTT = min(RTT_response)
max_RTT = max(RTT_response)
total = 0
for num in RTT_response:
    total += num
average_RTT = total / len(RTT_response)
print("\n\nThe minimal RTT response is: {}s\nThe maximum RTT response is: {}s\nThe average RTT response is: {}s\n".format(min_RTT, max_RTT, average_RTT))

loss_rate = float(cnt) / 10
print("The packet loss rate is: {:.0%}\n".format(loss_rate))

# Close the Client socket
clientSocket.close()
