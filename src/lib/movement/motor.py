from machine import Pin, PWM


class DCmotor:
    """DC Motor class
    class made for a dc motor with 2 pins and a pwm pin

    Defaults: 
        max_duty & min_duty are preset for a raspberry pi pico's arcitecture
        speed is set to 0 so the motor doesnt start when making the object 

    Attributes:
        pos_pin: possitive pin for the motor  
        neg_pin: negetive pin for the motor 
        enable_pin: pwm enable pin for the motor 
        max_duty: max duty, depends on arcitecture 
        min_duty: min_duty, ensures the motor gets the minimum duty needed to spin
        speed: sets the standart speed

    Methods: forward, backward, stop, custome"""
    def __init__(self, pos_pin, neg_pin, enable_pin, max_duty=65636, min_duty=15000, speed=0):
        self.pos_pin = Pin(pos_pin, Pin.OUT)
        self.neg_pin = Pin(neg_pin, Pin.OUT)
        self.enable_pin = PWM(enable_pin, freq=1000, duty_u16=65535)
        self.max_duty = max_duty
        self.min_duty = min_duty
        self.speed = speed

    def duty_cycle(self, speed: int) -> int:
        self.speed = speed
        if self.speed <= 0 or self.speed > 100:
            duty_cyclen = 0
        else:
            duty_cyclen = int(self.min_duty + ((self.max_duty - self.min_duty) * (self.speed / 100)))
            print(self.min_duty)
            print( self.max_duty)
            print(self.speed)

            # duty = min + ((max - min) * (80 / 100))
            # duty = 15000 + (50000 * 0,8)
            # 50000 * 0,8 = 40000
            # duty = 15000 + 40000
            # duty = 55000
        #print(duty_cyclen)
        return duty_cyclen

    def forward(self, speed: int):
        self.enable_pin.duty_u16(self.duty_cycle(speed))
        self.pos_pin.on()
        self.neg_pin.off()

    def backward(self, speed: int):
        self.enable_pin.duty_u16(self.duty_cycle(speed))
        self.pos_pin.off()
        self.neg_pin.on()

    def stop(self):
        self.speed = 0
        self.enable_pin.duty_u16(self.duty_cycle(self.speed))
        self.pos_pin.on()
        self.neg_pin.on()

    def custome(self,speed):
        self.enable_pin.duty_u16(speed)
        self.pos_pin.on()
        self.neg_pin.off()


class Car:
    """Class for Car
    with 2 DCmotors with pwm control 


    Defaults:
        h_offset: can be set if the right motor needs offset
        v_offset: can be set if the left motor needs offset 
    
    Attributes:
        h_pos_pin: right possitive pin
        h_neg_pin: right negative pin 
        v_pos_pin: left possitive pin 
        v_neg_pin: left negative pin 
        h_enable_pin: enable pin for right motor
        v_enable_pin: enable pin for left motor  
        h_offset: offset for right motor 
        v_ffset: offset for left motor 
    
    Methods: move_forward, move_backward, turn_right, turn_left, q_turn_right, q_turn_left, stop 
    
    Warning: When using movement methods you need to have 2 speeds, one for each side """
    def __init__(self, h_pos_pin, h_neg_pin, h_enable_pin, v_pos_pin, v_neg_pin, v_enable_pin, h_offset=0, v_offset=0):
        self.h_pos_pin = Pin(h_pos_pin, Pin.OUT)
        self.h_neg_pin = Pin(h_neg_pin, Pin.OUT)
        self.h_enable_pin = PWM(h_enable_pin, freq=1000, duty_u16=65535)
        self.v_pos_pin = Pin(v_pos_pin, Pin.OUT)
        self.v_neg_pin = Pin(v_neg_pin, Pin.OUT)
        self.v_enable_pin = PWM(v_enable_pin, freq=1000, duty_u16=65535)
        self.h_offset = h_offset
        self.v_offset = v_offset

        self.h_motor = DCmotor(h_pos_pin, h_neg_pin, h_enable_pin)
        self.v_motor = DCmotor(v_pos_pin, v_neg_pin, v_enable_pin)

    def move_back(self, h_speed, v_speed):
        self.h_motor.backward(h_speed - self.h_offset)
        self.v_motor.backward(v_speed - self.v_offset)

    def stop(self):
        self.h_motor.stop()
        self.v_motor.stop()

    def move_forward(self, h_speed, v_speed):
        self.h_motor.forward((h_speed - self.h_offset))
        self.v_motor.forward((v_speed - self.v_offset))

    def turn_right(self, h_speed, v_speed):
        self.h_motor.forward(int((h_speed / 2) - self.h_offset))
        self.v_motor.forward(v_speed - self.v_offset)

    def q_turn_right(self, h_speed, v_speed):
        self.h_motor.backward(h_speed - self.h_offset)
        self.v_motor.forward(v_speed - self.v_offset)

    def turn_left(self, h_speed, v_speed):
        self.h_motor.forward(h_speed - self.h_offset)
        self.v_motor.forward(int((v_speed / 2) - self.v_offset))

    def q_turn_left(self, h_speed, v_speed):
        self.h_motor.forward(h_speed - self.h_offset)
        self.v_motor.backward(v_speed - self.v_offset)

    def wall_movement(self, h_duty, v_duty):
        self.h_motor.custome(h_duty)
        self.v_motor.custome(v_duty)

RC_car = Car(16, 17, 18, 19, 20, 21, v_offset=3)

