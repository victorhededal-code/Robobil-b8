from movement import motor
from sensors import TOF, REF_sens

from src.lib.movement.motor import RC_car

push_count = 0
reset = False
startup_time = 1000  # ms
calc_timer = 0
new_place_time = 2000


def find_box(done=False) -> None:
    global reset, push_count, startup_time, calc_timer, new_place_time
    if done:
        startup_time = 1000
        motor.RC_car.stop()
    if startup_time:
        startup_time -= 5  # ms
        return

    if calc_timer <= 0:
        TOF.calc_distance_sumo()
        calc_timer = 20
    else:
        calc_timer -= 1
    edge = REF_sens.check_edge()
    if edge:
        motor.RC_car.stop()
        REF_sens.edge_reset()

    box = REF_sens.check_box()
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
        if new_place_time<=0:
            if not edge:
                push()
            else:
                if push_count / 2 >= 100:
                    go_back()
                    push_count -= 1
                else:
                    new_place_time = 2000
                    push_count = 0

        else:
            cm = TOF.get_distance_sumo()
            if cm < 80:
                REF_sens.found_box()
                reset = True
            else:
                if calc_timer <= 10:
                    motor.RC_car.stop()
                else:
                    turn()
                    new_place_time -= 5


def push() -> None:
    global push_count
    motor.RC_car.move_back(58, 60)  # Only works on max volt
    push_count += 1


def turn() -> None:
    motor.RC_car.q_turn_right(30, 30)


def go_back() -> None:
    motor.RC_car.move_forward(45, 45)