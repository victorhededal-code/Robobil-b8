from machine import Pin

from movement import motor
from sensors import TOF,REF_sens
from time import sleep, sleep_ms
from modes import Wall,Sumo
from web import udp_main as web

def main():
    while True:
        try:
            print("running main")
            TOF.irq_init_sumo()
            TOF.irq_init_wall()
            REF_sens.irq_init()
            web.UDP_Listen()


        except KeyboardInterrupt:
            print("interrupted")
            motor.stop_motors()


main()



