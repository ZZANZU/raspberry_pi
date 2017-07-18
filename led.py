import RPi.GPIO as GPIO
import time

def blink(pin):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1) #second
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)
    return

GPIO.setmode(GPIO.BCM)
GPIO.setup (17, GPIO.OUT)

try:
    while True:
        blink(17)

except KeyboardInterrupt:
    print("\nInterrupted!")

finally:
    GPIO.cleanup()