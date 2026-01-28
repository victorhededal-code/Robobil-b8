import components
import movement
#import sensors
#import web

def main():

    DCmotor = movement.make_DCmotor()
    dc_motor1 = DCmotor
    dc_motor2 = DCmotor
    dc_motor1 = components.set_pins(16,17,18)
    dc_motor2 = components.set_pins(19,20,21)

try:
    print('Forward with speed: 50%')
    dc_motor1.forward(50)
    dc_motor2.forward(50)
    sleep(5)
    dc_motor1.stop()
    dc_motor2.stop()
    sleep(5)
    print('Backwards with speed: 100%')
    dc_motor1.backwards(100)
    dc_motor2.backwards(100)
    sleep(5)
    print('Forward with speed: 5%')
    dc_motor1.forward(5)
    dc_motor2.forward(5)
    sleep(5)
    dc_motor1.stop()
    dc_motor2.stop()
except KeyboardInterrupt:
    print('Keyboard Interrupt')
    dc_motor1.stop()
    dc_motor2.stop()
