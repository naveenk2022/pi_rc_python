# Introduction

This repository contains a guide to creating a "remote-controlled" car/buggy using a Raspberry Pi Zero 2 W, along with the Python scripts used to operate the car over SSH. 

# Components

- Raspberry Pi - Zero 2 W, along with a microSD card to flash the OS onto, along with **GPIO headers** soldered on to it.
- A power bank capable of providing 5V DC 2.5A power output.
- L298N DC Motor Controller Module.
- Four (4) 3-6V DC Motor.
- A rechargabale 12V 5200mAh battery/power supply.
- RC Car board to wire the motors/components to.

The motors are connected to the Pi via an L298N motor driver, through GPIO headers that were soldered on. 

With a 12V DC power supply, each L298N motor driver can power and communicate with 4 DC motors. 

![](images/l298n_module.jpg)

# Pin definitions

The following are the GPIO pin definitions for the L298N motor driver (assuming 2 motors are being powered):

**Motor 1**

IN1 = 22

IN2 = 27

EN-A = 17

**Motor 2**

IN3 = 13

IN4 = 19

EN-B = 26


