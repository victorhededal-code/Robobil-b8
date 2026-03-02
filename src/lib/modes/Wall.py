from movement import motor
from sensors import TOF

target_dist = 40  # mm
base_speed = 60000  # duty
startup_time = 25  # for more accurate measurements w

p_val = 700
i_val = 0.15

i_sum = 0
"""



def pi_calc(mm):
    global i_sum, p_val, i_val, target_dist, base_speed
    print(mm)
    error = target_dist - mm
    error = max(-30, min(39, error))

    print(error)
    p = error * p_val

    i_sum = int(i_sum + (i_val * error))
    i_sum = max(-8000, min(8000, i_sum))



    duty = int(p + i_sum)

    r_duty = max(0, min(65353, base_speed + duty))
    l_duty = max(0, min(65353, base_speed - duty))

    return r_duty, l_duty


def wall_main(done=False):
    global startup_time
    if done:
        startup_time = 5
        motor.RC_car.stop()
    if startup_time != 0:
        startup_time -= 1
        return

    r_duty, l_duty = pi_calc(TOF.get_distance_wall())
    print(f"duty left {l_duty}")
    print(f"\n\n\n\nduty right{r_duty}")
    motor.RC_car.wall_movement(r_duty, l_duty)"""


def wall_emergency_main(done=False):
    global startup_time
    if done:
        startup_time = 5
        motor.RC_car.stop()
    if startup_time != 0:
        startup_time -= 1
        return
    cm = TOF.get_distance_wall()
    if cm < 15:
        motor.RC_car.q_turn_left(0,50)
    elif 30 > cm > 15:
        motor.RC_car.turn_left(50,50)
    elif 40 > cm > 30:
        motor.RC_car.move_forward(50,50)
    elif 55 > cm > 40:
        motor.RC_car.turn_right(50,50)
    elif cm > 55:
        motor.RC_car.turn_right(50,30)


