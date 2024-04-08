# Introduction

This repository contains python scripts to operate the Pi RC car v1.0, a rudimentary implementation of a remotely controlled "RC" car, running on a single Raspberry Pi Zero 2 W.

# Components

- Raspberry Pi - Zero 2 W
- A power bank capable of up to 3A of power output
- L298N DC Motor Controller Module
- Four (4) 3-6V DC Motor
- A rechargabale 12V 5200mAh battery/power supply
- RC Car board to wire the motors/components to

The motors are connected to the Pi via an L298N motor driver, through GPIO headers that were soldered on. 

With a 12V DC power supply, each L298N motor driver can power and communicate with 2 DC motors. 

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


