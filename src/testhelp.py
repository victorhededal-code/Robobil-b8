from machine import Pin
from time import ticks_us
gy53 = Pin(14, Pin.IN)

distList = []
start = 0
timer = 1000000


def distance( gy53 ):
    global start
    if gy53.value():
        start = ticks_us()
    else:
        end = ticks_us()
        dist = (end - start) / 100
        distList.append(dist)


def test_init():
    gy53.irq( trigger = Pin.IRQ_RISING | Pin.IRQ_FALLING, handler = distance )

def get_dist():
    global distList, start
    if not start:
        pass
    cut = len(distList)
    cutoff = cut - 2
    temp = distList[:cutoff]
    temp.sort()
    distList = temp
    print(temp[1])
    print(distList)