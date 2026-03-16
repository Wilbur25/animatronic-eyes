from adafruit_servokit import ServoKit
from time import sleep

kit = ServoKit(channels=16)

servo = 0  # change this for each servo

for angle in range(70, 111, 2):
    print("Angle:", angle)
    kit.servo[servo].angle = angle
    sleep(0.5)
