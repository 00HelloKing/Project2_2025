# Agile Rasberry Pi Plant Moisture Sensor with Email Notification
# It combined the function that uses check water from soil with function that sends emails to inform the user the plant need to be watered
# Name: Jin Kaifeng
# Student ID: 202283890029
# Semester Project 3  &  Grade 3
# Date: 20/4/25

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

# Create an array to save the history information about watering
history = []

# Create a funtion about sending email
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
# The checking time in a day
    if current_hour in [10, 13, 16, 19]:
        if GPIO.input(channel):
            send_email("HEY! You need to water me!")
        else:
            send_email("HAHA! Water is enough. Don't water me!")

# Wait for 1 hour to avoid repetition
        time.sleep(3600)  
# Check every minute
    time.sleep(60)  
