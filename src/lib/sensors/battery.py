from machine import ADC

#############################
#       definitions         #
#############################
check_start = ADC(26)
check_mid = ADC(27)
check_end = ADC(28)

#############################
#       calculation         #
#############################
# v_ref = 3.3
# Rt = 3.35
# I_ref = v_ref/Rt = 98.4 * 10^-6

battery = 0

def calc_battery():
    global battery
    battery = round(((check_start.read_u16()* (4.1/ 65535)) + (check_end.read_u16() * (2.6 / 65535))  + (check_mid.read_u16() * ( 2.6/65535 ))),2)

def get_battery():
    global battery
    return battery

"""def bettery_calc_procentage():
    bettery_power = (check_start.read_u16() + check_end.read_u16() + check_mid.read_u16()) * (3.3 / 65535)
    bettery_procentage = (bettery_power / 8.8) * 100
    return bettery_procentage"""