from microbit import *

devices = i2c.scan()
print(devices)

i2c.write(0x27, bytes([0x00]))  # Attempt a basic write

sleep(1000)

addr = 0x27  # Change to 0x3F if necessary

# Try sending a basic LCD command (turn on backlight)
try:
    i2c.write(addr, bytes([0x08]))  # 0x08 turns on backlight
except OSError:
    print("I2C write failed!")