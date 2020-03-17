from tcp import *
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('parameter')
    args = parser.parse_args()
    
    info = TCP('localhost', 12003, 1024)
    
    if args.parameter == 'server':
        server = TCP.tcp_server(info)
    elif args.parameter == 'client':
        client = TCP.tcp_client(info)
    
    
    