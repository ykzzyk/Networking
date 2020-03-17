from socket import *
import argparse


# Parameters
#TCP_IP = 'localhost'
#TCP_PORT = 12003
BUFFER_SIZE = 1024

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument('server_host')
parser.add_argument('server_port')
parser.add_argument('filename')
args = parser.parse_args()

# Prepare a client socket
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((args.server_host, int(args.server_port)))

# Send message to GET HTML file
# Filename: HelloWorld.html
MESSAGE = f'GET {args.filename}'
MESSAGE = bytes(MESSAGE, 'utf-8')
clientSocket.send(MESSAGE)

# GET the full content from the HTML file
full_content = ''
while True:
    data = clientSocket.recv(BUFFER_SIZE)
    if not data:
        break
    data = data.decode('utf-8')
    full_content += data
    
with open('files_from_server/HelloWorld.html', 'w') as f:
    f.write(full_content)

print("received data:", full_content)

# Close Client
clientSocket.close()
print("\n\nClient close successfully!")

