from tools.ServoMotor import ServoMotor
from tools.get_current_position import get_current_position
from time import sleep

ip = "http://172.20.10.3:5000/"
initial_direction = get_current_position(ip)

servo = ServoMotor(18, 0)

print(initial_direction['currentAngle'])
servo.turn(initial_direction['currentAngle'])

sleep(1)
servo.turn(90)
sleep(1)
servo.turn(180)
sleep(1)
servo.turn(270)
sleep(1)
servo.turn(0)
