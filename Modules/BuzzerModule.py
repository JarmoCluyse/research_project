import os
import time
import RPi.GPIO as GPIO
import logconfig
import logging

GPIO.setwarnings(False)
Buzzer_Pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(Buzzer_Pin,GPIO.OUT)

class Buzzer:
    def __init__(self):
        GPIO.setwarnings(False)
        Buzzer_Pin = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Buzzer_Pin,GPIO.OUT)

    def run(self,command):
        if command!="0":
            GPIO.output(Buzzer_Pin,True)
        else:
            GPIO.output(Buzzer_Pin,False)
        logging.debug(f"buzzer set to {command}")

if __name__=='__main__':
    # start the logging
    logconfig.from_json(os.getcwd() + "/logconfig.json")
    log = logging.getLogger()
    logging.info("Program BuzzerModule started")
    # instanciate the buzzer class
    B = Buzzer()
    try:
        B.run('1')
        time.sleep(3)
        B.run('0')
    except KeyboardInterrupt:
        pass
    finally:
        logging.info("Program BuzzerModule ended")
        B.run('0')





