#!/usr/bin/env python
#coding: utf8

import RPi.GPIO as GPIO

# Initialize how to count the pins
GPIO.setmode(GPIO.BCM)

# Print GPIO usage as message
GPIO.setwarnings(False)
print("Warning: GPIO2 in use!")

# Set pin 2 as output
GPIO.setup(2, GPIO.OUT)

# Read GPIO value for decision
value = GPIO.input(2)

# Output turn fan on/off
if value == 0:
	GPIO.output(2, GPIO.HIGH)
	print("Status: Fan active")
elif value == 1:
	GPIO.output(2, GPIO.LOW)
	print("Status: Fan inactive")
else:
	print("Error: No initial value set")

exit()
