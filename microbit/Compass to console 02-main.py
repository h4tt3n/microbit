from microbit import *
import math

# Calibration is required for accurate magnetometer readings.
# Remove the comment below to calibrate on first run.
# compass.calibrate()

while True:
    # Get raw magnetometer values
    x = compass.get_x()
    y = compass.get_y()
    z = compass.get_z()

    # Calculate angle in radians using the X/Z plane
    # atan2 returns values from -pi to pi
    angle_rad = math.atan2(z, x)

    # Convert radians to degrees
    angle_deg = math.degrees(angle_rad)

    # Normalize to 0-360 degrees
    bearing = (angle_deg + 360) % 360

    print("X:{} Y:{} Z:{} Bearing: {:.2f}".format(x, y, z, bearing))

    sleep(100)