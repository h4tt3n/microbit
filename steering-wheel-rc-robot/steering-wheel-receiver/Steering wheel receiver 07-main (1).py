from microbit import *
import radio

# Define motor control pins
MOTOR1_PIN1 = pin12
MOTOR1_PIN2 = pin8
MOTOR2_PIN1 = pin16
MOTOR2_PIN2 = pin0

# Clear pins
MOTOR1_PIN1.write_digital(0)
MOTOR1_PIN2.write_digital(0)
MOTOR2_PIN1.write_digital(0)
MOTOR2_PIN2.write_digital(0)

# Set up radio
radio.on()
radio.config(group=42, channel=42, power=7)

def motor_run(pin1, pin2, speed):
    speed = max(-1, min(1, speed))  # Ensure speed stays in range [-1,1]
    
    if speed > 0:
        pin1.write_analog(int(speed * 1023))
        pin2.write_digital(0)  
    elif speed < 0:
        pin1.write_digital(0) 
        pin2.write_analog(int(-speed * 1023))
    else:
        pin1.write_digital(0)
        pin2.write_digital(0)

while True:
    message = radio.receive()
    
    if message:
        try:
            # Deserialize data
            angle_str, a_str, b_str = message.split(",")
            angle = float(angle_str)
            a_pressed = int(a_str)
            b_pressed = int(b_str)

            # Reverse
            if a_pressed and not b_pressed:
                motor1_speed = -0.5 - angle
                motor2_speed = -0.5 + angle

            # Forward
            elif b_pressed and not a_pressed:
                motor1_speed = 0.5 + angle
                motor2_speed = 0.5 - angle

            # Fast forward
            elif a_pressed and b_pressed:
                motor1_speed = 1.0 - angle
                motor2_speed = 1.0 + angle

            # Stop
            else:
                motor1_speed = 0
                motor2_speed = 0

            motor_run(MOTOR1_PIN1, MOTOR1_PIN2, motor1_speed)
            motor_run(MOTOR2_PIN1, MOTOR2_PIN2, motor2_speed)

        except ValueError:
            print("Invalid message:", message)

    sleep(10)  # Faster response time
