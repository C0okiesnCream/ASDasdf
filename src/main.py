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

# Robot configuration code
left_drive_smart1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_drive_smart1 = Motor(Ports.PORT11, GearSetting.RATIO_18_1, True)
drivetrain1 = DriveTrain(left_drive_smart1, right_drive_smart1, 319.19, 295, 40, MM, 1)
left_drive_smart2 = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
right_drive_smart2 = Motor(Ports.PORT12, GearSetting.RATIO_18_1, True)
drivetrain2 = DriveTrain(left_drive_smart2, right_drive_smart2, 319.19, 295, 40, MM, 1)
optical = Optical(Ports.PORT15)
distance = Distance(Ports.PORT19)

#drivetrain merge functions
def drivetrainsTurn(dir, speed):
    '''first var: direction,
    values: LEFT, RIGHT
    
    second var speed, 
    values: any int 1-100, measured as percentage'''
    drivetrain1.turn(dir, speed, PERCENT)
    drivetrain2.turn(dir, speed, PERCENT)

def drivetrainsDrive(dir, speed):
    '''first var: direction, 
    values: FORWARD, REVERSE
    
    second var: speed, 
    values: any int 1-100, measured as percentage'''
    drivetrain1.drive(dir, speed, PERCENT)
    drivetrain2.turn(dir, speed, PERCENT)

# Begin project code
count = 0
leftTurn = 0
rightTurn = 0
optical.set_light_power(25)
optical.set_light(True)
drivetrain1.set_stopping(BRAKE)

# Print all drivetrain1 sensing values to the screen in an infinite loop
while True:
    randfloat = random.random()
    objectDistance = float(str(distance.object_distance(MM)))
    hue = float(str(optical.hue()))
    if objectDistance <= 250 or leftTurn > 0 or rightTurn > 0:
        if hue >= 335 and (leftTurn > 0 or rightTurn > 0) == False:
            pass
        else:
            if leftTurn > 0:
                drivetrain1.turn(LEFT, 50, PERCENT)
                drivetrain2.turn(LEFT, 50, PERCENT)
                leftTurn += 1
            elif rightTurn > 0:
                drivetrain1.turn(RIGHT, 50, PERCENT)
                drivetrain2.turn(RIGHT, 50, PERCENT)
                rightTurn += 1
            else:
               if  bool(randfloat > 0.5):
                   drivetrain1.turn(LEFT, 50, PERCENT)
                   drivetrain2.turn(LEFT, 50, PERCENT)
                   leftTurn += 1
               else:
                   drivetrain1.turn(RIGHT, 50, PERCENT)
                   drivetrain2.turn(RIGHT, 50, PERCENT)
                   rightTurn += 1
            
    else:
        drivetrain1.drive(FORWARD, 50, PERCENT)
        drivetrain2.drive(FORWARD, 50, PERCENT)
    
    if rightTurn or leftTurn > 25:
        rightTurn = 0
        leftTurn = 0

    # Clear the screen and set the cursor to top left corner on each loop
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)

    brain.screen.print("Velocity:", drivetrain1.velocity(PERCENT), "   TurningLeft:", (leftTurn > 0))
    brain.screen.next_row()

    brain.screen.print("Current:", drivetrain1.current(CurrentUnits.AMP), "   TurningRight:", (rightTurn > 0))
    brain.screen.next_row()

    brain.screen.print("Power:", drivetrain1.power(PowerUnits.WATT), "      RandFloat:", randfloat)
    brain.screen.next_row()

    brain.screen.print("Torque:", drivetrain1.torque(TorqueUnits.NM), "    returningFalse:", (randfloat > 0.5))
    brain.screen.next_row()

    brain.screen.print("Efficiency:", drivetrain1.efficiency(PERCENT))
    brain.screen.next_row()

    brain.screen.print("Temperature:", drivetrain1.temperature())
    brain.screen.next_row()

    brain.screen.print("Count: " + str(count))
    brain.screen.next_row()

    brain.screen.print("color:", str(optical.color()))
    brain.screen.next_row()

    brain.screen.print("hue:", str(optical.hue()))
    brain.screen.next_row()

    brain.screen.print("brightness:", str(optical.brightness()))
    brain.screen.next_row()

    brain.screen.print("distance(mm):", str(distance.object_distance(MM)))
    brain.screen.next_row()

  
    # A brief delay to allow text to be printed without distortion or tearing
    wait(100,MSEC)
    
