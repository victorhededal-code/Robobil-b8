# målinger
import time
from machine import Pin

values_wall = []
gy53_wall = Pin(14, Pin.IN)  # Initialize GY-53 I2C pin
pwm_start_wall = 0
pwm_stop_wall = 0
####################################
###             Wall             ###
####################################
def irq_init_wall():
    gy53_wall.irq(trigger=Pin.IRQ_RISING |Pin.IRQ_FALLING, handler = irq_handler_wall)
def irq_handler_wall(gy53_wall):
    global pwm_start_wall, pwm_stop_wall
    if gy53_wall.value() == 1:
        pwm_start_wall = time.ticks_us()
    else:
        pwm_stop_wall = time.ticks_us()
        cm_wall = time.ticks_diff(pwm_stop_wall, pwm_start_wall) / 100
        values_wall.append(cm_wall)

def get_distance_wall():
    global values_wall
    temp_values_wall = values_wall[:-3]
    temp_values_wall.sort()
    values_wall = temp_values_wall
    return temp_values_wall[1]
####################################
###             Sumo             ###
####################################

values_sumo = []
gy53_sumo = Pin(26, Pin.IN)  # Initialize GY-53 I2C pin
pwm_start_sumo = 0
pwm_stop_sumo = 0

def irq_init_sumo():
    gy53_sumo.irq(trigger=Pin.IRQ_RISING |Pin.IRQ_FALLING, handler = irq_handler_sumo)
def irq_handler_sumo(gy53_sumo):
    global pwm_start_sumo, pwm_stop_sumo
    if gy53_sumo.value() == 1:
        pwm_start_sumo = time.ticks_us()
    else:
        pwm_stop_sumo = time.ticks_us()
        cm_sumo = time.ticks_diff(pwm_stop_sumo, pwm_start_sumo) / 100
        values_sumo.append(cm_sumo)

def get_distance_sumo():
    global values_sumo
    temp_values_sumo = values_sumo[:-3]
    temp_values_sumo.sort()
    values_sumo = temp_values_sumo
    return temp_values_sumo[1]

def reset_sumo():
    global values_sumo,temp_values_sumo
    temp_values_sumo = []
    values_sumo = []
