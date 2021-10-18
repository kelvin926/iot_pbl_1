# GPIO library
import RPi.GPIO as GPIO
# Tkinter library: GUI
import time

GPIO.setmode(GPIO.BCM) # Assigning GPIO pin number by connector pin
pin_num_LED=18
pin_num_switch=23

GPIO.setup(pin_num_LED, GPIO.OUT, initial=GPIO.LOW)
# pin_num to be assinged as output pin, initial output to be LOW level
GPIO.setup(pin_num_switch, GPIO.IN)
#GPIO.setup(pin_num_switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	while 1:
		key_in = GPIO.input(pin_num_switch)
		if key_in==0: # If switch is open, LOW
			GPIO.output(pin_num_LED, GPIO.LOW)
		else: # If switch is closed, HIGH
			GPIO.output(pin_num_LED, GPIO.HIGH)

except KeyboardInterrupt:
	pass

GPIO.cleanup()