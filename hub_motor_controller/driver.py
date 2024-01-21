import RPi.GPIO as GPIO
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


def go(sleep): 
    GPIO.output(LEFT_DIR_PIN, True)
    GPIO.output(LEFT_BRAKE_PIN, False)

    motorl = GPIO.PWM(LEFT_PWM_PIN, 50)
    motorl.start(0)
    motorl.ChangeDutyCycle(20)

    time.sleep(sleep)
    GPIO.cleanup((LEFT_PWM_PIN))

def brake(sleep): 
    GPIO.output(LEFT_BRAKE_PIN, True)
    time.sleep(sleep)

def main():
    init()
    sleep_time = 0.030

    while True:
        go(sleep_time)
        time.sleep(2)
        brake(sleep_time)
        time.sleep(2)

if __name__ == "__main__":
    main()