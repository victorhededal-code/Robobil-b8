from machine import Pin, PWM
from time import sleep

def test_movement():
    print("running test_movement")
    motor1 = Make_DCmotor(16,17,18)
    motor2 = Make_DCmotor(19,20,21)
    motor1.backward(50)
    motor2.forward(50)
    sleep(2)
    motor1.forward(75)
    motor2.backward(75)
    sleep(2)
    motor2.forward(100)
    motor1.backward(100)
    sleep(2)
    motor1.stop()
    motor2.stop()
"""def forwards():
    print("running forwards")
    motor1 = Make_DCmotor(16,17,18)
    motor2 = Make_DCmotor(19,20,21)
    motor1.backward()
    motor2.forward()"""


class Make_DCmotor:
    def __init__(self, pin1, pin2, enable_pin, max_duty = 65636,min_duty = 15000,speed=0):
        print(self,"making motor")
        self.pin1 = Pin(pin1,Pin.OUT)
        self.pin2 = Pin(pin2,Pin.OUT)
        self.enable_pin = PWM(enable_pin,freq=1000, duty_u16=65535)
        self.max_duty = max_duty
        self.min_duty = min_duty
        self.speed = speed


    def duty_cycle(self, speed):
        if self.speed <= 0 or self.speed > 100:
            duty_cyclen = 0
        else:
            duty_cyclen = int(self.min_duty + (self.max_duty - self.min_duty) * ((self.speed - 1) / (100 - 1)))
        return duty_cyclen

    def forward(self,speed):
        self.speed = speed
        print(self,"moving forward")
        self.enable_pin.duty_u16(self.duty_cycle(self.speed))
        self.pin1.on()
        self.pin2.off()
        #self.enable_pin.value(1)

    def backward(self,speed):
        self.speed = speed
        print(self,"moving backward")
        self.enable_pin.duty_u16(self.duty_cycle(self.speed))
        self.pin1.off()
        self.pin2.on()
        #self.enable_pin.value(1)
    def stop(self):
        print(self,"stopping motor")
        self.speed = 0
        self.enable_pin.duty_u16(self.duty_cycle(self.speed))
        self.pin1.on()
        self.pin2.on()
        #self.enable_pin.value(0)




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
        duty_cyclen = 0
    else:
        duty_cyclen = int(self.min_duty + (self.max_duty - self.min_duty) * ((self.speed - 1) / (100 - 1)))
    return duty_cyclen