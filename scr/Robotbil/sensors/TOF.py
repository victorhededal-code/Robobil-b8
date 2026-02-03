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

    while cm < 20:
        motor.turn_right(80)
        time.sleep_ms(30)
        cm = measure()

    while cm <= 30 and cm > 20:
        print(" too close")
        motor.turn_right(80)
        time.sleep_ms(30)
        motor.move_forward(70)
        time.sleep_ms(10)
        cm = measure()

    while cm > 60:
        motor.move_forward(60)
        time.sleep_ms(15)
        motor.turn_left(100)
        time.sleep_ms(100)
        cm = measure()

    while 40 <= cm:
        print(" too far away")
        motor.turn_left(80)
        time.sleep_ms(30)
        motor.move_forward(80)
        time.sleep_ms(10)
        cm = measure()

    while cm < 40 and cm > 30:
        print(" move along the wall")
        motor.move_forward(100)
        cm = measure()


