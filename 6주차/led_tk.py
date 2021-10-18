# GPIO library
import RPi.GPIO as GPIO
# Tkinter library: GUI
import Tkinter

GPIO.setmode(GPIO.BOARD) # Assigning GPIO pin number by connector pin
pin_num=11 

GPIO.setup(pin_num, GPIO.OUT, initial=GPIO.LOW)
# pin_num to be assinged as output pin, initial output to be LOW level

def func(): # Defining a function to turn on/off LED
	GPIO.output(pin_num, not GPIO.input(pin_num)) 
	# Output: the opposite of current state from pin_num
	
root = Tkinter.Tk() # an instance of Tkinter
label=Tkinter.Label(root, text='press button') # create label on the dialog
label.pack() # allocate the label using pack

button=Tkinter.Button(root, text='LED', command=func) # create button
button.pack() # allocate the button using pack
root.mainloop() # present root on the screen

GPIO.cleanup()
