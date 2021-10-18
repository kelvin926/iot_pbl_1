import time # time lbrary import
import RPi.GPIO as GPIO # GPIO lbrary import

GPIO.setmode(GPIO.BOARD) # Assigning GPIO pin number by connector pin

pin_num=8 # Which pin number to assign
myinterval=1 # second

GPIO.setup(pin_num, GPIO.OUT, initial=GPIO.LOW) 
# pin_num to be assinged as output pin, initial output to be LOW level

try: # Start Try/Exception
    while 1: # Infinite loop
        GPIO.output(pin_num, GPIO.HIGH) # Output HIGH level
        time.sleep(myinterval) # Stand by 
        
        GPIO.output(pin_num, GPIO.LOW) # Output LOW level
        time.sleep(myinterval) # Stand by 
except KeyboardInterrupt: # Detect exception condition
    print("\nInterrupted!") # Print what happend
    pass

finally:
    GPIO.cleanup() # GPIO open
