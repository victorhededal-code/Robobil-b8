wall = False
sumo = False
ball = False

def check_active_mode():
    global wall, sumo, ball
    if wall:
        mode = "wall"
    elif sumo:
        mode = "sumo"
    elif ball:
        mode = "ball"
    else:
        mode = "None"
    return mode

def change_mode(mode:str):
    global wall, sumo, ball
    if mode == "sumo":
        sumo = True
        wall = False
        ball = False

    if mode == "wall":
        wall = True
        ball = False
        sumo = False

    if mode == "ball":
        ball = True
        sumo = False
        wall = False
