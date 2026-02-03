from movement import motor
from sensors import TOF

def main():
    while True:
        print("running main")
        #motor.test_movement()
        #motor.turn_right()
        #motor.turn_left()
        cm = TOF.measure()
        TOF.give_command(cm)

main()