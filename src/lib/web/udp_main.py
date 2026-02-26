# /udp_main.py
from movement import motor
from network import WLAN
from modes import Sumo, Wall, Fodbold
from sensors import REF_sens, TOF
import socket

wall = False

sumo = False

fodbold = False


def UDP_Listen():
    global wall, sumo, fodbold
    # Internet protocol, UDP
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        soc.bind(("0.0.0.0", 12345))
        try:
            # Wait for a command
            data, addr = soc.recvfrom(1024)
            # Convert data from bytes to string
            data = data.decode('ascii').strip('\n').lower()
        except OSError:
            data = "123"

        # Handle command

        if data == '1':
            REF_sens.sumo_init(False)
            fodbold = True
            Fodbold.control(data)
        elif data == '2':
            REF_sens.sumo_init(False)
            wall = True
            TOF.reset_wall()
            Wall.wall_main()
        elif data == '3':
            sumo = True
            REF_sens.sumo_init(sumo)
            REF_sens.reset_ref()
            TOF.reset_sumo()
            Sumo.find_box()
        elif data == 'space':
            motor.RC_car.stop()

        if wall:
            if data == "4":
                wall = False
                Wall.wall_main(True)
                motor.RC_car.stop()
            else:
                TOF.reset_sumo()
                Wall.wall_main()
        elif sumo:
            if data == "4":
                sumo = False
                REF_sens.sumo_init(sumo)
                Sumo.find_box(True)
            else:
                TOF.reset_wall()
                Sumo.find_box()
        elif fodbold:
            if data == "4":
                fodbold = False
                motor.RC_car.stop()
            else:
                TOF.reset_wall()
                TOF.reset_sumo()
                Fodbold.control(data)
        else:
            TOF.reset_wall()
            TOF.reset_sumo()
        soc.close()

    except Exception as e:
        # If the program is interrupted, we need to close the port
        soc.close()
        raise e  # Re-raise the error, so the program exits properly
