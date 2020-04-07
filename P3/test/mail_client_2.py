# Imports
import socket
import base64
import ssl
import time
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

#---------------------------------------------------------------------------
# Constants

RECV_LENGTH = 2084

#---------------------------------------------------------------------------
# Functions 

def check_for_error(recv):

    if type(recv) == bytes:
        recv = recv.decode('utf-8')

    recv = recv.strip()

    if recv[:3] == '220':
        print('220: Server ready -', recv[4:])

    elif recv[:3] == '250':
        print('250: Requested mail action okay completed')
    
    elif recv[:3] == '530':
        print("530: Authentication Problem -", recv[4:])

    elif recv[:3] == '550':
        print("550: Recipient email address does not exist")

    else:
        print(recv)

    return recv

#---------------------------------------------------------------------------
# Main Code

# Choose a mail server (e.g. Google mail server) and call it mailserver
# mailserver = ("stmp.gmail.com", 587)
mailserver = ("imap.gmail.com", 587) # or port 25

# Creating socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to server
client_socket.connect(mailserver)
check_for_error(client_socket.recv(RECV_LENGTH))

# Send HELO command and print server response.
client_socket.send('HELO Alice\r\n'.encode('utf-8'))
check_for_error(client_socket.recv(RECV_LENGTH))

# First must do STARTTLS command
# Help here: https://stackoverflow.com/questions/12593944/how-to-start-tls-on-an-active-connection-in-python
client_socket.send('STARTTLS\r\n'.encode('utf-8'))
check_for_error(client_socket.recv(RECV_LENGTH))
client_socket = ssl.wrap_socket(client_socket, ssl_version=ssl.PROTOCOL_SSLv23)

username = "davana1611@gmail.com"
#password = "Davalos_97!"
password = "qaqzsbxnqcajemkn" # App password: https://support.google.com/accounts/answer/185833?p=InvalidSecondFactor&visit_id=637217219295063725-2771767880&rd=1
# username = 'n359222435@gmail.com'
# password = 'fwrtnvaecypmvnne'

client_socket.send("AUTH LOGIN\r\n".encode('utf-8'))
client_socket.send(base64.b64encode(username.encode('utf-8'))+b'\r\n')
client_socket.send(base64.b64encode(password.encode('utf-8'))+b'\r\n')

check_for_error(client_socket.recv(RECV_LENGTH))

# Send MAIL FROM command and print server response.
mail_from = 'MAIL FROM:<davana1611@gmail.com>\r\n'

client_socket.send(mail_from.encode('utf-8'))
check_for_error(client_socket.recv(RECV_LENGTH))

# Send RCPT TO command and print server response.
mail_to = "RCPT TO:<davana1611@gmail.com>\r\n"

client_socket.send(mail_to.encode('utf-8'))
check_for_error(client_socket.recv(RECV_LENGTH))

# Send DATA command and print server response.
client_socket.send("DATA\r\n".encode('utf-8'))
check_for_error(client_socket.recv(RECV_LENGTH))

# Send message data.
msg = "\r\n I love computer networks \r\n"
subject = 'Subject: COMPUTER NETWORKING PROJECT 3\r\n\r\n'
date = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()) + "\r\n\r\n"

client_socket.send(subject.encode('utf-8'))
client_socket.send(date.encode('utf-8'))
client_socket.send(msg.encode('utf-8'))

r"""
# Sending an image - https://stackoverflow.com/questions/35963673/how-to-send-email-with-embedded-image-file-in-python-without-using-smtplib
email_contents = MIMEMultipart()
email_contents['Subject'] = 'CN - Image - Project 3'
email_contents['To'] = "<davalosaeduardo@gmail.com>"
email_contents['From'] = "<davana1611@gmail.com>"

# Text
text = MIMEText("I LOVE COMPUTER NETWORKS")
email_contents.attach(text)

# Image
fp = open(r"C:\Users\daval\Documents\COLLEGE\Graduate_Year_1\Spring_2020\Computer_Networking\ProgrammingProblems\p3\nocs_camera.png", 'rb')
image = MIMEImage(fp.read(), _subtype='.png')
fp.close()
image.add_header('Content-ID', '<camera.png>')
email_contents.attach(image)

# Sending an image END
client_socket.send(email_contents.as_bytes())

"""
# Message ends with a single period.
endmsg = "\r\n.\r\n"
client_socket.send(endmsg.encode('utf-8'))
check_for_error(client_socket.recv(RECV_LENGTH))

# Send QUIT command and get server response.
client_socket.send('QUIT\r\n'.encode('utf-8'))
check_for_error(client_socket.recv(RECV_LENGTH))
client_socket.close()