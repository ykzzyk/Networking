from socket import *
import requests
import sys
    

if __name__ == '__main__':  
    # Proxy server: localhost
    # Create a server socket, bind it to a port and start listening 
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    # Fill in start.
    port = 8888
    tcpSerSock.bind(('', port))
    
    tcpSerSock.listen()
    # Fill in end.
    
    while 1:
        # Strat receiving data from the client
        print('Ready to serve...')
        tcpCliSock, addr = tcpSerSock.accept()
        print('Received a connection from:{}'.format(addr))
        message = tcpCliSock.recv(1024).decode()
        print(f'MESSAGE:\n\n{message}END OF MESSAGE\n\n')
        # Extract the filename from the given message 
        
        hostn = message.split()[1]
        print(f'hostn: {hostn}')
        filename = hostn.partition("/")[2]
        print(f'filename:{filename}')
        fileExist = "false"
        filetouse = "/" + filename
        print(f'filetouse:{filetouse}')
        
        try:
            # Check whether the file exist in the cache 
            f = open(filetouse[1:], "rb")
            outputdata = f.read()
            print(outputdata)
            fileExist = "true"
            # ProxyServer finds a cache hit and generates a response message 
            tcpCliSock.send(b"HTTP/1.0 200 OK\r\n") 
            tcpCliSock.send(b"Content-Type:text/html\r\n\r\n")
            # Fill in start.
            tcpCliSock.sendall(outputdata)
            # Fill in end.
            print('Read from cache\n\n')
            # Error handling for file not found in cache
        except FileNotFoundError:
            if fileExist == "false":
                # Create a socket on the proxyserver
                c = socket(AF_INET, SOCK_STREAM) 
                hostn = filename.replace("www.","",1)
                try:
                    # Connect to the socket to port 80
                    # Fill in start.
                    print("CONNECTING")
                    print(f'Connected hostn:{hostn}')
                    
                    c.connect((hostn, 80))
                    print("FINISHED CONNECTING")
                    # Fill in end.
                    r = requests.get("http://www.google.com")
                    print(r.content)
                    # Create a new file in the cache for the requested file. 
                    # Also send the response in the buffer to client socket and the corresponding file in the cache
                    bodyFile = open("./" + filename,"wb")
                    bodyFile.write(r.content)
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