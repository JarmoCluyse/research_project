import os
import time
import logconfig
import logging

class Servo:
    def __init__(self):
        logging.info("Servo was instanciated")
        # connect to pca
        self.PwmServo = PCA9685(0x40, debug=True)
        self.PwmServo.setPWMFreq(50)
        # set the servo to begin position
        logging.debug("Servos where set to begin position")
        self.PwmServo.setServoPulse(8,1500)
        self.PwmServo.setServoPulse(9,1500)

    def setServoPwm(self,channel,angle,error=10):
        # set the servo to the desired angle
        angle=int(angle)
        if channel=='0':
            self.PwmServo.setServoPulse(8,2500-int((angle+error)/0.09))
        elif channel=='1':
            self.PwmServo.setServoPulse(9,500+int((angle+error)/0.09))
        # logging.debug(f"servo {channel} set to {angle}°")

def test_servo(servo):
    # test the movement of the servo
    logging.debug(f"both set to 90°")
    servo.setServoPwm('0',90)
    servo.setServoPwm('1',80)
    time.sleep(1)
    logging.debug(f"servo 0 set to 150")
    servo.setServoPwm('0',150)
    time.sleep(1)
    logging.debug(f"servo 1 set to 120")
    servo.setServoPwm('1',120)
    time.sleep(1)
    

if __name__ == '__main__':
    # import module
    from PCA9685 import PCA9685
    logconfig.from_json(os.getcwd() + "/logconfig.json")
    log = logging.getLogger()
    logging.info("Program ServoModule started")
    # instanciate the servo class
    servo=Servo()
    try :
        while True:
            test_servo(servo)
    except KeyboardInterrupt:
        pass
    finally:
        logging.debug("servo set to original state")
        pwm.setServoPwm('0',120)
        pwm.setServoPwm('1',90)
        logging.info("Program ServoModule ended")
else:
    from Modules.PCA9685 import PCA9685
    

    
       



    
