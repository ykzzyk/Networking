import smtplib
import datetime

server = smtplib.SMTP_SSL('imap.gmail.com', 465)
server.login("n359222435@gmail.com", "fwrtnvaecypmvnne")

# For the message
from_addr = "n359222435@gmail.com"
to_addr = "nz9024295@gmail.com"
subject = "SMTP client project"
date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )
body = 'I love computer networks!\n'

msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( from_addr, to_addr, subject, date, body)

server.sendmail(
  "n359222435@gmail.com", 
  ["nz9024295@gmail.com"],
  msg)
server.quit()