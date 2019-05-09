import RPi.GPIO as GPIO
import time

def button_handler(pin):
    print("pin %s's value is %s" % (pin, GPIO.input(pin)))

def main():
    voice_change_pin = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(voice_change_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    # events can be GPIO.RISING, GPIO.FALLING, or GPIO.BOTH
    GPIO.add_event_detect(voice_change_pin, GPIO.BOTH,
                          callback=button_handler,
                          bouncetime=300)



if __name__ == '__main__':
    main()
    counter = 0
    try:
        while True:
            counter += 1
            print(counter)
            time.sleep(5)
    except KeyboardInterrupt:
        GPIO.cleanup()