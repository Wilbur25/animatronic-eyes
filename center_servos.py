from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

for i in range(6):
    kit.servo[i].angle = 90

print("Servos 0-5 centered at 90°")
