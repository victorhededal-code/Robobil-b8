from movement import motor
from sensors import TOF
import time

cm = 0


def find_wall():
    global cm
    cm = TOF.get_distance()
    give_command(cm)


def give_command(cm: float) -> None:
    """gives the command to the robot"""
    if cm <= 5:
        print("stop motor pls")
        motor.stop_motors()

    elif 5 < cm < 20:
        print("way too close")
        motor.turn_left(80)
        time.sleep_ms(30)

    elif cm <= 30 and cm > 20:
        print(" too close")
        motor.turn_left(80)
        time.sleep_ms(30)
        motor.move_forward(70)
        time.sleep_ms(10)


    elif cm > 60:
        print("way too far")
        motor.move_forward(60)
        time.sleep_ms(15)
        motor.turn_right(100)
        time.sleep_ms(100)


    elif 40 <= cm:
        print(" too far away")
        motor.turn_right(80)
        time.sleep_ms(30)
        motor.move_forward(80)
        time.sleep_ms(10)


    elif cm < 40 and cm > 30:
        print(" move along the wall")
        motor.move_forward(100)

