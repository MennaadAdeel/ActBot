import RPi.GPIO as GPIO
import time

# Define GPIO pins for servos
SERVO_PIN_ARM = 17
SERVO_PIN_NECK = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN_ARM, GPIO.OUT)
GPIO.setup(SERVO_PIN_NECK, GPIO.OUT)

arm_servo = GPIO.PWM(SERVO_PIN_ARM, 50)  # 50 Hz
neck_servo = GPIO.PWM(SERVO_PIN_NECK, 50)

arm_servo.start(0)
neck_servo.start(0)

def set_servo_angle(servo, angle):
    duty_cycle = (angle / 18) + 2
    GPIO.output(servo, True)
    servo.ChangeDutyCycle(duty_cycle)
    time.sleep(1)
    GPIO.output(servo, False)
    servo.ChangeDutyCycle(0)

# Example usage
set_servo_angle(arm_servo, 90)  # Move arm to 90 degrees
set_servo_angle(neck_servo, 45)  # Move neck to 45 degrees

arm_servo.stop()
neck_servo.stop()
GPIO.cleanup()
