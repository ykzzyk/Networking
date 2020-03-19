from socket import *

class TCP():
    def __init__(self, ip, port, bfsz):
        self.ip = ip
        self.port = port
        self.bfsz = bfsz
        
    def tcp_server(self):
        # Prepare a server socket
        serverSocket = socket(AF_INET, SOCK_STREAM)

        # Bind IP address and port
        serverSocket.bind((self.ip, self.port))
        
        # Listening for Client
        serverSocket.listen(1)
        print('Ready to serve..')
        serverSocket.settimeout(80)

        # Establish the connection
        connectionSocket, addr = serverSocket.accept()

        while True:
            try:
                # Receive the message from the Client
                message = connectionSocket.recv(self.bfsz)
                
                filename = message.split()[1].decode('utf-8')
                
                # filename = 'HelloWorld.html'
                with open(filename) as f:
                    outputdata = f.read()
                
                # Send one HTTP header line into socket
                connectionSocket.send(b'HTTP/1.1 200 OK\r\n\r\n')

                # Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(bytes(outputdata[i], 'utf-8'))
                
                #Close client socket
                connectionSocket.close()
                break
                
            except IOError:
                #Send response message for file not found
                connectionSocket.send(b'404 Not Found')
                
                #Close client socket
                connectionSocket.close()
                break
            
        # Close Server
        serverSocket.close()
        print("\n\nServer Quit Successfully!") 
    
    def tcp_client(self):
        # Prepare a client socket
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((self.ip, self.port))

        # Send message to GET HTML file
        MESSAGE = b'GET HelloWorld.html'
        clientSocket.send(MESSAGE)

        # GET the full content from the HTML file
        full_content = ''
        while True:
            data = clientSocket.recv(self.bfsz)
            if not data:
                break
            data = data.decode('utf-8')
            full_content += data
            
        print("received data:", full_content)

        # Close Client
        clientSocket.close()
        print("\n\nClient close successfully!")
        
        
        