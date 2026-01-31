from microbit import i2c, sleep
import random

# PCA9685 I2C address (default)
PCA9685_ADDR = 0x40
MODE1 = 0x00
PRESCALE = 0xFE
LED0_ON_L = 0x06
LED0_OFF_L = 0x08

# Function to write to PCA9685 registers
def write_register(register, value):
    i2c.write(PCA9685_ADDR, bytes([register, value]))

# Function to read from PCA9685 registers
def read_register(register):
    i2c.write(PCA9685_ADDR, bytes([register]))
    return i2c.read(PCA9685_ADDR, 1)[0]

# Initialize the PCA9685 and set PWM frequency
def init_pca9685(frequency=50):
    write_register(MODE1, 0x00)  # Reset PCA9685
    prescale = int(25000000 / (4096 * frequency) - 1)
    old_mode = read_register(MODE1)
    new_mode = (old_mode & 0x7F) | 0x10  # Sleep mode
    write_register(MODE1, new_mode)
    write_register(PRESCALE, prescale)
    write_register(MODE1, old_mode)
    sleep(5)
    write_register(MODE1, old_mode | 0xA1)  # Auto increment enabled

# Set PWM signal for a specific channel
def set_pwm(channel, on, off):
    register = LED0_ON_L + 4 * channel
    i2c.write(PCA9685_ADDR, bytes([register, on & 0xFF, on >> 8, off & 0xFF, off >> 8]))

# Convert an angle (0-180) to a pulse width (0-4095) and set servo position
def set_servo_angle(channel, angle):
    min_pulse = 0  # Adjust as necessary
    max_pulse = 600  # Adjust as necessary
    pulse = min_pulse + (angle / 180) * (max_pulse - min_pulse)
    set_pwm(channel, 0, int(pulse))

# Test function to move a servo back and forth
def test_servo(channel):

    while True:
        set_servo_angle(channel, 3)
        sleep(500)
        angle = 180 #random.randrange(0, 180)
        set_servo_angle(channel, angle)
        sleep(500)
    
    #print("Testing servo on channel", channel)
    #for angle in range(0, 181, 10):
    #    set_servo_angle(channel, angle)
    #    sleep(300)
    #for angle in range(180, -1, -10):
    #    set_servo_angle(channel, angle)
    #    sleep(300)

# Initialize and run the test
init_pca9685()
test_servo(0)  # Test servo on channel 0