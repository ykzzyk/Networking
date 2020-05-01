import socket
import threading
import argparse
import sys

def broadcast(clients, msg, data=""):
    for client in clients:
        message = data.encode('utf-8') + msg
        client.send(message)

def chat_room(c, clients):
    try:
        data = c.recv(4096).decode('utf-8')
        welcome = 'Welcome %s\n! please type "Gotta go, TTYL!" to quit the chat.' % data
        c.send(welcome.encode('utf-8'))
        client = "%s has joined the chat room..." % data
        broadcast(clients, client.encode('utf-8'))
        clients[c] = data
        while True:
            msg = c.recv(4096) 
            bye = 'Gotta go, TTYL!'
            if msg != bye.encode('utf-8'):
                broadcast(clients, msg, data+": ")
            else:
                broadcast(clients, msg, data+": ")
                c.close()
                del clients[c]
                client = "%s has left the chat." % data
                broadcast(clients, client.encode('utf-8'))
                break
    except Exception as e:
        raise e
        sys.exit(1)


if __name__ == '__main__':
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
        backlog=100  # Number of incoming connections that can wait
                    # to be accept()'ed before being turned away
        s.listen(backlog)
    except socket.error as msg:
        print("Error: unable to listen()")
        print("Description: " + str(msg))
        sys.exit()    
    print("Listening socket bound to port %d" % args.server_port)
    
    clients = {}
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
        client_s.send("Enter username: ".encode("utf8"))

        threading.Thread(target = chat_room, args = (client_s, clients)).start()