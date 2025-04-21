# Rasberry Pi Plant Moisture Sensor
# It can check if there is water from soil
# Name: Jin Kaifeng
# Student ID: 202283890029
# Semester Project 3  &  Grade 3
# Date: 20/4/25

import RPi.GPIO as GPIO
import time

# GPIO setup
channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

# show information about watering
def callback(channel):
	if GPIO.input(channel):
		print("Water Not Detected")
	else:
		print("Water Detected")

# Let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(channel, GPIO.BOTH,bouncetime=300)

# Assign function to GPIO PIN,Run function on change
GPIO.add_event_callback(channel, callback)

# Infinite loop
while True:
	time.sleep(0)
