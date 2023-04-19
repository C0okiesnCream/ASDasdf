# ----------------------------------------------------------------------------- #
#                                                                               #             
# 	Project:        drivetrain1 Sensing                                          #
#   Module:         main.py                                                     #
#   Author:         VEX                                                         #
#   Created:        Fri Aug 05 2022                                             #
#	Description:    This example will show all of the available commands        #
#                   for using the drivetrain1                                    #
#                                                                               #                                                                          
#   Configuration:  V5 Speedbot (drivetrain1 2-motor, No Gyro)                   #
#                                                                               #                                                                          
# ----------------------------------------------------------------------------- #

# Library imports
from vex import *
import random

# Brain should be defined by default
brain=Brain()

# Begin project code
while True:


    # Clear the screen and set the cursor to top left corner on each loop
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)

  
    # A brief delay to allow text to be printed without distortion or tearing
    wait(100,MSEC)
    
