from movement import motor
#from sensors import *

def main():
    print("running main")
    motor.test_movement()
    motor.turn_right()
    motor.turn_left()
    #REF_sens.ref_measure(True)
main()