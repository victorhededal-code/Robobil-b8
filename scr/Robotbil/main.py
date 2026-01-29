from movement import movement
from sensors import TOF, REF_sens

def main():
    print("running main")
    movement.test_movement()
    REF_sens.ref_measure(True)
main()