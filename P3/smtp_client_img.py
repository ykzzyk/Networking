import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def SendMail(img):
    # Open the image, and load the image data
    img_data = open(img, 'rb').read()
    
    # Use the MIMEMultipart module for message
    msg = MIMEMultipart()
    # Configuration
    msg['Subject'] = "SMTP client project - send image"
    msg['From'] = 'n359222435@gmail.com'
    msg['To'] = 'nz9024295@gmail.com'

    # attach the text
    text = MIMEText('I love computer networks!\n\n\n')
    msg.attach(text)
    
    # attach the image
    image = MIMEImage(img_data, name=os.path.basename(img))
    msg.attach(image)

    # Connect to the google server, Use SSL
    s = smtplib.SMTP_SSL('imap.gmail.com', 465)
    
    # Login to the google server, the password is the google APP password
    s.login("n359222435@gmail.com", "fwrtnvaecypmvnne")
    
    # Send email
    s.sendmail(
        "n359222435@gmail.com", 
        ["nz9024295@gmail.com"],
        msg.as_string()
    )
    
    # Quit
    s.quit()
    
if __name__ == '__main__':
    SendMail('5.pgm')