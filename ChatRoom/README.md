# README

> Project Describtion:
Implement a server that provides a common chat room, and implement a GUI client that can communicate with the server. With this system, a client can send text messages to all parties in the chat room, as well as receive notifications when other clients connect or disconnect. Clients do not communicate directly with other clients. Instead, all communication is routed through the central server.
```
Enter the folder:
    cd ChatRoom/


Run server:
    python server.py


Run client:
    <help>: python client.py -h


    RESULT:
    usage: client.py [-h] [--version] [--server_ip [SERVER_IP]]
                    [--server_port [SERVER_PORT]] [--username USERNAME]

    optional arguments:
    -h, --help            show this help message and exit
    --version, -v         show program's version number and exit
    --server_ip [SERVER_IP], -ip [SERVER_IP]
    --server_port [SERVER_PORT], -p [SERVER_PORT]
    --username USERNAME, -u USERNAME


    <version>: python client.py -v or python client.py --version


    RESULT:
    client.py 1.0


    Run the script:
    python client.py -u <username>


Optional<send file in the chat>:
    click the file button, and select the text.txt in this folder
```
