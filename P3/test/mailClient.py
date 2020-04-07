from socket import *
import base64

if __name__ == '__main__':
    # Choose a mail server (e.g. Google mail server) and call it mailserver 
    mailserver = 'smtp-mail.outlook.com'
    mail_port = 587

    # Create socket called clientSocket and establish a TCP connection with mailserver 
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, mail_port))

    recv = clientSocket.recv(1024) 
    print(recv.decode())
    
    if recv.decode()[:3] != '220':
        print('220 reply not received from server.')
        
    # Send HELO command and print server response. 
    #heloCommand = b'HELO smtp.gmail.com\r\n' 
    heloCommand = b'HELO Nicole\r\n'
    clientSocket.send(heloCommand)
    recv_helo = clientSocket.recv(1024)
    print('HELO command reply: {}'.format(recv_helo.decode()))
    if recv_helo.decode()[:3] != '250':
        print('250 reply not received from server.')
       
       
    # Send STARTTLS command
    startllsCommand = b'STARTTLS\r\n'
    clientSocket.send(startllsCommand)
    recv_startlls = clientSocket.recv(1024)
    print('STARTTLS command reply: {}'.format(recv_startlls.decode()))
    
    
    # # Username & Password
    # username = b'yZhang5@mail.stmarytx.edu'
    # password = b'Zykzykzyk123'

    # clientSocket.send(b"AUTH LOGIN\r\n")
    # clientSocket.send(base64.b64encode(username)+b'\r\n')
    # clientSocket.send(base64.b64encode(password)+b'\r\n')

    # recv_auth = clientSocket.recv(1024)
    # print(recv_auth.decode())
    
    # Send MAIL FROM command and print server response.
    mailCommand = b'MAIL FROM:<yZhang5@mail.stmarytx.edu>\r\n'
    clientSocket.send(mailCommand)
    recv2 = clientSocket.recv(1024)
    print(recv2.decode())
    
    # Send RCPT TO command and print server response.
    rcpt_toCommand = b'RCPT TO <nz9024295@gmail.com>\n'
    clientSocket.send(rcpt_toCommand)
    recv3 = clientSocket.recv(1024)
    print(recv3.decode())
    
    