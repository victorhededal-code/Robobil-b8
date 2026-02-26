# current problems summerized
# 1. TOF for wall currently does not return correct values, for some fucking reason (always return 500+)
# 2. we are currently always driving into a wall, when close to wall it will try to drive straight, when away from wall  it turns into wall
# 3. duty is almost always negative, this is big problem, as code is made with intention of duty being positive
# 4. I am getting very annoyed :D

from movement import motor
from sensors import TOF

target_dist = 20  # was 40 before
base_speed = 40000
startup_time = 1000
calc_timer = 0

p_val = 500  # burde ikke komme over 550
i_val = 0.005

i_sum = 0


def pi_calc(cm):
    global i_sum, p_val, i_val, target_dist, base_speed
    error = target_dist - cm
    print("cm:", cm)

    if not 25 < error > -39:
        if error > 0:
            error = 25
        else:
            error = -39
    p = error * p_val

    i_sum = i_sum + i_val * error

    if not 5 > i_sum > -5:
        if i_sum > 5:
            i_sum = 5
        else:
            i_sum = -5

    duty = p + i_sum
    if duty + base_speed >= 65535 / 2:
        r_duty = int(duty - base_speed)
        l_duty = int((duty + base_speed) / 2)
    else:
        r_duty = int(duty - base_speed)
        l_duty = int(duty + base_speed)

    return r_duty, l_duty


def wall_main(done=False):
    global startup_time, calc_timer
    if done:
        startup_time = 1000
        motor.RC_car.stop()
    if startup_time:
        startup_time -= 5  # ms
        return
    if calc_timer <= 0:
        TOF.calc_distance_wall()
        calc_timer = 20
    else:
        calc_timer -= 1

    r_duty, l_duty = pi_calc(TOF.get_distance_wall())
    motor.RC_car.wall_movement(r_duty, l_duty)


