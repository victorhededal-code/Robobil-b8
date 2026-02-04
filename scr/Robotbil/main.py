from movement import motor
from sensors import TOF
from time import sleep, sleep_ms
from modes import Wall

def main():
    while True:
        print("running main")
        #motor.test_movement()
        #motor.turn_right()
        #motor.turn_left()
        Wall.find_wall() #yessir it work


main()