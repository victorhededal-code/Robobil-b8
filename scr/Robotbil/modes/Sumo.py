from movement import motor
from sensors import TOF, REF_sens
import time

count = 0
box = False


def dummy():
    motor.q_turn_left(50)
    time.sleep_ms(175)
    motor.stop_motors()


def find_box() -> None:
    global box
    ###########################################################
    ##          pls read IMPORTANT                           ##
    ##       Sumo at the moment is not very precise          ##
    ###########################################################
    if not box:
        cm = TOF.measure()
    if box:
        cm = 200
    edge = REF_sens.ref_measure()
    # print("edge =", edge)
    # print("cm =", cm)
    give_command(cm, edge)


def give_command(cm: float, edge: int) -> None:
    """gives the command to the robot"""
    """tankegang:
    bil drejer i cirkel indtil den finder en box,
    når den har fundet en box vil den køre ind i den indtil den når kanten
    når bilen når kanten vil den stoppe og gå tilbage i ligeså lang tid som den kørte frem (return to middle)
    inden den søger igen vil bilen dreje 45 grader (dvs, x antal millisekunder)for at undgå at konstant køre ind i den samme kasse"""
    global box
    print(cm)
    """
    if edge == 1:
        go_back()
    elif box == True:

        push()
    elif cm > 10 and cm < 70 and box == False:
        print("Found box at ",cm)
        box = True
        motor.stop_motors()
        time.sleep_ms(500)
        motor.q_turn_left(50)
        time.sleep_ms(1110)


    else:
        print("No box, searching...")
        motor.stop_motors()
        motor.q_turn_left(40)



def go_back() -> None:  # we go back, then we stop and turn
    global count, box
    print("GB " + str(count))
    if count == 0 and box == False:
        motor.move_forward(50)
        time.sleep(1)

    for x in range(count):
        motor.move_forward(50)
        time.sleep_ms(20)
        motor.stop_motors()

    motor.q_turn_right(50)
    time.sleep_ms(400)
    count = 0
    box = False




def push():
    global count
    motor.move_back(50)
    count += 1
    print("pushing ",count)



"""