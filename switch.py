import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
GPIO.setup(17, GPIO.OUT)

try:
    while True:
        if GPIO.input(4) == 0 :
            print("Open")
            GPIO.output(17, GPIO.LOW) # LED OFF
        else :
            print("Closed")
            GPIO.output(17, GPIO.HIGH) # LED ON

except KeyboardInterrupt:
    print("\nInterrupted!")

finally:
    GPIO.cleanup()