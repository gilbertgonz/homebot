# import RPi.GPIO as GPIO
import time

# To install:
# sudo apt-get -y install python3-rpi.gpio

LEFT_PWM_PIN   = 32
LEFT_DIR_PIN   = 31
LEFT_BRAKE_PIN = 29

def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    GPIO.setup(LEFT_PWM_PIN, GPIO.OUT)
    GPIO.setup(LEFT_DIR_PIN, GPIO.OUT)
    GPIO.setup(LEFT_BRAKE_PIN, GPIO.OUT)


def forward(sleep): 
    GPIO.output(LEFT_DIR_PIN, True)
    GPIO.output(LEFT_BRAKE_PIN, False)
    

    motorl = GPIO.PWM(LEFT_PWM_PIN, 50)
    motorl.start(0)
    motorl.ChangeDutyCycle(40)

    time.sleep(sleep)
    GPIO.cleanup((LEFT_PWM_PIN))

def reverse(sleep): 
    GPIO.output(LEFT_DIR_PIN, False)
    GPIO.output(LEFT_BRAKE_PIN, False)

    motorl = GPIO.PWM(LEFT_PWM_PIN, 50)
    motorl.start(0)
    motorl.ChangeDutyCycle(40)

    time.sleep(sleep)
    GPIO.cleanup((LEFT_PWM_PIN))

def brake(sleep): 
    GPIO.output(LEFT_BRAKE_PIN, True)
    time.sleep(sleep)

# TODO: translate raw data to move motor
def move(data):
    x = data.get('x', 0)
    y = data.get('y', 0)
    # print(f"recived x:{x}, y:{y}")

def main():
    init()
    sleep_time = 0.030

    while True:
        brake(sleep_time)
        forward(sleep_time)
        time.sleep(2)
        brake(sleep_time)
        reverse(sleep_time)
        time.sleep(2)

if __name__ == "__main__":
    main()