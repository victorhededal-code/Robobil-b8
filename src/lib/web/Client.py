import keyboard
import socket
from time import sleep
wall = False
sumo = False
# Setup socket
soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet protocol, UDP
soc.bind(("0.0.0.0", 12345))  # Bind the socket to the machines own IP, and port 12345
addr = "10.110.0.39", 12345
while True:
    try:
        data = None
        if keyboard.is_pressed('w'):
            data = "w"
            data = data.encode("ascii")
            # Handle command
            soc.sendto(data, addr)

        elif keyboard.is_pressed('a'):
            data = "a"
            data = data.encode("ascii")
            # Handle command
            soc.sendto(data, addr)

        elif keyboard.is_pressed('s'):
            data = "s"
            data = data.encode("ascii")
            # Handle command
            soc.sendto(data, addr)

        elif keyboard.is_pressed('d'):
            data = "d"
            data = data.encode("ascii")
            # Handle command
            soc.sendto(data, addr)

        elif keyboard.is_pressed('1'):
            data = "1"
            data = data.encode("ascii")
            # Handle command
            soc.sendto(data, addr)

        elif keyboard.is_pressed('2'):
            data = "2"
            data = data.encode("ascii")
            # Handle command
            wall = True
            soc.sendto(data, addr)

        elif keyboard.is_pressed('3'):
            data = "3"
            data = data.encode("ascii")
            # Handle command
            sumo = True
            soc.sendto(data, addr)

        elif keyboard.is_pressed('space'):
            data = "space"
            sumo = False
            wall = False
            data = data.encode("ascii")
            # Handle command
            soc.sendto(data, addr)

        elif keyboard.is_pressed('q'):
            data = "q"
            data = data.encode("ascii")
            # Handle command
            soc.sendto(data, addr)

        elif keyboard.is_pressed('e'):
            data = "e"
            data = data.encode("ascii")
            # Handle command
            soc.sendto(data, addr)

        elif keyboard.is_pressed('z'):
            data = "z"
            data = data.encode("ascii")
            # Handle command
            soc.sendto(data, addr)

        elif keyboard.is_pressed('c'):
            data = "c"
            data = data.encode("ascii")
            # Handle command
            soc.sendto(data, addr)
        else:
            if wall:
                data = "2"
                data = data.encode("ascii")
                soc.sendto(data, addr)
            if sumo:
                data = "3"
                data = data.encode("ascii")
                soc.sendto(data, addr)
            sleep(0.1)

    except Exception as e:
        # if the program is interrupted, we need to close the port
        soc.close()
        raise e  # Re-raise the error, so the program exits properly
