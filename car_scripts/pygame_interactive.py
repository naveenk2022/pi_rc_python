# Importing libraries
import RPi.GPIO as GPIO
from time import sleep
import pygame
import sys
import os
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
p.start(50)

# Setting up Motor 2
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
q=GPIO.PWM(enb,1000)
q.start(50)


# Initialize Pygame
pygame.display.init()
pygame.font.init() 
# Set up the screen (you won't actually see it, but Pygame requires it)
window = pygame.display.set_mode((640,480))
pygame.display.set_caption("KushWagen v1.0")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up font
font = pygame.font.SysFont(None, 40)

# Defining a text function
# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define font
font = pygame.font.Font(None, 36)

def render_text():
    window.fill(WHITE)  # Fill the screen with white color

    # Render text
    text = [
        "W - Move Forward",
        "A - Turn Left",
        "S - Turn Right",
        "D - Reverse",
        "Press H to increase speed!",
        "Press M to decrease speed.",
        "Press E to exit."
    ]

    # Display text on the screen
    y_offset = 100
    for line in text:
        rendered_text = font.render(line, True, BLACK)
        window.blit(rendered_text, (50, y_offset))
        y_offset += 50

    pygame.display.flip()  # Update the display


# creating a running loop
while True:
    render_text()
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

            # Key "M" - MEDIUM
            if event.key == pygame.K_h:
                p.ChangeDutyCycle(50)
                q.ChangeDutyCycle(50)

        # Key RELEASED
        elif event.type == pygame.KEYUP:
            # Stopping Motor 1
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            # Stopping Motor 2
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4, GPIO.LOW)
