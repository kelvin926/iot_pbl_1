import RPi.GPIO as GPIO # import GPIO library
import time # import time library

GPIO.setmode(GPIO.BCM) # Assigning GPIO pin number by connector pin

pin_num=18
# define a variable from 0~100 to represent the duty cycle
dc=[0,1,2,3,4,5,6,7,8,9,10,12,1,15,20,30,50,70,100] 

# pin_num to be assinged as output pin, initial output to be LOW level
GPIO.setup(pin_num, GPIO.OUT, initial=GPIO.LOW)

# Create an PWM instance
p=GPIO.PWM(pin_num, 100) # 100 Hz

# start from 0% of DC 
p.start(0)
try: # Start Try/Exception
	while 1: # Infinite loop
		for val in dc: # iterate for loop over the list defined with dc
			p.ChangeDutyCycle(val) # set duty cycle
			time.sleep(0.1) # delay 0.1 sec
		dc.reverse() # reverse the order 
		time.sleep(0.1) # delay 0.1 sec

except KeyboardInterrupt: # Detect exception condition
	pass

p.stop()
GPIO.cleanup() # GPIO open
