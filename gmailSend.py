# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 11:01:56 2017
Script to send mails thorugh Gmail using smtplib
"""

import smtplib
# Connecting to an SMTP Server
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

# Sending the SMTP “Hello” Message
smtpObj.ehlo()

# Starting TLS Encryption
smtpObj.starttls()

# Logging in to the SMTP Server
smtpObj.login('your_gmail_id', 'your_gmail_password')

# Sending an Email
smtpObj.sendmail('your_gmail_id', 'receiver_gmail_id', 
'Subject: Data Science, Machine Learning & Coding Interview Questions \
\nMessage to be sent with the mail')

# Disconnecting from the SMTP Server
smtpObj.quit()