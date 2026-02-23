#########################################################
# Import external modules
#########################################################
from machine import Timer
from sensors import hall_irq_init, ref_irq_init, tof_irq_init
from movement import Car
from web import UDP_init, UDP_listen
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
ref_irq_init()
tof_irq_init()
RC_car = Car(16,17,18,19,20,21, l_offset=4)


#########################################################
# CREATS TASKS
#########################################################
create_task( UDP_LISTENER, 10, UDP_listen )
create_task( CALC_SPEED, 1000, calc_speed )
create_task( PRINT_TO_TERMINAL, 1000, print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGoing at {get_speed()} cmps"))


#########################################################
# EXECUTES TASKS
#########################################################
while True:
    tm_execute_task()
