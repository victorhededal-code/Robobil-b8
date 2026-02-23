from movement import motor

def control(data):
    if data == 'w':
        motor.move_forward(80)
    elif data == 's':
        motor.move_back(80)
    elif data == 'd':
        motor.q_turn_right(80)
    elif data == 'a':
        motor.q_turn_left(80)
    elif data == 'wd':
        motor.turn_right(80)
    elif data == 'wa':
        motor.turn_left(80)
    elif data == 'space':
        motor.stop_motors()

