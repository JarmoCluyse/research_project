import os
import time
import logconfig
import logging

class Motor:
    def __init__(self):
        logging.info("Motor was instanciated")
        # connect to motors
        self.pwm = PCA9685(0x40, debug=True)
        self.pwm.setPWMFreq(50)
        # make a list of the different motors
        self.motordict = {"lu": [0, 1], "ll": [3, 2], "ru": [6, 7], "rl": [4, 5]}

    def duty_range(self,duty1,duty2,duty3,duty4):
        logging.debug(f"Motor.duty_range was called with duty1:{duty1} duty2:{duty2} duty3:{duty3} duty4:{duty4}")
        # make the duties in range
        for duty in [duty1,duty2,duty3,duty4]:
            if duty>4095:
                duty=4095
            elif duty<-4095:
                duty=-4095        
        return duty1,duty2,duty3,duty4

    def move_wheel(self,wheel,duty):
        logging.debug(f"Motor.move_wheel was called with wheel:{wheel} duty:{duty}")
        # set the pwm of the motor given
        if duty>0:
            self.pwm.setMotorPwm(self.motordict[wheel][0],duty)
            self.pwm.setMotorPwm(self.motordict[wheel][1],0)
        elif duty<0:
            self.pwm.setMotorPwm(self.motordict[wheel][0],0)
            self.pwm.setMotorPwm(self.motordict[wheel][1],abs(duty))
        else:
            self.pwm.setMotorPwm(self.motordict[wheel][0],4095)
            self.pwm.setMotorPwm(self.motordict[wheel][1],4095)
            
    def set_motor_model(self,duty1,duty2,duty3,duty4):
        logging.debug(f"Motor.set_motor_model was called with duty1:{duty1} duty2:{duty2} duty3:{duty3} duty4:{duty4}")
        # set all wheels
        duty1,duty2,duty3,duty4=self.duty_range(duty1,duty2,duty3,duty4)
        self.move_wheel("lu", duty1)
        self.move_wheel("ll", duty2)
        self.move_wheel("ru", duty3)
        self.move_wheel("rl", duty4)
        # logging.debug(f"wheels where set to lu:{duty1} ll:{duty2} ru:{duty3} rl:{duty4}")
            
def test_movement(PWM):
    logging.debug(f"MotorModule.test_movement was called")
    # test the different movements
    logging.info("forward")
    PWM.set_motor_model(2000,2000,2000,2000)
    time.sleep(1)
    logging.info("backward")
    PWM.set_motor_model(-2000,-2000,-2000,-2000)
    time.sleep(1)
    logging.info("left")
    PWM.set_motor_model(0,0,2000,2000)
    time.sleep(1)
    logging.info("right")
    PWM.set_motor_model(2000,2000,0,0)   
    time.sleep(1)

if __name__=='__main__':
    # import modules
    from PCA9685 import PCA9685
    # start logging
    logconfig.from_json(os.getcwd() + "/logconfig.json")
    log = logging.getLogger()
    logging.info("Program MotoModule started")
    # instanciate motor class
    PWM=Motor()               
    try:
        # test the motor
        test_movement(PWM)
    except KeyboardInterrupt:
        pass
    finally:
        PWM.set_motor_model(0,0,0,0)
        logging.info("Program MotorModule ended")
else:
    from Modules.PCA9685 import PCA9685

