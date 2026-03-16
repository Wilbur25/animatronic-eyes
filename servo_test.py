from adafruit_servokit import ServoKit
from time import sleep

kit = ServoKit(channels=16)

SERVO = 0

positions = [70, 90, 110, 90]

while True:
    for p in positions:
        print(f"Moving to {p}")
        kit.servo[SERVO].angle = p
        sleep(1)
