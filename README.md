# Introduction

This repository contains python scripts to operate the Pi RC car v1.0, a rudimentary implementation of a remotely controlled "RC" car, running on two Pi Zero 2 Ws.

The motors are connected to the Pi via an L298N motor driver, through GPIO headers that were soldered on. 

With a 12V DC power supply, each L298N motor driver can power and communicate with 2 DC motors. 

# Pin definitions

The following are the GPIO pin definitions for the L298N motor driver (assuming 2 motors are being powered):

**Motor 1**

in1 = 22
in2 = 27
ena = 17

**Motor 2**
in3 = 13
in4 = 19
enb = 26


