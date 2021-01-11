import os
import time
import RPi.GPIO as GPIO
import logconfig
import logging

class Ultrasonic:
    def __init__(self):
        logging.info("Ultrasonic was instanciated")
        # set GPIO pins
        GPIO.setwarnings(False)
        self.trigger_pin = 27
        self.echo_pin = 22
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin,GPIO.OUT)
        GPIO.setup(self.echo_pin,GPIO.IN)

    def send_trigger_pulse(self):
        # send a pulse
        GPIO.output(self.trigger_pin,True)
        time.sleep(0.00015)
        GPIO.output(self.trigger_pin,False)

    def wait_for_echo(self,value,timeout):
        # listen for a pulse
        count = timeout
        while GPIO.input(self.echo_pin) != value and count>0:
            count = count-1
     
    def get_distance(self):
        # get disctance
        distance_cm=[0,0,0,0,0]
        for i in range(3):
            self.send_trigger_pulse()
            self.wait_for_echo(True,10000)
            start = time.time()
            self.wait_for_echo(False,10000)
            finish = time.time()
            pulse_len = finish-start
            distance_cm[i] = pulse_len/0.000058
        distance_cm=sorted(distance_cm)
        return int(distance_cm[2])
                
def test_ultrasonic(ultrasonic):
    while True:
        distance = ultrasonic.get_distance()
        logging.debug(f"distance was {distance} cm")
        time.sleep(1)
        
                      
if __name__ == '__main__':
    from PCA9685 import PCA9685
    # start the logging
    logconfig.from_json(os.getcwd() + "/logconfig.json")
    log = logging.getLogger()
    logging.info("Program UltrasonicModule started")
    # instanciate class
    ultrasonic=Ultrasonic()   
    try:
        test_ultrasonic(ultrasonic)
    except KeyboardInterrupt:
        pass
    finally:
        logging.info("Program UltrasonicModule ended")
else:
    from Modules.PCA9685 import PCA9685

