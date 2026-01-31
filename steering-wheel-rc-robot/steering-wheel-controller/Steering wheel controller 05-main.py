from microbit import *
from math import atan2, pi
import radio

radio.on()
radio.config(group=42, channel=42, power=7)

while True:
    x, y = accelerometer.get_x(), accelerometer.get_y()

    angle = atan2(y, x) - 0.5 * pi
    if angle < -pi:
        angle += 2 * pi
    elif angle > pi:
        angle -= 2 * pi

    angle = round(angle / pi, 2)

    message = "{},{},{}".format(angle, int(button_a.is_pressed()), int(button_b.is_pressed()))
    radio.send(message)
    print(message)
    
    sleep(10)  # More responsive
