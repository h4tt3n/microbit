from microbit import *
from math import *
import radio

# Set up radio
radio.on()
radio.config(channel=42)  # Must match receiver's channel

# Define motor control pins
MOTOR1_PIN1 = pin12
MOTOR1_PIN2 = pin8
MOTOR2_PIN1 = pin16
MOTOR2_PIN2 = pin0

def motor_run(pin1, pin2, speed):
    if(speed > 0):
        pin1.write_analog(speed * 1023)
        pin2.write_digital(0)  
    elif(speed < 0):
        pin1.write_digital(0) 
        pin2.write_analog(-speed * 1023)
    else:
        pin1.write_digital(0)
        pin2.write_digital(0)


while True:

    message = radio.receive()
    
    if message:
        try:
            # Deserialize data (split by comma)
            angle_str, a_str, b_str = message.split(",")
            angle = float(angle_str)  # Convert string to float
            
            #print("Angle:", angle, "A:", a_str, "B:", b_str)  # Display data

            if(a_str == "True"):
                
                motor1_speed = 0.5 + angle
                motor2_speed = 0.5 - angle
            
                motor_run(MOTOR1_PIN1, MOTOR1_PIN2, motor1_speed)
                motor_run(MOTOR2_PIN1, MOTOR2_PIN2, motor2_speed)

                #print("forward", motor1_speed, motor2_speed)
                
            if(b_str == "True"):
                
                motor1_speed = - 0.5 - angle
                motor2_speed = - 0.5 + angle
            
                motor_run(MOTOR1_PIN1, MOTOR1_PIN2, motor1_speed)
                motor_run(MOTOR2_PIN1, MOTOR2_PIN2, motor2_speed)

                #print("reverse", motor1_speed, motor2_speed)

            elif(a_str == "False" and b_str == "False"):
                motor_run(MOTOR1_PIN1, MOTOR1_PIN2, 0)
                motor_run(MOTOR2_PIN1, MOTOR2_PIN2, 0)

                #print("stop")
            
        except ValueError:
            print("Invalid message:", message)  # Handle errors
    
    sleep(1)
