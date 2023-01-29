import RPi.GPIO as GPIO

# GPIO.BCM set GPIO numbers to system on chip
# GPIO.BOARD set GPIO numbers to physical board numbers
GPIO.setmode(GPIO.BCM)

# pin 21 as input with onboard pull up ressistor, conntect pin to ground toggle from 1 to 0
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# if button is pressed return True
def pressed():
    return not GPIO.input(21)
    