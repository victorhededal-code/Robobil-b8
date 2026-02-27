# /udp_main.py
from movement import motor
from modes import Sumo, Wall, Fodbold, check_mode
from sensors import REF_sens, TOF  # get_bettery, hall_sens
import socket


def UDP_Listen():
    # Internet protocol, UDP
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        mode = check_mode.check_active_mode()
        soc.bind(("0.0.0.0", 12345))
        # Wait for a command
        data, addr = soc.recvfrom(1024)
        # Convert data from bytes to string
        data = data.decode('ascii').strip('\n').lower()
        # Handle command

        if data == '1':
            REF_sens.sumo_init(False)
            check_mode.change_mode("ball")

        elif data == '2':
            REF_sens.sumo_init(False)
            check_mode.change_mode("wall")

        elif data == '3':
            check_mode.change_mode("sumo")
            REF_sens.sumo_init(True)
            REF_sens.reset_ref()

        if mode == "wall":
            if data == "space":
                Wall.wall_main(True)
                motor.RC_car.stop()
            else:
                TOF.reset_sumo()
                Wall.wall_main()

        elif mode == "sumo":
            if data == "space":
                REF_sens.sumo_init(False)
                Sumo.find_box(True)
            else:
                Sumo.find_box()

        elif mode == "ball":
                TOF.reset_sumo()
                Fodbold.control(data)

        else:
            TOF.reset_sumo()
        soc.close()

    except OSError:
        mode = check_mode.check_active_mode()
        if mode == "wall":
            TOF.reset_sumo()
            Wall.wall_main()

        elif mode == "sumo":
            Sumo.find_box()

        soc.close()

# def printing_task():
#    print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGoing at: {hall_sens.get()} mps\nBattery has: {get_bettery.bettery_calc()} V")