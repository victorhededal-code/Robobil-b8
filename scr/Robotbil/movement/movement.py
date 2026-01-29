from machine import Pin
from time import sleep
def test_movement():
    print("running test_movement")
    motor1 = Make_DCmotor(16,17,18)
    motor2 = Make_DCmotor(19,20,21)
    motor1.backward()
    motor2.forward()
    sleep(2)
    motor1.forward()
    motor2.backward()
    sleep(2)
    motor1.stop()
    motor2.stop()

class Make_DCmotor:
    def __init__(self, pin1, pin2, enable_pin):
        print(self,"making motor")
        self.pin1 = Pin(pin1,Pin.OUT)
        self.pin2 = Pin(pin2,Pin.OUT)
        self.enable_pin = Pin(enable_pin,Pin.OUT)
    def forward(self):
        print(self,"moving forward")
        self.pin1.value(1)
        self.pin2.value(0)
        self.enable_pin.value(1)
    def backward(self):
        print(self,"moving backward")
        self.pin1.value(0)
        self.pin2.value(1)
        self.enable_pin.value(1)
    def stop(self):
        print(self,"stopping motor")
        self.pin1.value(1)
        self.pin2.value(1)
        self.enable_pin.value(0)




def forward(self, speed):
    self.speed = speed
    self.enable_pin.duty_u16(self.duty_cycle(self.speed))
    self.pin1.value(1)
    self.pin2.value(0)

def backwards(self, speed):
    self.speed = speed
    self.enable_pin.duty_u16(self.duty_cycle(self.speed))
    self.pin1.value(0)
    self.pin2.value(1)

def stop(self):
    self.enable_pin.duty_u16(0)
    self.pin1.value(0)
    self.pin2.value(0)

def duty_cycle(self, speed):
    if self.speed <= 0 or self.speed > 100:
        duty_cycle = 0
    else:
        duty_cycle = int(self.min_duty + (self.max_duty - self.min_duty) * ((self.speed - 1) / (100 - 1)))
    return duty_cycle