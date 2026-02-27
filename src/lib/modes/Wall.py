# current problems summerized
# 1. TOF for wall currently does not return correct values, for some fucking reason (always return 500+)
# 2. we are currently always driving into a wall, when close to wall it will try to drive straight, when away from wall  it turns into wall
# 3. duty is almost always negative, this is big problem, as code is made with intention of duty being positive
# 4. I am getting very annoyed :D
from movement import motor
from sensors import TOF

target_dist = 40  # was 40 before
base_speed = 40000
startup_time = 10

p_val = 700  # TODO latest change needs testing
i_val = 0.0005

i_sum = 0


def pi_calc(cm):
    global i_sum, p_val, i_val, target_dist, base_speed
    error = target_dist - cm

    if 39 < error or error < -25:
        if error > 0:
            error = 39
        else:
            error = -25
    p = error * p_val

    i_sum = i_sum + (i_val * error)

    if not 1000 > i_sum > -1000:
        if i_sum > 1:
            i_sum = 1000
        else:
            i_sum = -1000

    duty = p + i_sum

    r_duty = int(base_speed + duty)
    l_duty = int(base_speed - duty)
    return r_duty, l_duty


def wall_main(done=False):
    if done:
        motor.RC_car.stop()

    r_duty, l_duty = pi_calc(TOF.get_distance_wall())
    print("right", r_duty)
    print("left", l_duty)
    motor.RC_car.wall_movement(r_duty, l_duty)


