# src/boot.py
from time import sleep, sleep_ms, ticks_ms, ticks_diff
from machine import Pin
from network import WLAN
import webrepl
"""Sets up webrepl and connects to the wifi"""
# setting up wlan and connecting to the network
wlan = WLAN(WLAN.IF_STA)
wlan.active(True)

# setting hostname for pico
wlan.config(hostname="B8 pico")

# Connecting to the network
wlan.connect("ITEK 1st", "itekf25v")

# starting webrepl
webrepl.start(password="1234")
