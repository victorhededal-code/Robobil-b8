input()
#########################################################
# Import external modules
#########################################################
from machine import Timer
from sensors import REF_sens, TOF
from web import udp_main
import TM


#########################################################
# Hardware config
#########################################################
# 1 ms timer interrupt:
# Define the IRQ callback ISR:
def tick( timer ):
    TM.tm_update_isr()

tim = Timer()
tim.init(freq=1000, mode=Timer.PERIODIC, callback=tick)


#########################################################
# internal init modules
#########################################################
TOF.irq_init_sumo()
TOF.irq_init_wall()
REF_sens.irq_init()


#########################################################
# CREATS TASKS
#########################################################
TM.create_task("UDP_LISTENER", 5, udp_main.UDP_Listen)
#TM.create_task( CALC_SPEED, 1000, calc_speed )
#TM.create_task( PRINT_TO_TERMINAL, 1000, print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGoing at {get_speed()} cmps"))


#########################################################
# EXECUTES TASKS
#########################################################
while True:
    TM.tm_execute_task()