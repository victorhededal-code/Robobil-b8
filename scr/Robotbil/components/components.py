from machine import Pin, PWM
from time import sleep

def set_pins(pinin1, pinin2, enable):
    frequency = 1000
    pin1 = Pin(pinin1, Pin.OUT)
    pin2 = Pin(pinin2, Pin.OUT)
    enable = PWM(Pin(enable), frequency)

    return



# Set min duty cycle (15000) and max duty cycle (65535)
# dc_motor = DCMotor(pin1, pin2, enable, 15000, 65535)




#højre_motor

#venstre_motor

#tof_sensor

#refleksion_sensor




