#Importing modules
import time
from machine import Pin

# setting the pin for the Reflection sensor 
REF_sens = Pin(15, Pin.IN)  # Initialize pin


def ref_measure(readout=False) -> int:
    """measure with UV sensor and returns 0 if it cant find a measurement back"""
    #while REF_sens.value():  # Wait for the sensor to become ready
        #pass

    #while not REF_sens.value():  # Read the sensor data
        #pass

    #while REF_sens.value():  # Wait for the GY-53 to finish reading
        #pass
    
    meas = REF_sens.value()
    #endtime = time.ticks_us()
    # To get distance in mm, use (endtime - starttime) / 10
        #cm = (endtime - starttime) / 10
    if readout:
        print("measurement gained: ", meas)

    return meas




