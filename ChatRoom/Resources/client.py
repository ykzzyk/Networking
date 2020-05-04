#!/usr/bin/env python3

# Simple network socket demo - CLIENT
#
# Set script as executable via: chmod +x client.py
# Run via:  ./client.py <IP> <PORT>
#
# To connect to a server on the same computer, <IP> could
# either be 127.0.0.1 or localhost (they have the same meaning)

import socket
import sys
import argparse

def main():

    # Use argparse method
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('server_ip', nargs='?', default='localhost')
    parser.add_argument('server_port', nargs='?', default=8765)
    parser.add_argument('username')
    args = parser.parse_args()
    
    # Create TCP socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("Error: could not create socket")
        print("Description: " + str(msg))
        sys.exit()

    print("Connecting to server at " + str(args.server_ip) + " on port " + str(args.server_port))
     
    # Connect to server
    try:
        s.connect((args.server_ip , args.server_port))
    except socket.error as msg:
        print("Error: Could not open connection")
        print("Description: " + str(msg))
        sys.exit()
 
    print("Connection established")
    
    # Send message to server
    # string_unicode = "Tiger Roar!"
    string_unicode = "Car Meow!"
    raw_bytes = bytes(string_unicode,'ascii')
    
    try:
        # Send the string
        # Note: send() might not send all the bytes!
        # You should loop, or use sendall()
        bytes_sent = s.send(raw_bytes)
    except socket.error as msg:
        print("Error: send() failed")
        print("Description: " + str(msg))
        sys.exit()
 
    print("Sent %d bytes to server" % bytes_sent)

    # Close socket
    try:
        s.close()
    except socket.error as msg:
        print("Error: unable to close() socket")
        print("Description: " + str(msg))
        sys.exit()

    print("Sockets closed, now exiting")

if __name__ == "__main__":
    sys.exit(main())