#Importing modules
from machine import Pin
from movement import motor

# setting the pin for the Reflection sensor 
REF_sens = Pin(15, Pin.IN)  # Initialize pin
box = False
sumo = False

def irq_init():
    REF_sens.irq(trigger=Pin.IRQ_RISING, handler = irq_handler)

def sumo_init(state):
    global sumo
    if state:
        sumo = True
    else:
        sumo = False

def irq_handler(REF_sens):
    global box, sumo
    if sumo:
        box = False
        motor.stop_motors()
    else:
        pass

def found_box():
    global box
    box = True
def check_box():
    global box
    return box

def reset_ref():
    global box
    box = False