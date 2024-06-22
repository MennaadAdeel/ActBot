import pigpio
import time
import random

# Define GPIO pins for each servo
SERVO_PINS = {
    'neck': 17,
    'left_shoulder': 18,
    'left_elbow': 27,
    'left_wrist': 22,
    'right_shoulder': 23,
    'right_elbow': 24,
    'right_wrist': 25
}

# Initialize pigpio
pi = pigpio.pi()

# Function to set servo angle
def set_servo_angle(pin, angle):
    pulse_width = 500 + (angle * 2000 / 180)  # Convert angle to pulse width
    pi.set_servo_pulsewidth(pin, pulse_width)

# Function to wave hand
def wave_hand():
    for _ in range(3):
        set_servo_angle(SERVO_PINS['right_shoulder'], 90)
        set_servo_angle(SERVO_PINS['right_elbow'], 45)
        set_servo_angle(SERVO_PINS['right_wrist'], 45)
        time.sleep(0.5)
        set_servo_angle(SERVO_PINS['right_wrist'], 90)
        time.sleep(0.5)
    reset_servos()

# Function to clap hands
def clap_hands():
    for _ in range(3):
        set_servo_angle(SERVO_PINS['left_shoulder'], 90)
        set_servo_angle(SERVO_PINS['right_shoulder'], 90)
        set_servo_angle(SERVO_PINS['left_elbow'], 45)
        set_servo_angle(SERVO_PINS['right_elbow'], 45)
        time.sleep(0.5)
        set_servo_angle(SERVO_PINS['left_elbow'], 90)
        set_servo_angle(SERVO_PINS['right_elbow'], 90)
        time.sleep(0.5)
    reset_servos()

# Function to move head side to side
def move_head():
    for _ in range(3):
        set_servo_angle(SERVO_PINS['neck'], 45)
        time.sleep(0.5)
        set_servo_angle(SERVO_PINS['neck'], 135)
        time.sleep(0.5)
    reset_servos()

# Function to reset servos to initial position
def reset_servos():
    for pin in SERVO_PINS.values():
        set_servo_angle(pin, 90)
    time.sleep(0.5)

# Function to randomly move servos
def random_movements():
    while True:
        for pin in SERVO_PINS.values():
            angle = random.randint(0, 180)
            set_servo_angle(pin, angle)
        time.sleep(1)

# Function to perform startup actions
def startup_actions():
    wave_hand()
    random_movements()

# Clean up
def cleanup():
    reset_servos()
    pi.stop()

