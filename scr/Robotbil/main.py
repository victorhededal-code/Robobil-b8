#########################################################
# Import external modules
#########################################################
from machine import Timer
from sensors import hall_irq_init, REF_sens, TOF
from movement import motor
from web import UDP_Listen, UDP_init
from .TM import * 


#########################################################
# Hardware config
#########################################################
# 1 ms timer interrupt:
# Define the IRQ callback ISR:
def tick( timer ):
    tm_update_isr()

tim = Timer()
tim.init(freq=1000, mode=Timer.PERIODIC, callback=tick)


#########################################################
# internal init modules
#########################################################
UDP_init()
hall_irq_init()
TOF.irq_init_sumo()
TOF.irq_init_wall()
REF_sens.irq_init()


#########################################################
# CREATS TASKS
#########################################################
create_task( UDP_LISTENER, 50, UDP_Listen )
#create_task( CALC_SPEED, 1000, calc_speed )
#create_task( PRINT_TO_TERMINAL, 1000, print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGoing at {get_speed()} cmps"))


#########################################################
# EXECUTES TASKS
#########################################################
while True:
    tm_execute_task()