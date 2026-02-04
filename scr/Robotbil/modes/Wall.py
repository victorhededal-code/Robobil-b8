from movement import motor
from sensors import TOF #,REF_sens
import time
def find_wall():
    while True:
        cm = TOF.measure()
        give_command(cm)


def give_command(cm:float) -> None:
    """gives the command to the robot"""
    if cm == 1:
        print("stop motor pls")
        motor.stop_motors()

    while 1< cm < 20:
        print("way too close")
        motor.turn_right(80)
        time.sleep_ms(30)
        cm = TOF.measure()

    while cm <= 30 and cm > 20:
        print(" too close")
        motor.turn_right(80)
        time.sleep_ms(30)
        motor.move_forward(70)
        time.sleep_ms(10)
        cm = TOF.measure()

    while cm > 60:
        print("way too far")
        motor.move_forward(60)
        time.sleep_ms(15)
        motor.turn_left(100)
        time.sleep_ms(100)
        cm = TOF.measure()

    while 40 <= cm:
        print(" too far away")
        motor.turn_left(80)
        time.sleep_ms(30)
        motor.move_forward(80)
        time.sleep_ms(10)
        cm = TOF.measure()

    while cm < 40 and cm > 30:
        print(" move along the wall")
        motor.move_forward(100)
        cm = TOF.measure()