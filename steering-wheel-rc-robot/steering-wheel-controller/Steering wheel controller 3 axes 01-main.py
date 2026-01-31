from microbit import *
from math import atan2, pi
import radio

# Configure radio
radio.on()
radio.config(group=42, channel=42, power=7)

while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()

    mag = accelerometer.get_strength()

    xy_angle = atan2(y, x) - 0.5 * pi

    if xy_angle < -pi:
        xy_angle += 2 * pi
    elif xy_angle > pi:
        xy_angle -= 2 * pi
    
    xz_angle = atan2(z, x) - 0.5 * pi
    
    if xz_angle < -pi:
        xz_angle += 2 * pi
    elif xz_angle > pi:
        xz_angle -= 2 * pi

    xy_angle = round(xy_angle / (0.5 * pi), 2)
    xz_angle = round(xz_angle / (0.5 * pi), 2)
    
    btn_a = int(button_a.is_pressed())
    btn_b = int(button_b.is_pressed())

    message = "{},{},{},{}".format(xy_angle, xz_angle, btn_a, btn_b)
    
    radio.send(message)
    print(z)
    
    sleep(10)
