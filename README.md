# Raspberry Pi Animatronic Eye Controller

Animatronic eye system built using:

- Raspberry Pi 3
- PCA9685 servo driver
- 6 MG90S metal gear servos

Features:

- Random eye movement
- Blinking and double blinking
- Micro-saccades for realism
- Automatic startup via systemd
- WiFi multi-network support

## Hardware

- Raspberry Pi 3
- PCA9685 16-channel servo HAT
- External 5V servo power supply
- 6 MG90S servos

## Servo Channels

0 = Left / Right  
1 = Up / Down  
PCA9685 Wiring

   Servo 0 (LR)
   Servo 1 (UD)
   Servo 2 (Top Left lid)
   Servo 3 (Bottom Left lid)
   Servo 4 (Top Right lid)
   Servo 5 (Bottom Right lid)

## Install

Create environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
