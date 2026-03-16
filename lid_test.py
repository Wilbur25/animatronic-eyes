from adafruit_servokit import ServoKit
from time import sleep

kit = ServoKit(channels=16)

LID_2 = 2
LID_3 = 3
LID_4 = 4
LID_5 = 5

CLOSED_2 = 90
OPEN_2 = 180

CLOSED_3 = 90
OPEN_3 = 0

CLOSED_4 = 90
OPEN_4 = 0

CLOSED_5 = 90
OPEN_5 = 180

def lids_closed():
    kit.servo[LID_2].angle = CLOSED_2
    kit.servo[LID_3].angle = CLOSED_3
    kit.servo[LID_4].angle = CLOSED_4
    kit.servo[LID_5].angle = CLOSED_5

def lids_open():
    kit.servo[LID_2].angle = OPEN_2
    kit.servo[LID_3].angle = OPEN_3
    kit.servo[LID_4].angle = OPEN_4
    kit.servo[LID_5].angle = OPEN_5

print("Closing lids...")
lids_closed()
sleep(2)

while True:
    print("Open")
    lids_open()
    sleep(1)

    print("Close")
    lids_closed()
    sleep(1)
