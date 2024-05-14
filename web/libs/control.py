import RPi.GPIO as GPIO
import time

LEFT_PWM_PIN   = 32
LEFT_DIR_PIN   = 31
LEFT_BRAKE_PIN = 29

RIGHT_PWM_PIN   = 35
RIGHT_DIR_PIN   = 37
RIGHT_BRAKE_PIN = 36

init_called = False

def init():
    global init_called
    if not init_called:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        GPIO.setup(LEFT_PWM_PIN, GPIO.OUT)
        GPIO.setup(LEFT_DIR_PIN, GPIO.OUT)
        GPIO.setup(LEFT_BRAKE_PIN, GPIO.OUT)

        GPIO.setup(RIGHT_PWM_PIN, GPIO.OUT)
        GPIO.setup(RIGHT_DIR_PIN, GPIO.OUT)
        GPIO.setup(RIGHT_BRAKE_PIN, GPIO.OUT)

        init_called = True

init()

def brake(sleep=0.03): 
    GPIO.output(LEFT_BRAKE_PIN, True)
    GPIO.output(RIGHT_BRAKE_PIN, True)
    time.sleep(sleep)

def left_motor(value, sleep=0.03):
    GPIO.output(LEFT_BRAKE_PIN, False)

    if value > 0:
        GPIO.output(LEFT_DIR_PIN, True)  # forward
    else:
        GPIO.output(LEFT_DIR_PIN, False) # reverse
        value *= -1
        value += 20 # the motor struggles to reverse for whatever reason

    motorl = GPIO.PWM(LEFT_PWM_PIN, 50)
    motorl.start(0)
    motorl.ChangeDutyCycle(value)

    time.sleep(sleep)
    
def right_motor(value, sleep=0.03):
    GPIO.output(RIGHT_BRAKE_PIN, False)

    if value > 0:
        GPIO.output(RIGHT_DIR_PIN, True)  # forward
    else:
        GPIO.output(RIGHT_DIR_PIN, False) # reverse
        value *= -1
        value += 20 # the motor struggles to reverse for whatever reason

    motorl = GPIO.PWM(RIGHT_PWM_PIN, 50)
    motorl.start(0)
    motorl.ChangeDutyCycle(value)

    time.sleep(sleep)

def receive(data):    
    x = int(data.get('x', 0)) # [-100, 100] left, right
    y = int(data.get('y', 0)) # [-100, 100] reverse, forward
    # print(f"received x:{x}, y:{y}")

    left_motor_y = 0
    left_motor_x = 0
    right_motor_y = 0
    right_motor_x = 0

    if x == 0 and y == 0:
        brake()
        return
    if y > 0:
        left_motor_y = map_value(y, 0, 100, 0, 40)   # forward
        right_motor_y = map_value(y, 0, 100, 0, 40)
    else:
        left_motor_y = map_value(y, -100, 0, -40, 0) # reverse
        right_motor_y = map_value(y, -100, 0, -40, 0)
    if x > 0:
        left_motor_x = map_value(x, 0, 100, 0, 40)   # turn right
    else:
        right_motor_x = map_value(x, -100, 0, 40, 0) # turn left

    # TODO: PID control

    left_motor_value = left_motor_y + left_motor_x
    right_motor_value = right_motor_y + right_motor_x
    print(f"mapped left_motor_value:{left_motor_value}, right_motor_value:{right_motor_value}")

    left_motor(left_motor_value)
    right_motor(right_motor_value)

def map_value(value, in_min, in_max, out_min, out_max):
    """
    Params:
    - value (int): input value to be mapped.
    - in_min (int): minimum value of input range.
    - in_max (int): maximum value of input range.
    - out_min (int): minimum value of output range.
    - out_max (int): maximum value of output range.

    Returns:
    float: mapped value in output range.

    """
    return round((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min, 2)