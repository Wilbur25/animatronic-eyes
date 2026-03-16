from adafruit_servokit import ServoKit
import sys
import time

kit = ServoKit(channels=16)

if len(sys.argv) != 3:
    print("Usage: python set_servo.py <channel> <angle>")
    print("Example: python set_servo.py 2 110")
    sys.exit(1)

channel = int(sys.argv[1])
angle = int(sys.argv[2])

if not 0 <= channel <= 15:
    print("Channel must be 0-15")
    sys.exit(1)

if not 0 <= angle <= 180:
    print("Angle must be 0-180")
    sys.exit(1)

print(f"Setting channel {channel} to angle {angle}")
kit.servo[channel].angle = angle

# hold position so the servo stays there while you work
while True:
    time.sleep(1)
