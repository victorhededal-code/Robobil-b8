from math import pi
from machine import Pin

hall_right = Pin( 12, Pin.IN ) 
hall_left = Pin( 13, Pin.IN )

left_counter = 0
right_counter = 0 

#############################################################
# Init for hall sensor left and right IRQ 
#############################################################
def irq_hall_left_init():
    hall_left.irq( handler = left_irq_counter,trigger = Pin.IRQ_RISING )
    
def irq_hall_right_init():
    hall_right.irq(handler = right_irq_counter, trigger = Pin.IRQ_RISING )


#############################################################
# Handlers for hall left and right 
#############################################################
def left_irq_counter( hall_left ):
    global left_counter
    if hall_left.value() == 1:
        left_counter += 1

def right_irq_counter( hall_right ):
    global right_counter 
    if hall_right.value() == 1:
        right_counter += 1


##############################################################
# Calculate speed in meters pr second / mps 
#
#
# TODO
# Get and get the diameter of the wheels and replace foo with them
# Set a fixed timer with interupts to 100 ms to calculate rpm 
##############################################################
def calc_speed():
    global left_counter, right_counter
    left_rpm = (left_counter * 5) * 60
    left_counter = 0
    right_rpm = (right_counter * 5) * 60
    right_counter = 0 

    left_speed = left_rpm * pi * 6 / 100 / 60 # left wheels speed in mps 
    right_speed = right_rpm * pi * 6 / 100 / 60 # right wheels speed in mps 
    
    speed = (right_speed + left_speed) / 2 # speed in mps 
    return speed 

 #############################################################
 # timer for interupts 
 #############################################################






