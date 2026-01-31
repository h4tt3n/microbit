from microbit import *
from math import *
import radio

# Set up radio
radio.on()
radio.config(channel=42)  # Must match receiver's channel

while True:

    message = radio.receive()
    
    if message:
        try:
            # Deserialize data (split by comma)
            angle_str, a_str, b_str = message.split(",")
            angle = float(angle_str)  # Convert string to float
            
            print("Angle:", angle, "A:", a_str, "B:", b_str)  # Display data
            
        except ValueError:
            print("Invalid message:", message)  # Handle errors
    
    sleep(10)
