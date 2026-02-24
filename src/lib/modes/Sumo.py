from movement import motor
from sensors import TOF, REF_sens

push_count = 0
reset = False
startup_time = 250 #ms


def find_box(done=False) -> None:
    global reset, push_count, startup_time
    if done:
        startup_time = 250
        motor.stop_motors()
    if startup_time:
        startup_time -= 50 #ms
        return
    box= REF_sens.check_box()
    if reset:
        if box:
            push()
        else:
            if push_count >= 1:
                go_back()
                push_count -= 1
            else:
                reset = False
    elif not box:
        cm = TOF.get_distance_sumo()
        if cm<70:
            REF_sens.found_box()
            reset = True
        else:
            if not cm:
                pass
            else:
                turn()


def push() -> None:
    global push_count
    motor.move_back(50)
    push_count += 1

def turn() -> None:
    motor.q_turn_right(50)

def go_back() -> None:
    motor.move_forward(50)