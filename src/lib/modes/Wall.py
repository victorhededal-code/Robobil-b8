from movement import motor
from sensors import TOF 

target_dist = 40 
base_speed = 40000

p_val = 500
i_val = 0.005

i_sum = 0 


def pi_calc( cm ):
    global i_sum, p_val, i_val, target_dist, base_speed 
    error = target_dist - cm  

    if not 25 < error > -39:
        if error > 0:
            error = 25 
        else:
            error = -39 

    p = error * p_val

    i_sum = i_sum + i_val * error 

    if not 5 < i_sum > -5:
        if i_sum > 5:
            i_sum = 5
        else:
            i_sum = -5

    duty = p + i_sum 

       
    r_duty = int( duty - base_speed )
    l_duty = int( duty + base_speed )

    return r_duty, l_duty
    
    
def wall_main():
    global RC_car 
    r_duty, l_duty = pi_calc( TOF.get_distance_wall() )
    motor.RC_car.wall_movement( r_duty, l_duty )


