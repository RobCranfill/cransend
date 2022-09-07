#!/usr/bin/python3

# @author robcranfill@robcranfill.net
#  with much thanks to https://www.bc-robotics.com/tutorials/sending-email-using-python-raspberry-pi/
#
# Syntax:
#   {this thing} [-s {subject}] {to address} 
# (a very small subset of https://www.commandlinux.com/man-page/man1/Mail.1.html )
#
# Pipe message body from input.
#
# TODO: --from? (will that work?)

import getopt
import os
import smtplib
import sys


# Email Variables
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT   = 587
GMAIL_USERNAME = 'robcranfill@gmail.com'
GMAIL_PASSWORD = 'XXXXXXXXXXXXXXXX' # special gmail "app password"

class Emailer:
    def sendmail(self, recipient, subject, content):
 
        # Create Headers
        headers = ["From: " + GMAIL_USERNAME, "Subject: " + subject, "To: " + recipient,
                   "MIME-Version: 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)

        # Connect to Gmail server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()
 
        # Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
 
        # Send email and exit
        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        session.quit


# Here we go....

def main(argv):
    sender = Emailer()
    
    usageString = "Usage: " + os.path.basename(__file__) + " [-s|--subject {subject}] to-addr"

    subject = "(no subject)"
    sendTo = ""

    try:
      opts, args = getopt.getopt(argv, "hs:", ["subject="])
    except getopt.GetoptError:
      print(usageString)
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print(usageString)
         sys.exit()
      elif opt in ("-s", "--subject"):
         subject = arg

    if len(args) != 1:
        print("exactly one to-addr, please!")
        print(usageString)
        sys.exit()
    sendTo = args[0]

    if not sendTo:
        print("to-addr is required!")
        print(usageString)
        sys.exit()
    
    dryRun = False
    if dryRun:
        print("dry run:")
        print(' To:', sendTo)
        print(' Subject:', subject)
        print(' len(args)', len(args))
        sys.exit(666)

 
    content = ""
    for line in sys.stdin:
        content += line
    

    # Send it!
    sender.sendmail(sendTo, subject, content)  


if __name__ == "__main__":
   main(sys.argv[1:])
