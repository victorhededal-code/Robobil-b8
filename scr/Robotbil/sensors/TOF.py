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
    if cm == 1:
        motor.stop_motors()

    while cm < 10:
        motor.turn_right(75)
        time.sleep_ms(50)
        cm = measure()

    while cm <= 20 and cm > 10:
        print(" too close")
        motor.turn_right(50)
        time.sleep_ms(50)
        motor.move_forward(25)
        cm = measure()

    while cm > 50:
        motor.move_forward(50)
        time.sleep_ms(100)
        motor.turn_left(50)
        time.sleep_ms(100)
        cm = measure()

    while 30 <= cm:
        print(" too far away")
        motor.turn_left(50)
        time.sleep_ms(50)
        motor.move_forward(50)
        cm = measure()

    while cm < 30 and cm > 20:
        print(" move along the wall")
        motor.move_forward(100)
        cm = measure()

    if cm < 10:
        motor.turn_right(100)

    elif cm <= 20:
        print(" too close")
        motor.turn_right(50)
        motor.move_forward(25)

    elif cm > 50:
        motor.move_forward(50)
        time.sleep_ms(100)
        motor.turn_left(50)

    elif 30 <= cm:
        print(" too far away")
        motor.turn_left(50)
        motor.move_forward(50)

    else:
        print(" move along the wall")
        motor.move_forward(100)