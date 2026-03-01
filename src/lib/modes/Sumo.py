from movement import motor
from sensors import TOF, REF_sens

push_count = 0
reset = False
startup_time = 50  # 500 ms
start_stop_time = 15  # 400 ms
new_place_time = 200  # 2000 ms


def find_box(done=False) -> None:
    global reset, push_count, startup_time, start_stop_time, new_place_time
    if done:
        startup_time = 50
        motor.RC_car.stop()
    if startup_time:
        startup_time -= 5  # ms
        return

    if start_stop_time <= 0:
        start_stop_time = 15
    else:
        start_stop_time -= 1

    edge = REF_sens.check_edge()
    if edge:
        motor.RC_car.stop()
        REF_sens.reset_edge()

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
        if new_place_time <= 0:
            if not edge:
                push()
            else:
                if push_count / 2 >= 100:
                    go_back()
                    push_count -= 1
                else:
                    new_place_time = 200
                    push_count = 0

        else:
            cm = TOF.get_sumo_dist()
            if cm < 100:
                REF_sens.found_box()
                reset = True
                print(cm)
            else:
                if start_stop_time >= 5:
                    motor.RC_car.stop()
                else:
                    turn()
                    new_place_time -= 1


def push() -> None:
    global push_count
    motor.RC_car.move_back(58, 60)  # Only works on max volt
    push_count += 1


def turn() -> None:
    motor.RC_car.q_turn_right(30, 30)


def go_back() -> None:
    motor.RC_car.move_forward(45, 45)