from movement import motor
from sensors import TOF
from time import sleep, sleep_ms
from modes import Wall,Sumo

def main():
    while True:
        try:
            print("running main")
            ch=input("press the corresponding number to start said mode:\n"
                     "1) wallfollow\n"
                     "2) sumo\n"
                     "3) None(future football)")
            #motor.test_movement()
            #motor.turn_right()
            #motor.turn_left()
            if ch == "1":
                Wall.find_wall()
            if ch == "2":
                Sumo.find_box()
        except KeyboardInterrupt:
            print("interrupted")
            motor.stop_motors()


main()



