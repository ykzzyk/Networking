from socket import *
import requests
import sys

if __name__ == '__main__':
    # Proxy server: localhost
    # Create a server socket, bind it to a port and start listening 
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    port = 8888
    tcpSerSock.bind(('', port))
    tcpSerSock.listen()
    
    while 1:
        # Strat receiving data from the client
        print('Ready to serve...')
        
        # ACCEPT
        tcpCliSock, addr = tcpSerSock.accept()
        print('Received a connection from:{}'.format(addr))
        
        # RECEIVE
        message = tcpCliSock.recv(1024).decode()
        print(f'MESSAGE:\n\n{message}END OF MESSAGE\n\n')
        
        hostn = message.split()[1]
        print(f'hostn: {hostn}')
        filename = hostn.partition("/")[2]
        print(f'filename:{filename}')
        fileExist = "false"
        filetouse = "/" + filename
        print(f'filetouse:{filetouse}')
        
        try:
            # Check whether the file exist in the cache
            filename = filename.replace("/", "_")
            f = open(filetouse[1:], "rb")
            outputdata = f.read()
            print(outputdata)
            print("\n\n-------------------------------------------\n\n")
            fileExist = "true"
            
            # Headers
            # ProxyServer finds a cache hit and generates a response message
            tcpCliSock.send(b"HTTP/1.1 200 OK\r\n") 
            tcpCliSock.send(b"Content-Type:text/html\r\n\r\n")
            
            # SEND
            tcpCliSock.sendall(outputdata)
            print('Read from cache\n\n')
            
        # Error handling for file not found in cache
        except FileNotFoundError:
            if fileExist == "false":
                # Create a socket on the proxyserver
                c = socket(AF_INET, SOCK_STREAM) 
                try:
                    # Connect to the socket to port 80
                    
                    print("CONNECTING")
                    hostname = gethostbyname('www.google.com')
                    c.connect((hostname, 80))
                    print("FINISHED CONNECTING")
                          
                    r = requests.get("http://www.google.com")
                    # gif = requests.get('http://google.com/' + hostn)
                    # Create a new file in the cache for the requested file. 
                    # Also send the response in the buffer to client socket and the corresponding file in the cache
                    file1 = open("./" + filename,"wb")
                    print(r.content)
                    file1.write(r.content)
                except Exception as e:
                    raise e
                    print('Illegal request')
            else:
                # HTTP response message for file not found 
                # Fill in start.
                print('404 Error file not found.')
                # Fill in end.
    
        # Close the client and the server sockets
        tcpCliSock.close()
    # Fill in start.
    tcpSerSock.close()
    # Fill in end.