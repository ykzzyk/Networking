from socket import *
import threading


def tcp_server(TCP_IP, TCP_PORT, BUFFER_SIZE):
    
    # Prepare a server socket
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Bind TCP_IP address and TCP_PORT
    serverSocket.bind((TCP_IP, TCP_PORT))
        
    threads = []

    #listening for  Client
    serverSocket.listen(5)
    serverSocket.settimeout(80)
    print('Multithread server ready to serve..')

    #Establish the connection
    while True:
        if len(threads) == 5:
            break
        try:
            connectionSocket, addr = serverSocket.accept()
            newthread = threading.Thread(target = tcp_server, args = (TCP_IP, TCP_PORT, BUFFER_SIZE))
            newthread.start()
            threads.append(newthread)
            # Receive the message from the Client
            message = connectionSocket.recv(BUFFER_SIZE)
            
            filename = message.split()[1].decode('utf-8')
            
            # filename = 'HelloWorld.html'
            with open(filename) as f:
                outputdata = f.read()
            
            # Send one HTTP header line into socket
            connectionSocket.send(b'\r\n\r\nHTTP/1.1 200 OK\r\n\r\n')

            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(bytes(outputdata[i], 'utf-8'))
            
            #Close client socket
            connectionSocket.close()
            
        except IOError:
            #Send response message for file not found
            connectionSocket.send(b'404 Not Found')
            
            #Close client socket
            connectionSocket.close()
        
    for t in threads:
        t.join()
            
        
    # Close Server     
    serverSocket.close()
    
if __name__ == "__main__":
    # Parameters
    TCP_IP = 'localhost'
    TCP_PORT = 12003
    BUFFER_SIZE = 1024
    
    tcp_server(TCP_IP, TCP_PORT, BUFFER_SIZE)