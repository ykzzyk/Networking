import time
from socket import *

# Set the server name and port
serverName = 'localhost'
serverPort = 12000

# Configure the client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Store the received messages
received_message = []

# Store the RTT responses
RTT_response = []

# Count for the actual package loss
cnt = 0

times = 0
# Limit to 10 PINGs
while times < 10:
    try:
        # Package number
        request_times = times+1
        message = str(request_times) + " " + str(time.ctime())
        clientSocket.sendto(message, (serverName, serverPort))
        
        # Receive the modified message
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        print("\nPackage {}".format(request_times))
        try:
            # If the message is number then append to the RTT_response
            # If not, then print the message
            modifiedMessage = float(modifiedMessage)
            print("The time difference is: " + str(modifiedMessage) + "s")
            RTT_response.append(modifiedMessage)
        except:
            cnt += 1
            print(modifiedMessage)
        times += 1
        
    # KeyboardInterrupt: Ctrl-C
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

print("\n\nThe minimal RTT response is: {}s\nThe maximum RTT response is: {}s\nThe average RTT response is: {}s\n".format(min_RTT, max_RTT, average_RTT))

# Calculate the loss rate
loss_rate = float(cnt) / 10
print("The packet loss rate is: {:.0%}\n".format(loss_rate))

# Close the Client socket
clientSocket.close()
