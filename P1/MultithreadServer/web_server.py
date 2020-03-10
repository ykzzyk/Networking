#import socket module
from socket import *
import threading

def tcp_server(ip, port, bfsz):

    # Prepare a server socket
    serverSocket = socket(AF_INET, SOCK_STREAM)


    # Bind IP address and port
    serverSocket.bind((ip, port))
    
    #listening for  Client
    serverSocket.listen(1)
    serverSocket.settimeout(80)

    #Establish the connection
    connectionSocket, addr = serverSocket.accept()

    while True:
        try:
            # Receive the message from the Client
            message = connectionSocket.recv(bfsz)
            
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
    
def multithreading(ip, port, bfsz):
    num = 5
    cnt = 0
    threads = []
    while cnt < num:
        t = threading.Thread(target = tcp_server, args = (ip, port+cnt, bfsz))
        t.start()
        threads.append(t)
        cnt = cnt + 1
        
    for k, t in enumerate(threads):
        print(t)
        t.join()
        print(f"\nServer {k+1} Quit Successfully!\n\n")  
        
        
    
    
if __name__ == '__main__':
    # Parameters
    TCP_IP = '10.102.19.207'
    TCP_PORT = 12003
    BUFFER_SIZE = 1024
    
    print('Multithread server ready to serve..')
    multithreading(TCP_IP, TCP_PORT, BUFFER_SIZE)

    
        
    