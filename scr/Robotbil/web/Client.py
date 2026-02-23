import keyboard
import socket

# Setup socket
soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet protocol, UDP
soc.bind(("0.0.0.0", 12345))  # Bind the socket to the machines own IP, and port 12345
addr = "10.110.0.39", 12345

try:
    while True:
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

        elif keyboard.is_pressed('w') and keyboard.is_pressed('a'):
            data = "wa"
            data = data.encode("ascii")
            # Handle command
            soc.sendto(data, addr)

        elif keyboard.is_pressed('w') and keyboard.is_pressed('d'):
            data = "wd"
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
            soc.sendto(data, addr)

        elif keyboard.is_pressed('3'):
            data = "3"
            data = data.encode("ascii")
            # Handle command
            soc.sendto(data, addr)

        elif keyboard.is_pressed('4'):
            data = "4"
            data = data.encode("ascii")
            # Handle command
            soc.sendto(data, addr)
        elif keyboard.is_pressed('5'):
            data = "5"
            data = data.encode("ascii")
            # Handle command
            soc.sendto(data, addr)

        elif keyboard.is_pressed('space'):
            data = "space"
            data = data.encode("ascii")
            # Handle command
            soc.sendto(data, addr)

        elif keyboard.is_pressed('6'):
            data = "6"
            data = data.encode("ascii")
            # Handle command
            soc.sendto(data, addr)
        else:
            data = "Nothing"
            data = data.encode("ascii")
            # Handle command
            soc.sendto(data, addr)
        data=None

except Exception as e:
    # if the program is interrupted, we need to close the port
    soc.close()
    raise e  # Re-raise the error, so the program exits properly
