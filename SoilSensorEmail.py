import RPi.GPIO as GPIO
import smtplib
from email.message import EmailMessage
import time
from datetime import datetime

# Set GPIO
channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

# Set email
from_email_addr = "2924827477@qq.com"
from_email_pass = "pgcqojtevblxdcfh"
to_email_addr = "jkf1018407510@163.com"
smtp_server = "smtp.qq.com"
smtp_port = 587

history = []

def send_email(status):
    msg = EmailMessage()
    body = f"The plant's status: {status}\ntime: {datetime.now()}"
    msg.set_content(body)
    msg['From'] = from_email_addr
    msg['To'] = to_email_addr
    msg['Subject'] = 'Report for my plant'
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_email_addr, from_email_pass)
    server.send_message(msg)
    server.quit()
    history.append(body)
# Save 3 days * 4 times
    if len(history) > 12: 
        history.pop(0)

while True:
    current_hour = datetime.now().hour
# chect time in a day
    if current_hour in [10, 13, 16, 19]:
        if GPIO.input(channel):
            send_email("Water Not detected")
        else:
            send_email("Water  detected")
# wait for 1 hour to avoid repetition
        time.sleep(3600)  
# Chect every minute
    time.sleep(60)  
