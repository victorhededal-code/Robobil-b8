from movement import motor
from sensors import TOF, REF_sens
import time


count = 0
box = False

def dummy():
    push()
    return count

def find_box() -> None:
###########################################################
##          pls read IMPORTANT                           ##
##       Sumo at the moment WILL overheat REF sensor     ##
###########################################################
    cm = TOF.measure()
    edge = REF_sens.ref_measure()
    print("edge =", edge)
    print("cm =", cm)
    give_command(cm, edge)



def give_command(cm: float, edge: int) -> None:
    """gives the command to the robot"""
    """tankegang:
    bil drejer i cirkel indtil den finder en box,
    når den har fundet en box vil den køre ind i den indtil den når kanten
    når bilen når kanten vil den stoppe og gå tilbage i ligeså lang tid som den kørte frem (return to middle)
    inden den søger igen vil bilen dreje 45 grader (dvs, x antal millisekunder)for at undgå at konstant køre ind i den samme kasse"""
    global box
    if edge == 1:
        go_back()
    elif box == True:
        push()
    elif cm < 30:
        motor.stop_motors()
        time.sleep_ms(300)
        motor.stop_motors()
        motor.q_turn_left(50)
        time.sleep_ms(1600)
        push()


    elif cm > 30 and edge == 0:
        print("No box, searching...")
        motor.stop_motors()
        motor.q_turn_left(40)



def go_back() -> None:  # we go back, then we stop and turn
    global count, box
    for x in range(count):
        motor.move_forward(30)
        time.sleep_ms(20)
        motor.stop_motors()
        print(count)
    motor.q_turn_right(50)
    time.sleep_ms(400)
    count = 0
    box = False




def push():
    global count, box
    box = True


    edge = 0
    while not edge:
        motor.move_back(50)
        time.sleep_ms(20)
        motor.stop_motors()
        edge = REF_sens.ref_measure()
        count += 1
        print("push_close",count)




