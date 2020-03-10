#import socket module
from socket import *
import threading

def tcp_server(ip, port, bfsz):

    # Prepare a server socket
    serverSocket = socket(AF_INET, SOCK_STREAM)


    # Bind IP address and port
    serverSocket.bind((TCP_IP, TCP_PORT))
    
    #listening for  Client
    n = 5
    serverSocket.listen(n)
    print('Multithread server ready to serve..')
    serverSocket.settimeout(200)

    #Establish the connection
    connectionSocket, addr = serverSocket.accept()

    while True:
        try:
            # Receive the message from the Client
            message = connectionSocket.recv(1024)
            
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

    
    return n
    
def multi_thread(num, ip, port, bfsz):
    t = 0
    threads = []
    while t < num:
        t = threading.Thread(target = tcp_server, args = (ip, port+int(t), bfsz))
        t.start()
        threads.append(t)
        t = int(t) + 1
        
    return threads
    
if __name__ == '__main__':
    # Parameters
    TCP_IP = '10.102.19.207'
    TCP_PORT = 12003
    BUFFER_SIZE = 1024
    
    num = tcp_server(TCP_IP, TCP_PORT, BUFFER_SIZE)
    threads = multi_thread(num, TCP_IP, TCP_PORT, BUFFER_SIZE)

    for t in threads:
        t.join()
        
    # Close Server 
    print("\n\nServer Quit Successfully!")      
    serverSocket.close()