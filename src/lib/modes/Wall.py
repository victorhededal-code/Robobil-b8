from movement import motor
from sensors import TOF

target_dist = 30
base_speed = 40000

p_val = 750
i_val = 0.1

i_sum = 0.0

RC_car = Car(16, 17, 18, 19, 20, 21, l_offset=4)


def pi_calc(cm):
    global i_sum, p_val, i_val
    error = target_dist - cm

    if not 20 < error > -20:
        if error > 0:
            error = 20
        else:
            error = -20

    p = error * p_val
    i_sum = i_sum + i_val * error

    duty = p + i_sum

    r_duty = int(duty - base_speed)
    l_duty = int(duty + base_speed)

    return r_duty, l_duty


def wall_main():
    global RC_car
    r_duty, l_duty = pi_calc(get_distance_wall)
    RC_car.custome(1, 0, 1, 0, r_duty, l_duty)

