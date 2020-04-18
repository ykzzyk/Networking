from socket import * 
import sys

if __name__ == '__main__':  
    # Proxy server: localhost
    # Create a server socket, bind it to a port and start listening 
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    # Fill in start.
    port = 8888
    tcpSerSock.bind(("", port))
    
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
        
        hostn = message.split('\r\n')[1]
        print(f'hostn: {message.split()[1]}')
        filename = ".".join(hostn.partition("/")[2:])
        print(f'filename:{filename}')
        fileExist = "false"
        filetouse = "/" + filename
        print(f'filetouse:{filetouse}')
        
        try:
            # Check wether the file exist in the cache 
            f = open(filetouse[1:], "r")
            outputdata = f.readlines()
            fileExist = "true"
            # ProxyServer finds a cache hit and generates a response message 
            tcpCliSock.send("HTTP/1.0 200 OK\r\n") 
            tcpCliSock.send("Content-Type:text/html\r\n")
            # Fill in start.
            for i in range(0, len(outputdata)):
                tcpCliSock.send(outputdata[i])
            # Fill in end.
            print('Read from cache')
            # Error handling for file not found in cache
        except IOError:
            if fileExist == "false":
                # Create a socket on the proxyserver
                c = socket(AF_INET, SOCK_STREAM) 
                hostn = filename.replace("www.","",1)
                
                print(f'hostn:{hostn}')
                
                addr, port = hostn.split(":")
                
                try:
                    # Connect to the socket to port (443, 80)
                    # Fill in start.
                    print("CONNECTING")
                    c.connect((addr, port))
                    print("FINISHED CONNECTING")
                    # Fill in end.
                    # Create a temporary file on this socket and ask port 443 for the file requested by the client
                    print("makefile")
                    fileobj = c.makefile('rb', 0)
                    command = "GET " + "https://" + fileobj + " HTTP/1.0\r\n"
                    print("WRITING COMMAND")
                    print(command)
                    fileobj.write(command)
                    # Read the response into buffer
                    # Fill in start.
                    print("RECEIVING BUFFER")
                    buffer = c.recv(1024)
                    # Fill in end.
                    # Create a new file in the cache for the requested file. 
                    # Also send the response in the buffer to client socket and the corresponding file in the cache
                    tmpFile = open("./" + filename,"wb")
                    print(f'TMPFILE: {tmpFile}')
                    # Fill in start.
                    for i in range(0, len(buffer)):
                        tmpFile.write(buffer[i])
                    # Fill in end.
                except Exception as e:
                    raise e
                    print("EXCEPTION ERROR: ", e)
                    print('Illegal request')
                    tcpCliSock.close()
                    
                break
            
            else:
                # HTTP response message for file not found 
                # Fill in start.
                print('404 Error file not found.')
                # Fill in end.
    
        # Close the client and the server sockets
        tcpCliSock.close()