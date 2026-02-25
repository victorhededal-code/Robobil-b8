from movement import motor
speed = 80

def control(data):
    global speed
    if data == 'wd':
        speed = 80
        motor.RC_car.turn_right(speed,speed)
    elif data == 'wa':
        speed = 80
        motor.RC_car.turn_left(speed,speed)
    elif data == 'w':
        speed = 80
        motor.RC_car.move_forward(speed,speed)
    elif data == 's':
        speed = 80
        motor.RC_car.move_back(30,30 )
    elif data == 'd':
        speed = 80
        motor.RC_car.q_turn_right(speed,speed)
    elif data == 'a':
        speed = 80
        motor.RC_car.q_turn_left(speed,speed)
    elif data == 'space':
        motor.RC_car.stop()

    else:
        if speed < 30:
            motor.RC_car.stop()
        else:
            speed -= 1

