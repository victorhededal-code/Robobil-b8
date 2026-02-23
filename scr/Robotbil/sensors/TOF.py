# målinger
import time
from machine import Pin

values = []
gy53 = Pin(14, Pin.IN)  # Initialize GY-53 I2C pin
pwm_start = 0
pwm_stop = 0

def irq_init():
    gy53.irq(trigger=Pin.IRQ_RISING |Pin.IRQ_FALLING, handler = irq_handler)
def irq_handler(gy53):
    global pwm_start, pwm_stop
    if gy53.value() == 1:
        pwm_start = time.ticks_us()
    else:
        pwm_stop = time.ticks_us()
        cm = time.ticks_diff(pwm_stop, pwm_start) / 100
        values.append(cm)

def get_distance():
    global values
    temp_values = values[-1,-2,-3]
    temp_values.sort()
    values = temp_values
    return temp_values[1]
