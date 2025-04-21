# Email Notification
# It sends emails to inform the user with SMTP
# Name: Jin Kaifeng
# Student ID: 202283890029
# Semester Project 3  &  Grade 3
# Date: 20/4/25

import smtplib
from email.message import EmailMessage

# from and to email
from_email_addr = "2924827477@qq.com"
from_email_pass = "pgcqojtevblxdcfh"
to_email_addr = "jkf1018407510@163.com"

msg = EmailMessage()
body = "Hello from Raspberry Pi"
msg.set_content(body)
msg['From'] = from_email_addr
msg['To'] = to_email_addr
# The subject of emails
msg['Subject'] = 'TEST EMAIL'

# the port
server = smtplib.SMTP('smtp.qq.com', 587)  
server.starttls()
server.login(from_email_addr, from_email_pass)
server.send_message(msg)
print('Email sent')
# quit the server
server.quit()
