# målinger
import time
from machine import Pin

wall_dist = 0
wall_list = []
gy53_wall = Pin(14, Pin.IN)  # Initialize GY-53 I2C pin
pwm_start_wall = 0
list_count = 0
raw_dist = 0
####################################
###             Wall             ###
####################################

def irq_init_wall():
    gy53_wall.irq(trigger = Pin.IRQ_RISING | Pin.IRQ_FALLING, handler = irq_handler_wall)


def irq_handler_wall( gy53_wall ):
    global pwm_start_wall, wall_dist, list_count, raw_dist
    if gy53_wall.value() == 1:
        pwm_start_wall = time.ticks_us()
    else:
        pwm_stop_wall = time.ticks_us()
        cm = (pwm_stop_wall - pwm_start_wall) // 100
        #wall_list.append(cm)
        raw_dist = cm
        #if list_count >= 3:
        #    temp_list = wall_list.copy()
        #    temp_list.sort()
        #    wall_dist = temp_list[1]
        #    wall_list.pop(0)

        #else:
        #    list_count += 1


def get_distance_wall():
    global wall_dist
    return wall_dist

def get_raw_dist():
    global raw_dist
    return raw_dist


####################################
###             Sumo             ###
####################################

"""
sumo_list = []
temp_sumo = []
sumo_dist = 0
pwm_start_sumo = 0
pwm_stop_sumo = 0
"""
gy53_sumo = Pin(22, Pin.IN)  # Initialize GY-53 I2C pin
sumo_list = []
sumo_dist = 0
pwm_sumo = 0
sumo_count = 0

def sumo_irq():
    gy53_sumo.irq(trigger = Pin.IRQ_RISING | Pin.IRQ_FALLING,handler = sumo_handler )

def sumo_handler( gy53_sumo ):
    global pwm_sumo, sumo_dist, sumo_list, sumo_count
    if gy53_sumo.value() == 1:
        pwm_sumo = gy53_sumo.value()
    else:
        pwm_sumo_end = gy53_sumo.value()
        dist = (pwm_sumo_end - pwm_sumo) // 100
        sumo_list.append(dist)
        if sumo_count >= 5:
            temp_list = sumo_list.copy()
            temp_list.sort()
            sumo_dist = temp_list[2]
            sumo_list.pop(0)
        else:
            sumo_count += 1

def get_sumo_dist():
    global sumo_dist
    return sumo_dist
"""
def irq_init_sumo():
    gy53_sumo.irq(trigger=Pin.IRQ_RISING |Pin.IRQ_FALLING, handler = irq_handler_sumo)


def irq_handler_sumo( gy53_sumo ):
    global pwm_start_sumo, pwm_stop_sumo
    if gy53_sumo.value() == 1:
        pwm_start_sumo = time.ticks_us()
    else:
        pwm_stop_sumo = time.ticks_us()
        cm = ((pwm_stop_sumo - pwm_start_sumo) // 100)
        if len(sumo_list) < 20:
            sumo_list.append(cm)

def calc_distance_sumo():
    global sumo_list, temp_sumo, sumo_list, sumo_dist
    #print("\nsumo list pre overwrite", sumo_list)
    sumo_dist = 0
    cut = len(sumo_list)
    temp_sumo = sumo_list[(cut - 5):]
    #print("\ntemporary list",temp_sumo)
    sumo_list = temp_sumo
   # print("\nsumo list post overwrite",sumo_list)
    temp_sumo.sort()
    sumo_dist = temp_sumo[2]
    #print("\n\nsumo dist",temp_sumo[1])

def get_distance_sumo():
    global sumo_dist
    return sumo_dist


def reset_sumo():
    global sumo_list
    sumo_list = []'
"""