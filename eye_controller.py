from adafruit_servokit import ServoKit
from time import sleep
import random

kit = ServoKit(channels=16)

# -----------------------------
# Channel mapping
# -----------------------------
LR = 0   # left/right
UD = 1   # up/down
LID_2 = 2
LID_3 = 3
LID_4 = 4
LID_5 = 5

# -----------------------------
# Eye movement calibration
# Start conservative. Increase later if needed.
# -----------------------------
LR_CENTER = 90
LR_LEFT = 35
LR_RIGHT = 150

UD_CENTER = 90
UD_UP = 82
UD_DOWN = 100

# -----------------------------
# Eyelid calibration
# -----------------------------
LID_2_OPEN = 170
LID_2_CLOSED = 90

LID_3_OPEN = 10
LID_3_CLOSED = 90

LID_4_OPEN = 10
LID_4_CLOSED = 90

LID_5_OPEN = 170
LID_5_CLOSED = 90

# -----------------------------
# Helper functions
# -----------------------------
def clamp(value, low, high):
    return max(low, min(high, value))

def set_lids_open():
    kit.servo[LID_2].angle = LID_2_OPEN
    kit.servo[LID_3].angle = LID_3_OPEN
    kit.servo[LID_4].angle = LID_4_OPEN
    kit.servo[LID_5].angle = LID_5_OPEN

def set_lids_closed():
    kit.servo[LID_2].angle = LID_2_CLOSED
    kit.servo[LID_3].angle = LID_3_CLOSED
    kit.servo[LID_4].angle = LID_4_CLOSED
    kit.servo[LID_5].angle = LID_5_CLOSED

def blink(closed_time=0.10):
    set_lids_closed()
    sleep(closed_time)
    set_lids_open()

def center_eyes():
    kit.servo[LR].angle = LR_CENTER
    kit.servo[UD].angle = UD_CENTER

def look_to(lr_angle, ud_angle):
    kit.servo[LR].angle = clamp(lr_angle, min(LR_LEFT, LR_RIGHT), max(LR_LEFT, LR_RIGHT))
    kit.servo[UD].angle = clamp(ud_angle, min(UD_UP, UD_DOWN), max(UD_UP, UD_DOWN))

def random_look():
    lr = random.randint(min(LR_LEFT, LR_RIGHT), max(LR_LEFT, LR_RIGHT))
    ud = random.randint(min(UD_UP, UD_DOWN), max(UD_UP, UD_DOWN))
    look_to(lr, ud)

def micro_saccade():
    # Tiny natural eye flick
    current_lr = kit.servo[LR].angle if kit.servo[LR].angle is not None else LR_CENTER
    current_ud = kit.servo[UD].angle if kit.servo[UD].angle is not None else UD_CENTER

    lr = clamp(current_lr + random.randint(-2, 2), min(LR_LEFT, LR_RIGHT), max(LR_LEFT, LR_RIGHT))
    ud = clamp(current_ud + random.randint(-1, 1), min(UD_UP, UD_DOWN), max(UD_UP, UD_DOWN))
    look_to(lr, ud)

# -----------------------------
# Startup state
# -----------------------------
center_eyes()
set_lids_open()
sleep(1.0)

# Small startup blink so you know it is alive
blink(0.15)
sleep(0.3)

# -----------------------------
# Main behavior loop
# -----------------------------
while True:
    # Pick a new gaze target
    random_look()

    # Hold gaze for a natural-ish amount of time
    hold_time = random.uniform(0.8, 2.2)
    end_time = hold_time / 0.2

    for _ in range(int(end_time)):
        # occasional tiny eye movement while holding
        if random.random() < 0.35:
            micro_saccade()

        # occasional blink
        if random.random() < 0.18:
            blink(0.10)

            # occasional double blink
            if random.random() < 0.15:
                sleep(0.08)
                blink(0.08)

        sleep(0.2)

    # Sometimes return closer to center before next move
    if random.random() < 0.30:
        look_to(
            random.randint(LR_CENTER - 4, LR_CENTER + 4),
            random.randint(UD_CENTER - 3, UD_CENTER + 3)
        )
        sleep(random.uniform(0.2, 0.5))
