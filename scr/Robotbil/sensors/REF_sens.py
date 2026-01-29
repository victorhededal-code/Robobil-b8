# målinger

# målinger
import time
from machine import Pin

REF_sens = Pin(15, Pin.IN)  # Initialize GY-53 I2C pin


def ref_measure(readout=False) -> int:
    """measure with UV sensor and returns 0 if it cant find a measurement back"""
    while REF_sens.value():  # Wait for the GY-53 to become ready
        # print("Waiting for GY-53 to become ready...")
        pass
    while not REF_sens.value():  # Read the GY-53 data
        # print("Reading GY-53 data...")
        pass
    #starttime = time.ticks_us()
    while REF_sens.value():  # Wait for the GY-53 to finish reading
        # print("Waiting for GY-53 to finish reading...")
        pass
    meas = REF_sens.value()
    #endtime = time.ticks_us()
    # To get distance in mm, use (endtime - starttime) / 10
    #cm = (endtime - starttime) / 10
    if readout:
        print("measurement gained: ", meas)

    return meas


while True:
    ref_measure(True)
    time.sleep_ms(100)


