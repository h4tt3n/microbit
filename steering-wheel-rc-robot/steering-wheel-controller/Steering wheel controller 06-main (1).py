from microbit import *
from math import atan2, pi
import radio

# Configure radio
radio.on()
radio.config(group=42, channel=42, power=7)

while True:
    x, y = accelerometer.get_x(), accelerometer.get_y()

    angle = atan2(y, x) - 0.5 * pi
    if angle < -pi:
        angle += 2 * pi
    elif angle > pi:
        angle -= 2 * pi

    angle = round(angle / (0.5 * pi), 2)
    btn_a = int(button_a.is_pressed())
    btn_b = int(button_b.is_pressed())

    message = "{},{},{}".format(angle, btn_a, btn_b)
    
    radio.send(message)
    #print(message)
    
    sleep(10)
