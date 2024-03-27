# Importing libraries
import RPi.GPIO as GPIO          
from time import sleep

# Defining the GPIO pin connections
# Motor 1
in1 = 22
in2 = 27
ena = 17

# Motor 2
in3 = 13
in4 = 19
enb = 26


temp1=1

# Setting up Motor 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(ena,1000)
p.start(25)

# Setting up Motor 2
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
q=GPIO.PWM(enb,1000)
q.start(25)

# Defining Button Presses
print("\n")
print("Default motor speed: LOW (25)")
print("\n")
print("Default motor direction: FORWARD")
print("\n")
print("Press the following buttons to change directions as follows:")
print("\n")
print("r-RUN s-STOP f-FORWARD b-BACKWARD")
print("\n")
print("Press the following buttons to change the motor speed:")
print("\n")
print("l-LOW(25) m-MEDIUM(50) h-HIGH(100)")
print("\n") 
print("Press 'e' before exiting the script to clear the pin outputs.")
print("\n") 
while(1):

    x=input()
    
    if x=='r':
        print("Running......Moving FORWARD at speed LOW")
        if(temp1==1):
         # Running Motor 1
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
         # Running Motor 2
         GPIO.output(in3,GPIO.HIGH)
         GPIO.output(in4,GPIO.LOW)
         print("Moving FORWARD.....")
         x='z'
        else:
         # Running Motor 1
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.HIGH)
         # Running Motor 2
         GPIO.output(in3,GPIO.LOW)
         GPIO.output(in4,GPIO.HIGH)
         print("Moving BACKWARDS.....")
         x='z'


    elif x=='s':
        print("STOPPING all motors.....")
        # Stopping Motor 1
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        # Stopping Motor 2
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)
        x='z'

    elif x=='f':
        print("Moving FORWARD.....")
        # Running Motor 1
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        # Running Motor 2
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='b':
        print("Moving BACKWARDS.....")
        # Reversing Motor 1
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        # Reversing Motor 2
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.HIGH)
        temp1=0
        x='z'

    elif x=='l':
        print("Changing speed to LOW.....")
        p.ChangeDutyCycle(25)
        q.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        print("Changing speed to MEDIUM.....")
        p.ChangeDutyCycle(50)
        q.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        print("Changing speed to HIGH.....")
        p.ChangeDutyCycle(75)
        q.ChangeDutyCycle(75)
        x='z'
     
    
    elif x=='e':
        print("Clearing GPIO pin outputs.....")
        GPIO.cleanup()
        break
    
    else:
        print("<<< Input not valid  >>>")
        print("Press the designated keys to continue.....")
