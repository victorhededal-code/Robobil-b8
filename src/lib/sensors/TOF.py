# målinger
import time
from machine import Pin

wall_list = []
temp_wall = []
gy53_wall = Pin(14, Pin.IN)  # Initialize GY-53 I2C pin
pwm_start_wall = 0
pwm_stop_wall = 0

####################################
###             Wall             ###
####################################

def irq_init_wall():
    gy53_wall.irq(trigger=Pin.IRQ_RISING |Pin.IRQ_FALLING, handler = irq_handler_wall)


def irq_handler_wall( gy53_wall ):
    global pwm_start_wall, pwm_stop_wall
    if gy53_wall.value() == 1:
        pwm_start_wall = time.ticks_us()
    else:
        pwm_stop_wall = time.ticks_us()
        cm = (pwm_stop_wall - pwm_start_wall) / 100
        wall_list.append(cm)


def get_distance_wall():
    global wall_list, temp_wall
    cut = len(wall_list)
    temp_wall = wall_list[:(cut - 3)]
    wall_list.clear()
    wall_list = temp_wall
    temp_wall.sort()
    dist = temp_wall[1]
    temp_wall.clear()
    return dist


def reset_wall():
    global wall_list
    wall_list = []


####################################
###             Sumo             ###
####################################


sumo_list = []
temp_sumo = []
sumo_dist = 0
gy53_sumo = Pin(26, Pin.IN)  # Initialize GY-53 I2C pin
pwm_start_sumo = 0
pwm_stop_sumo = 0


def irq_init_sumo():
    gy53_sumo.irq(trigger=Pin.IRQ_RISING |Pin.IRQ_FALLING, handler = irq_handler_sumo)


def irq_handler_sumo( gy53_sumo ):
    global pwm_start_sumo, pwm_stop_sumo
    if gy53_sumo.value() == 1:
        pwm_start_sumo = time.ticks_us()
    else:
        pwm_stop_sumo = time.ticks_us()
        cm = ((pwm_stop_sumo - pwm_start_sumo) / 100)
        sumo_list.append(cm)


def get_distance_sumo():
    global sumo_list, temp_sumo, sumo_list
    cut = len(sumo_list)
    temp_sumo = sumo_list[:(cut - 3)]
    sumo_list.clear()
    sumo_list = temp_sumo
    temp_sumo.sort()
    sumo_dist = temp_sumo[1]
    temp_sumo.clear()



def reset_sumo():
    global sumo_list
    sumo_list = []

