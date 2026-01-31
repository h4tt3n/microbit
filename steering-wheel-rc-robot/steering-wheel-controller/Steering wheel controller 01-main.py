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

    nx = x / mag if mag > 0 else 0
    ny = y / mag if mag > 0 else 0

    #print(nx, ny)

    angle = (atan2(ny, nx) / pi - 0.5) * 2

    #print(angle)

    # Determine button status
    if button_a.is_pressed() and button_b.is_pressed():
        button_status = "AB"
    elif button_a.is_pressed():
        button_status = "A"
    elif button_b.is_pressed():
        button_status = "B"
    else:
        button_status = "None"

    # Serialize data as a string (comma-separated)
    message = "{:.2f},{},{}".format(angle, button_a.is_pressed(), button_b.is_pressed())

    print(message)
    
    sleep(10)
