# målinger
import time
from machine import Pin

wall_dist = 0
gy53_wall = Pin(14, Pin.IN)  # Initialize GY-53 I2C pin
pwm_start_wall = 0
dist_1 = False
dist_2 = False
dist_3 = False

####################################
###             Wall             ###
####################################

def irq_init_wall():
    gy53_wall.irq(trigger = Pin.IRQ_RISING | Pin.IRQ_FALLING, handler = irq_handler_wall)


def irq_handler_wall( gy53_wall ):
    global pwm_start_wall, wall_dist, dist_1, dist_2, dist_3
    if gy53_wall.value() == 1:
        pwm_start_wall = time.ticks_us()
    else:
        pwm_stop_wall = time.ticks_us()
        cm = (pwm_stop_wall - pwm_start_wall) / 100
        if not dist_1:
            dist_1 = cm
        elif not dist_2:
            dist_2 = cm
        elif not dist_3:
            dist_3 = cm
            temp_list = [dist_1, dist_2, dist_3]
            temp_list.sort()
            wall_dist = temp_list[1]
            temp_list.clear()
            dist_1 = False
            dist_2 = False
            dist_3 = False


#def calc_distance_wall():
#    global wall_list, temp_wall, wall_list, wall_dist
    #print("\nwall list pre overwrite", wall_list)
#    wall_dist = 0
#    cut = len(wall_list)
#    temp_wall = wall_list[(cut - 5):]
    #print("\ntemporary list",temp_wall)
#    wall_list = temp_wall
   # print("\nwall list post overwrite",wall_list)
#    temp_wall.sort()
#    wall_dist = temp_wall[2]
    #print("\n\nwall dist",temp_wall[1])

def get_distance_wall():
    global wall_dist
    return wall_dist


####################################
###             Sumo             ###
####################################


sumo_list = []
temp_sumo = []
sumo_dist = 0
gy53_sumo = Pin(22, Pin.IN)  # Initialize GY-53 I2C pin
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
        cm = ((pwm_stop_sumo - pwm_start_sumo) // 100)
        if len(sumo_list) < 20:
            sumo_list.append(cm)
5

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
    sumo_list = []