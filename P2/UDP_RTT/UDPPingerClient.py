import time
from socket import *

# Set the server name and port
serverName = 'localhost'
serverPort = 12000

# Configure the client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Set the timeout 1s
clientSocket.settimeout(1)
times = 0

# Store the received messages
received_message = []

# Store the RTT responses
RTT_response = []

# Count for the actual package loss
cnt = 0

# Limit to 10 PINGs
while times < 10:
    try:
        # Send the message to server
        message = "ping"
        start = time.time()
        clientSocket.sendto(message, (serverName, serverPort))
        request_times = times+1
        print('Package' + ' ' + str(request_times) + ' ' + 'ping' + ' start at ' + str(start))
        try:
            # Reveive the message from server
            modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
            end = time.time()
            RTT = end - start
            
            # Round-trip-time
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
    
# Find the minimal RTT
min_RTT = min(RTT_response)

# Find the maximum RTT
max_RTT = max(RTT_response)

# Find the average RTT
total = 0
for num in RTT_response:
    total += num
average_RTT = total / len(RTT_response)

print("The minimal RTT response is: {}s\nThe maximum RTT response is: {}s\nThe average RTT response is: {}s\n".format(min_RTT, max_RTT, average_RTT))

# Calculate the loss rate
loss_rate = float(cnt) / 10
print("The packet loss rate is: {:.0%}\n".format(loss_rate))

# Close the Client socket
clientSocket.close()
