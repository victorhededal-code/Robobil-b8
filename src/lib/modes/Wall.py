from movement import motor
from sensors import TOF

target_dist = 35    # was 40 before
base_speed = 60000
startup_time = 25

p_val = 2300
i_val = 0.0005

i_sum = 0


def pi_calc(cm):
    global i_sum, p_val, i_val, target_dist, base_speed
    print(cm)
    error = target_dist - cm
    print(error)
    if 25 < error or error < -20:
        if error > 0:
            error = 25
        else:
            error = -20
    p = error * p_val

    i_sum = i_sum + i_val * error

    if not 5000 > i_sum > -5000:
         if i_sum >= 0:
             i_sum = 5000
         else:
              i_sum = -5000

    duty = p + i_sum
    if error > 0:
        r_duty = base_speed
        l_duty = int(base_speed - duty)
    else:
        r_duty = int(base_speed + duty)
        l_duty = base_speed
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
    print("r_duty:", r_duty)
    print("\n\n\nl_duty:", l_duty)
    motor.RC_car.wall_movement(r_duty, l_duty)


