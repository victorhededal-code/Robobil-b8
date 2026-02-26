from movement import motor
speed = 60

def control(data):
    global speed

    for i in data:
        if 30 < speed < 80:
            speed += 1

    if data == 'e':
        speed = 60
        motor.RC_car.turn_right(speed,speed)
    elif data == 'q':
        speed = 60
        motor.RC_car.turn_left(speed,speed)

    elif data == 'z':
        speed = 60
        motor.RC_car.back_turn_left(speed,speed)

    elif data == 'c':
        speed = 60
        motor.RC_car.back_turn_right(speed,speed)

    elif data == 'w':
        speed = 60
        motor.RC_car.move_forward(speed,speed)
    elif data == 's':
        speed = 60
        motor.RC_car.move_back(30,30 )
    elif data == 'd':
        speed = 60
        motor.RC_car.q_turn_right(speed,speed)
    elif data == 'a':
        speed = 60
        motor.RC_car.q_turn_left(speed,speed)
    elif data == 'space':
        motor.RC_car.stop()

    else:
        if speed < 30:
            motor.RC_car.stop()
        else:
            speed -= 1

