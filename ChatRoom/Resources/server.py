#!/usr/bin/env python3

# Simple network socket demo - SERVER
#
# Set script as executable via: chmod +x server.py
# Run via: ./server.py <PORT>

import socket
import sys
import argparse
import threading

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.clientsocket = clientsocket
        print("New connection added: ", clientAddress)
    def run(self):
        msg = ''
        while True:
            data = self.clientsocket.recv(4096)
            msg += data.decode('utf-8')
            print("from client", msg)
            #self.clientsocket.send(msg.encode('utf-8'))
        print("Client at ", clientAddress , " disconnected...")
        

def main():

    # Use argparse method
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('server_port', nargs='?', default=8765)
    args = parser.parse_args()

    # Create TCP socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("Error: could not create socket")
        print("Description: " + str(msg))
        sys.exit()

    # Bind to listening port
    try:
        host=''  # Bind to all interfaces
        s.bind((host,args.server_port))
    except socket.error as msg:
        print("Error: unable to bind on port %d" % args.server_port)
        print("Description: " + str(msg))
        sys.exit()

    # Listen
    try:
        backlog=10  # Number of incoming connections that can wait
                    # to be accept()'ed before being turned away
        s.listen(backlog)
    except socket.error as msg:
        print("Error: unable to listen()")
        print("Description: " + str(msg))
        sys.exit()    
    print("Listening socket bound to port %d\n\n" % args.server_port)
    
    threads = []
    while True:
        # Accept an incoming request
        try:
            (client_s, client_addr) = s.accept()
            # If successful, we now have TWO sockets
            #  (1) The original listening socket, still active
            #  (2) The new socket connected to the client
        except socket.error as msg:
            print("Error: unable to accept()")
            print("Description: " + str(msg))
            sys.exit()

        print("Accepted incoming connection from client")
        print("Client IP, Port = %s" % str(client_addr))

        threads.append(ClientThread(client_addr, client_s))
        threads[-1].start()
        
        try:
            client_s.close()
        except socket.error as msg:
            print("Error: unable to close() socket")
            print("Description: " + str(msg))
            sys.exit()

if __name__ == "__main__":
    sys.exit(main())
