
# Importing libraries
import RPi.GPIO as GPIO          
from time import sleep
import socket
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

## Setting up a TCP connection
tcp1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_ip = "192.168.0.147"
port = 9000
buffer_size = 1024

tcp1.connect((tcp_ip, port))


while True:

    data = tcp1.recv(buffer_size).decode('utf-8')  # Receive response from server
    
    if data == "":
        GPIO.cleanup()
        tcp1.close()
        break 
    print("Data received from server:", data)  # Print response from server
   # The FORWARD command
    if data=='w':
         # Running Motor 1
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
         # Running Motor 2
         GPIO.output(in3,GPIO.HIGH)
         GPIO.output(in4,GPIO.LOW)

    # The REVERSE command
    if data=="s":
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        # Reversing Motor 2
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.HIGH)
    # The STOP command
    elif data=='stop':
        # Stopping Motor 1
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        # Stopping Motor 2
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)
    # The LEFT command
    elif data=='a':
        # Running Motor 1
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        # Running Motor 2
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
    # The RIGHT command
    elif data=='d':
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        # Running Motor 2
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH) 
    # Speed HIGH
    elif data=='h':
        p.ChangeDutyCycle(75)
        q.ChangeDutyCycle(75)
    # The EXIT command
    elif data=='exit':
        GPIO.cleanup()
        break
GPIO.cleanup()
