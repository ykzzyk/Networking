from socket import *
import requests
import sys


# Link:
# http://localhost:8888/search?hl=en&gbv=2&ie=ISO-8859-1&q=help&oq=help&aqs=heirloom-srp..0l5
# http://localhost:8888/search?hl=en&gbv=2&ie=ISO-8859-1&q=heelp&oq=heelp&aqs=heirloom-srp..0l5
# http://localhost:8888/search?hl=en&gbv=2&ie=ISO-8859-1&q=heelo&oq=heelo&aqs=heirloom-srp..0l5
if __name__ == '__main__':
    if len(sys.argv) <= 1: 
        print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP  Address Of Proxy Server')
        sys.exit(2)
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
        
        filename = message.split()[1].partition("/")[2]
        filename = filename.replace("/", "_")
        fileExist = "false"
        
        try:
            # Check whether the file exist in the cache
            f = open(filename, "rb")
            outputdata = f.read()
            fileExist = "true"
            
            # Headers
            # ProxyServer finds a cache hit and generates a response message
            tcpCliSock.send(b"HTTP/1.1 200 OK\r\n")
            tcpCliSock.send(b"Content-Type:text/html\r\n\r\n")

            # SEND
            tcpCliSock.sendall(outputdata + b"\r\n\r\n")
            print('Read from cache\n\n')
            
        # Error handling for file not found in cache
        except FileNotFoundError:
            if fileExist == "false":
                # Create a socket on the proxyserver
                c = socket(AF_INET, SOCK_STREAM) 
                try:
                    # Connect to the socket to port 80
                    
                    print("CONNECTING")
                    c.connect((gethostbyname(f'www.{sys.argv[1]}.com'), 80))
                    print("FINISHED CONNECTING")
                          
                    if message.split()[1] == f'/{sys.argv[1]}.com':
                        r = requests.get(f"http://www.{sys.argv[1]}.com/")
                    else:
                        r = requests.get(f"http://www.{sys.argv[1]}.com/" + message.split()[1])
                    
                    # Create a new file in the cache for the requested file. 
                    # Also send the response in the buffer to client socket and the corresponding file in the cache
                    file = open("./" + filename,"wb")
                    
                    file.write(r.content)
                except Exception as e:
                    raise e
                    print('Illegal request')
            else:
                # HTTP response message for file not found
                print('404 Error file not found.')
    
        # Close the client and the server sockets
        tcpCliSock.close()
    tcpSerSock.close()