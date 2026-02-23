from movement import motor
from sensors import TOF, REF_sens
import time

push_count = 0
reset = False


def dummy():
    motor.q_turn_left(50)
    time.sleep_ms(175)
    motor.stop_motors()


def find_box() -> None:
    global reset, push_count
    ###########################################################
    ##          pls read IMPORTANT                           ##
    ##       Sumo at the moment is not very precise          ##
    ###########################################################
    box= REF_sens.check_box()
    if reset:
        if box:
            push()
        else:
            if push_count >= 1:
                go_back()
            else:
                reset = False
    elif not box:
        cm = TOF.get_distance_sumo()
        if 10<cm<70:
            REF_sens.found_box()
            reset = True
        else:
            find_box()


def push() -> None:
    global push_count
    motor.move_back(50)
    push_count += 1

def turn() -> None:
    motor.q_turn_right(50)

def go_back() -> None:
    motor.forward(50)