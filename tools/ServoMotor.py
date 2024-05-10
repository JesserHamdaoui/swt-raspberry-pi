from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep


class ServoMotor(Servo):
    def __init__(self, PIN=18, initial_angle=0):
        factory = PiGPIOFactory()
        super().__init__(18, pin_factory = factory)
        self.current_angle = initial_angle
    

    def turn(self, desired_angle):
        print(f"rotating to {desired_angle}")
        angle = (desired_angle - self.current_angle) % 360
        self.value = 0.5
        sleep(2*(abs(angle)/360))
        self.value = 0
        self.current_angle = desired_angle



