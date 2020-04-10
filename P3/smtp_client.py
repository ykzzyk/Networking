# Import modules
import smtplib
import datetime

# Connect to the google server, Use SSL
server = smtplib.SMTP_SSL('imap.gmail.com', 465)

# Login to the google server, the password is the google APP password
server.login("n359222435@gmail.com", "fwrtnvaecypmvnne")

# Configuration for the message
from_addr = "n359222435@gmail.com"
to_addr = "nz9024295@gmail.com"
subject = "SMTP client project"
date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )
body = 'I love computer networks!\n'

msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( from_addr, to_addr, subject, date, body)

# Send email
server.sendmail(
  "n359222435@gmail.com", 
  ["nz9024295@gmail.com"],
  msg)

# Quit
server.quit()