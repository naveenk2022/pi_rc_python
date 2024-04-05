# Importing libraries
import RPi.GPIO as GPIO
from time import sleep
import pygame
import sys
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


# Initialize Pygame
pygame.init()

from pygame.locals import *

windowSurfaceObj = pygame.display.set_mode((100,100))

# creating a running loop
while True:
       
    # creating a loop to check events that 
    # are occurring
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         
        # key PRESS
        if event.type == pygame.KEYDOWN:
               
            # Key "W"- FORWARD
            if event.key == pygame.K_w:
               GPIO.output(in1,GPIO.HIGH)
               GPIO.output(in2,GPIO.LOW)
               # Running Motor 2
               GPIO.output(in3,GPIO.HIGH)
               GPIO.output(in4,GPIO.LOW)

            # Key "A" - LEFT
            if event.key == pygame.K_a:
                # Running Motor 1
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.HIGH)
                # Running Motor 2
                GPIO.output(in3,GPIO.HIGH)
                GPIO.output(in4,GPIO.LOW)

            # Key "S" - REVERSE
            if event.key == pygame.K_s:
                # Reversing Motor 1
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.HIGH)
                # Reversing Motor 2
                GPIO.output(in3, GPIO.LOW)
                GPIO.output(in4, GPIO.HIGH)

            # Key "D" - RIGHT
            if event.key == pygame.K_d:
                # Running Motor 1
                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)
                # Running Motor 2
                GPIO.output(in3,GPIO.LOW)
                GPIO.output(in4,GPIO.HIGH)
            # Key "E" - EXIT
            if event.key == pygame.K_e:
                GPIO.cleanup()
                break
            # Key "H" - HIGH
            if event.key == pygame.K_h:
                p.ChangeDutyCycle(75)
                q.ChangeDutyCycle(75)


        # Key RELEASED
        elif event.type == pygame.KEYUP:
            # Stopping Motor 1
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            # Stopping Motor 2
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4, GPIO.LOW)
