#!/usr/bin/python3
#Author: Brayden Karnes
#Date: 11/19/21
#Description: Python script for sending text messages using gmail servers.

import smtplib
class sms:

    def send(message, number, carrier):
        carriers = {
            'att':'@mms.att.net',
            'tmobile':'@tmomail.net',
            'verizon':'@vtext.com',
            'sprint':'@page.nextel.com'
            }

        recipient = (f'{number}{carriers[carrier]}')
        auth = ('<INSERT EMAIL ADDRESS HERE>','<PASSWORD LINK HERE>')

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(auth[0], auth[1])

        server.sendmail(auth[0], recipient, message)
    

