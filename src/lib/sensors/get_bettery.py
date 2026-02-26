# check hvilke pins vi skal bruge (det skal være ad pins)
# pins(26,27,28)
# from machine import Pin, adc
"""lav en funktion der måler på pin 1,2 og 3 og gemmer verdier
Nu har du total ad
så skal du finde ud af hvad 1 er af 65000
så 3.3 / 65535 = værdi af 1
tag de tre målinger og lig dem sammen og gange med værdi af en
resultatet af dette er spændingen på batteriet
dette resultat kan divideres med 65535 og ganges med 100 for at finde %
"""
from machine import Pin, ADC

#############################
#       definitions         #
#############################
check_start = ADC(Pin(26,Pin.IN))
check_mid = ADC(Pin(27,Pin.IN))
check_end = ADC(Pin(28,Pin.IN))

#############################
#       calculation         #
#############################
def bettery_calc():
    bettery_power = (check_start.read_u16() + check_end.read_u16()  + check_mid.read_u16() ) * (3.3 / 65535)
    return bettery_power
def bettery_calc_procentage():
    bettery_power = (check_start.read_u16() + check_end.read_u16() + check_mid.read_u16()) * (3.3 / 65535)
    bettery_procentage = (bettery_power / 8.8) * 100
    return bettery_procentage