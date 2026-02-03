from sensors import TOF
from movement import motor
import time


def main():
    for i in range(500):
        cm = TOF.measure()
        TOF.give_command(cm)

    motor.stop_motors()


main()