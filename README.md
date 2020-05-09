# Car-Control-microsoft-joystick
The repository contains code for controlling RC car with Microsoft Flight Simulator Joystick

This program enables the user to control and RC Car having Raspberry pi zero w to be controlled using the joystick
The communication medium for both the remote system and the RC Car is Wifi. 

The protocol used for connection in TCP as it is connection-oriented and thus best for handling drop packet as each packet is acknowledged.

## Requirement :
Libraries Requirement:

socket
numpy
threading 
os
subprocess
matplotlib
time

## Backend Software used 
JSTEST
https://jstest-gtk.gitlab.io/


# Execution
### Server 
python ./tcp_joystic_comm.py

# Client
python ./tcp_client.py

#Testing
