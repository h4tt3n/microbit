from microbit import *
import random

for x in range(5):
    for y in range(5):
        display.set_pixel(x, y, 4)

while True:

    for x in range(5):
        for y in range(5):
            current_level = display.get_pixel(x, y)
            rnd = random.choice([-1, 1])
            new_level = max(0, min(9, current_level + rnd))
            display.set_pixel(x, y, new_level)
    
    sleep(20)
