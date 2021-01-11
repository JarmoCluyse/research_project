import time
from PCA9685 import PCA9685
class Motor:
    # on init connect to motors
    def __init__(self):
        self.pwm = PCA9685(0x40, debug=True)
        self.pwm.setPWMFreq(50)
        self.motordict = {"lu": [0, 1], "ll": [3, 2], "ru": [6, 7], "rl": [4, 5]}

    # make the duties in range
    def duty_range(self,duty1,duty2,duty3,duty4):
        if duty1>4095:
            duty1=4095
        elif duty1<-4095:
            duty1=-4095        
        
        if duty2>4095:
            duty2=4095
        elif duty2<-4095:
            duty2=-4095
            
        if duty3>4095:
            duty3=4095
        elif duty3<-4095:
            duty3=-4095
            
        if duty4>4095:
            duty4=4095
        elif duty4<-4095:
            duty4=-4095
        return duty1,duty2,duty3,duty4

    # move the weels
    def move_wheel(self,wheel,duty):
        if duty>0:
            self.pwm.setMotorPwm(self.motordict[wheel][0],duty)
            self.pwm.setMotorPwm(self.motordict[wheel][1],0)
        elif duty<0:
            self.pwm.setMotorPwm(self.motordict[wheel][0],0)
            self.pwm.setMotorPwm(self.motordict[wheel][1],abs(duty))
        else:
            self.pwm.setMotorPwm(self.motordict[wheel][0],4095)
            self.pwm.setMotorPwm(self.motordict[wheel][1],4095)
            
    # move all wheel
    def set_motor_model(self,duty1,duty2,duty3,duty4):
        duty1,duty2,duty3,duty4=self.duty_range(duty1,duty2,duty3,duty4)
        self.move_wheel("lu", duty1)
        self.move_wheel("ll", duty2)
        self.move_wheel("ru", duty3)
        self.move_wheel("rl", duty4)
            
            
PWM=Motor()
def test_movement():
    print("forward")
    PWM.set_motor_model(2000,2000,2000,2000)
    time.sleep(1)
    print("backward")
    PWM.set_motor_model(-2000,-2000,-2000,-2000)
    time.sleep(1)
    print("left")
    PWM.set_motor_model(0,0,2000,2000)
    time.sleep(1)
    print("right")
    PWM.set_motor_model(2000,2000,0,0)   
    time.sleep(1)
    print("stop")
    PWM.set_motor_model(0,0,0,0)  
                   
if __name__=='__main__':
    print("program starting MotorModule")
    try:
        test_movement()
    except KeyboardInterrupt:
        PWM.setMotorModel(0,0,0,0)
        print("end of program")
