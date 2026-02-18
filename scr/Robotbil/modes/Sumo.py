from movement import motor
from sensors import TOF, REF_sens
import time

def dummy(count=0):
    push(count)
    return count

def find_box(count=0):
    input("##############################################################\n"
          "##          pls read IMPORTANT                           ##\n"
          "##       Sumo at the moment WILL overheat REF sensor     ##\n"
          "#############################################################")
    cm = TOF.measure()
    edge = REF_sens.ref_measure()
    print("edge =", edge)
    print("cm =", cm)
    give_command(cm, edge,count)
    return count


def give_command(cm: float, edge: int,count:int) -> None:
    """gives the command to the robot"""
    """tankegang:
    bil drejer i cirkel indtil den finder en box,
    når den har fundet en box vil den køre ind i den indtil den når kanten
    når bilen når kanten vil den stoppe og gå tilbage i ligeså lang tid som den kørte frem (return to middle)
    inden den søger igen vil bilen dreje 45 grader (dvs, x antal millisekunder)for at undgå at konstant køre ind i den samme kasse"""
    if edge == 1:
        go_back(count)

    elif cm < 30:
        motor.stop_motors()
        time.sleep_ms(300)
        push(count)


    while cm > 30 and edge == 0:
        print("No box, searching...")
        motor.stop_motors()
        motor.q_turn_left(40)
        cm = TOF.measure()
        edge = REF_sens.ref_measure()


def go_back(count) -> None:  # we go back, then we stop and turn
    print("back")
    for x in range(count):
        motor.move_forward(30)
        time.sleep_ms(20)
        motor.stop_motors()
        print(count)
    count=0
    motor.q_turn_right(50)
    time.sleep_ms(400)



def push(count):
    motor.stop_motors()
    motor.q_turn_left(50)
    time.sleep_ms(1600)
    edge = 0
    while not edge:
        motor.move_back(50)
        time.sleep_ms(20)
        motor.stop_motors()
        edge = REF_sens.ref_measure()
        count += 1
        print("push_close",count)



