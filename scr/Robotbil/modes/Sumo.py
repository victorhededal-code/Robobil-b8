from movement import motor
from sensors import TOF, REF_sens
import time
def find_box():
    input("##############################################################\n"
          "##          pls read IMPORTANT                           ##\n"
          "##       Sumo at the moment WILL overheat REF sensor     ##\n"
          "#############################################################")
    while True:
        count=0
        cm = TOF.measure()
        edge=REF_sens.ref_measure()
        print("edge =", edge)
        give_command(cm,edge,count)

def give_command(cm:float,edge:int,count:int) -> None:
    """gives the command to the robot"""
    """tankegang:
    bil drejer i cirkel indtil den finder en box,
    når den har fundet en box vil den køre ind i den indtil den når kanten
    når bilen når kanten vil den stoppe og gå tilbage i ligeså lang tid som den kørte frem (return to middle)
    inden den søger igen vil bilen dreje 45 grader (dvs, x antal millisekunder)for at undgå at konstant køre ind i den samme kasse"""


    if edge == 0:
        print("stop motor pls")
        motor.stop_motors()
        #go_back(count) does not work yet

    while  cm < 60 and edge==1:
        print("box found, ramming")
        count+=1
        #motor.move_forward(100)
        cm = TOF.measure()
        edge=REF_sens.ref_measure()
    while cm > 60 and edge==1:
        print("No box, searching...")
        # motor.turn_left(100)
        cm = TOF.measure()
        edge=REF_sens.ref_measure()
def go_back(count:int) -> None: #we go back same distance we went forward, then we stop and turn
    for i in range(count):
        print("back")
        #motor.move_back(100)
    print("went back a total of",count,"times")
    count=0
    #motor.turn_left(100)
    time.sleep_ms(30)
    cm = TOF.measure()
    edge=REF_sens.ref_measure()
    give_command(cm,edge,count)




