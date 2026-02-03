# målinger
import time
from machine import Pin
from movement import motor

gy53 = Pin(14, Pin.IN)  # Initialize GY-53 I2C pin


def measure(readout=False) -> int:
    """measures the distance with the GY-53 sensor and returns the measurement in CM"""
    while gy53.value():  # Wait for the GY-53 to become ready
        # print("Waiting for GY-53 to become ready...")
        pass
    while not gy53.value():  # Read the GY-53 data
        # print("Reading GY-53 data...")
        pass
    starttime = time.ticks_us()
    while gy53.value():  # Wait for the GY-53 to finish reading
        # print("Waiting for GY-53 to finish reading...")
        pass
    endtime = time.ticks_us()
    # To get distance in mm, use (endtime - starttime) / 10
    cm = (endtime - starttime) / 100
    if readout:
        print("Time elapsed: ", cm, "cm")

    return cm


def give_command(cm):
    """gives the command to the robot"""

    if cm <= 5:
        print(" too close")
        motor.turn_right()
        motor.move_forward()


    elif 10 <= cm:
        print(" too far away")
        motor.turn_left()
        motor.move_forward()


    else:
        print(" move along the wall")
        motor.move_forward()