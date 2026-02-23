# /udp_main.py
from movement import motor
from network import WLAN
from modes import Sumo, Wall, Fodbold
from sensors import REF_sens, TOF
import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet protocol, UDP

wall = False

sumo = False

fodbold = False

def UDP_init():
    global soc
    # Setup socket
    soc.bind(("0.0.0.0", 12345))  # Bind the socket to the machines own IP, and port 12345
def UDP_Listen():
    global wall, sumo, fodbold

    try:
        # Wait for a command

        data, addr = soc.recvfrom(1024)

        # Convert data from bytes to string
        data = data.decode('ascii').strip('\n').lower()

        # Handle command
        if data == '1':
            fodbold = True
            Fodbold.control(data)
        elif data == '2':
            wall = True
            TOF.reset_wall()
            Wall.find_wall()
        elif data == '3':
            sumo = True
            REF_sens.reset_ref()
            TOF.reset_sumo()
            Sumo.find_box()
        elif data == 'space':
            motor.stop_motors()

        else:
            if wall:
                if data == "4":
                    wall = False
                    motor.stop_motors()
                else:
                    Wall.find_wall()
            if sumo:
                if data == "4":
                    sumo = False
                    motor.stop_motors()
                else:
                    Sumo.find_box()

            if fodbold:
                if data == "4":
                    fodbold = False
                    motor.stop_motors()
                else:
                    Fodbold.control(data)

    except Exception as e:
        # If the program is interrupted, we need to close the port
        soc.close()
        raise e  # Re-raise the error, so the program exits properly
