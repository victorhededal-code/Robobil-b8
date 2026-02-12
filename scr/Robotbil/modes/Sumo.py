from movement import motor
from sensors import TOF, REF_sens
import time


def find_box():
    input("##############################################################\n"
          "##          pls read IMPORTANT                           ##\n"
          "##       Sumo at the moment WILL overheat REF sensor     ##\n"
          "#############################################################")
    while True:
        cm = TOF.measure()
        edge = REF_sens.ref_measure()
        print("edge =", edge)
        give_command(cm, edge)


def give_command(cm: float, edge: int) -> None:
    """gives the command to the robot"""
    """tankegang:
    bil drejer i cirkel indtil den finder en box,
    når den har fundet en box vil den køre ind i den indtil den når kanten
    når bilen når kanten vil den stoppe og gå tilbage i ligeså lang tid som den kørte frem (return to middle)
    inden den søger igen vil bilen dreje 45 grader (dvs, x antal millisekunder)for at undgå at konstant køre ind i den samme kasse"""

    if edge == 1:
        go_back()

    elif cm < 40:
        push()

    while cm > 40 and edge == 0:
        print("No box, searching...")
        motor.q_turn_right()
        cm = TOF.measure()
        edge = REF_sens.ref_measure()


def go_back() -> None:  # we go back, then we stop and turn
    print("back")
    motor.move_back(100)
    time.sleep_ms(100)
    motor.q_turn_right(100)
    time.sleep_ms(100)
    return


def push():
    motor.q_turn_right(100)
    time.sleep(1)
    edge = 0
    while not edge:
        motor.move_forward(50)
        time.sleep_ms(20)
        motor.stop_motors()
        edge = REF_sens.ref_measure()




