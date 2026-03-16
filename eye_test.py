from adafruit_servokit import ServoKit
from time import sleep

kit = ServoKit(channels=16)

# Servo channel mapping
LR = 0
UD = 1
TOP_LEFT = 2
BOTTOM_LEFT = 3
TOP_RIGHT = 4
BOTTOM_RIGHT = 5

CENTER = 90

print("Centering eyes")
kit.servo[LR].angle = CENTER
kit.servo[UD].angle = CENTER
sleep(2)

while True:

    print("Look Left")
    kit.servo[LR].angle = 120
    sleep(1)

    print("Center")
    kit.servo[LR].angle = CENTER
    sleep(1)

    print("Look Right")
    kit.servo[LR].angle = 120
    sleep(1)

    print("Center")
    kit.servo[LR].angle = CENTER
    sleep(1)

    print("Look Up")
    kit.servo[UD].angle = 120
    sleep(1)

    print("Center")
    kit.servo[UD].angle = CENTER
    sleep(1)

    print("Look Down")
    kit.servo[UD].angle = 120
    sleep(1)

    print("Center")
    kit.servo[UD].angle = CENTER
    sleep(2)
