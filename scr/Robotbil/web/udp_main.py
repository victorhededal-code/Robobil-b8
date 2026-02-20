# /udp_main.py
from movement import motor
from network import WLAN
from modes import Sumo, Wall
import socket

wall = False

sumo = False

def UDP_Listen():
    global wall, sumo,count
    # Setup socket
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Internet protocol, UDP
    soc.bind(("0.0.0.0", 12345)) # Bind the socket to the machines own IP, and port 12345

    # Indicate program is ready

    try:
        while True:
            # Wait for a command
            data, addr = soc.recvfrom(1024)

            # Convert data from bytes to string
            data = data.decode('ascii').strip('\n').lower()

            print("Received from", addr, ":", data)



            # Handle command
            if data == 'w':
                motor.move_forward(80)
            elif data == 's':
                motor.move_back(80)
            elif data == 'd':
                motor.q_turn_right(80)
            elif data == 'a':
                motor.q_turn_left(80)
            elif data == 'wd':
                motor.turn_right(80)
            elif data == 'wa':
                motor.turn_left(80)
            elif data == '2':
                sumo = True
                Sumo.find_box()
            elif data == '1':
                wall = True
                Wall.find_wall()
            elif data == '3':
                motor.stop_motors()

            else:
                if wall == True:
                    if data == "4":
                        wall = False
                        motor.stop_motors()
                    else:
                        Wall.find_wall()
                if sumo == True:
                    if data == "4":
                        sumo = False
                        motor.stop_motors()
                    else:
                       Sumo.find_box()
                print(30*"\n")
                print("Waiting for data")


    except Exception as e:
        # If the program is interrupted, we need to close the port
        soc.close()
        raise e # Re-raise the error, so the program exits properly
