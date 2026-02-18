# /main.py
from movement import motor
from network import WLAN
from modes import Sumo, Wall
import socket

wall = False

sumo = False

count = 0

def UDP_Listen():
    global wall, sumo,count
    # Setup socket
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Internet protocol, UDP
    soc.bind(("0.0.0.0", 12345)) # Bind the socket to the machines own IP, and port 12345

    print(f'Listening for UDP on {WLAN.ipconfig('addr4')[0]}:12345')

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
                motor.move_forward()
            elif data == 's':
                motor.move_back()
            elif data == 'd':
                motor.qturn_right()
            elif data == 'a':
                motor.qturn_left()
            elif data == 'wd':
                motor.turn_right()
            elif data == 'wa':
                motor.turn_left()
            elif data == '2':
                sumo = True
            elif data == '1':
                wall = True
            elif data == '3':
                motor.stop_motors()

            else:
                if wall == True:
                    if data == "4":
                        wall = False
                    else:
                        Wall.find_wall()
                if sumo == True:
                    if data == "4":
                        sumo = False
                    else:
                        count = Sumo.find_box(count)
                print(30*"\n")
                print("Waiting for data")


    except Exception as e:
        # If the program is interrupted, we need to close the port
        soc.close()
        raise e # Re-raise the error, so the program exits properly
