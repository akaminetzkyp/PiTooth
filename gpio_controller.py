import RPi.GPIO as GPIO


class GPIOController:
    button_pin = 17

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(GPIOController.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    @staticmethod
    def block_until_press():
        while True:
            state = GPIO.input(GPIOController.button_pin)
            if not state:
                return
