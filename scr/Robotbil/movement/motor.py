from machine import Pin, PWM
from time import sleep, sleep_ms


def move_back():
    print("move back")
    motor1 = Make_DCmotor(16, 17, 18)
    motor2 = Make_DCmotor(20, 19, 21)
    motor2.backward(52)
    motor1.forward(50)
    sleep_ms(100)


def stop_motors():
    print("stop motors")
    motor1 = Make_DCmotor(16, 17, 18)
    motor2 = Make_DCmotor(20, 19, 21)
    motor1.stop()
    motor2.stop()


def move_forward():
    print("move forward")
    motor1 = Make_DCmotor(16, 17, 18)
    motor2 = Make_DCmotor(19, 20, 21)
    motor2.forward(52)
    motor1.backward(50)
    sleep_ms(100)


def turn_right():
    '''Makes motor turn right'''
    print("Turn right")
    motor1 = Make_DCmotor(16, 17, 18)
    motor2 = Make_DCmotor(20, 19, 21)
    motor1.backward(50)
    motor2.forward(50)
    sleep_ms(50)


def turn_left():
    '''Makes motor turn left'''
    print("turn left")
    motor1 = Make_DCmotor(16, 17, 18)
    motor2 = Make_DCmotor(20, 19, 21)
    motor2.backward(50)
    motor1.forward(50)
    sleep_ms(200)


class Make_DCmotor:
    """Builds motor class

    Params:pin1, pin2, enable_pin
    """

    def __init__(self, pin1, pin2, enable_pin, max_duty=65636, min_duty=15000, speed=0):
        self.pin1 = Pin(pin1, Pin.OUT)
        self.pin2 = Pin(pin2, Pin.OUT)
        self.enable_pin = PWM(enable_pin, freq=1000, duty_u16=65535)
        self.max_duty = max_duty
        self.min_duty = min_duty
        self.speed = speed

    def duty_cycle(self, speed) -> int:
        if self.speed <= 0 or self.speed > 100:
            duty_cyclen = 0
        else:
            duty_cyclen = int(self.min_duty + (self.max_duty - self.min_duty) * ((self.speed - 1) / (100 - 1)))
        return duty_cyclen

    def forward(self, speed: int):
        self.speed = speed
        self.enable_pin.duty_u16(self.duty_cycle(self.speed))
        self.pin1.on()
        self.pin2.off()

    def backward(self, speed):
        self.speed = speed
        self.enable_pin.duty_u16(self.duty_cycle(self.speed))
        self.pin1.off()
        self.pin2.on()

    def stop(self):
        self.speed = 0
        self.enable_pin.duty_u16(self.duty_cycle(self.speed))
        self.pin1.on()
        self.pin2.on()




