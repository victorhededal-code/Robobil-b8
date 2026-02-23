#Importing modules
import time
from machine import Pin
from movement import motor

# setting the pin for the Reflection sensor 
REF_sens = Pin(15, Pin.IN)  # Initialize pin
box = False


def irq_init():
    REF_sens.irq(trigger=Pin.IRQ_RISING, handler = irq_handler)
def irq_handler():
    global box
    box = False
def found_box():
    global box
    box = True
def check_box():
    global box
    return box

def reset():
    global box
    box = False