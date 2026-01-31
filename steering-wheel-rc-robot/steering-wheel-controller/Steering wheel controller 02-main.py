from microbit import *
from math import *
import radio

# Set up radio
radio.on()
radio.config(channel=42)  # Must match receiver's channel

while True:

    x = accelerometer.get_x()
    y = accelerometer.get_y()
    
    mag = sqrt(x * x + y * y)

    # Normalize angle vector
    nx = x / mag if mag > 0 else 0
    ny = y / mag if mag > 0 else 0
    #print(nx, ny)

    # Normalize angle in range [-1, 1]
    angle = (atan2(ny, nx) / pi - 0.5) * 2
    #print(angle)

    # Serialize data as a string (comma-separated)
    message = "{:.2f},{},{}".format(angle, button_a.is_pressed(), button_b.is_pressed())

    print(message)
    radio.send(message)
    
    sleep(10)
