import math
import sys
import logconfig
import logging
from Modules.LedModule import *
from Modules.JoyStickModule import *
from Modules.MotorModule import *
from Modules.ServoModule import *
from Modules.WebcamModule import *
from Modules.BuzzerModule import *
from Modules.UltrasonicModule import *
from Modules.SaveDataModule import *
import threading
import tensorflow as tf
import numpy as np


class DataUsage:
    def __init__(self, display=False):
        logging.info("Program DataUsage initiated")
        # variables
        self.display=display
        self.old_look = [0,0,0,0]
        self.old_option = 0
        self.setting = 0
        self.servostands = [120,90]
        self.forward = 0
        self.direction = 0
        # initialize classes
        self.buzzer = Buzzer()
        self.motor = Motor()
        self.led = Led()
        self.servo = Servo()
        self.webcam = Webcam()
        self.ultrasonic = Ultrasonic()
        self.js = Joystick()
        # load model
        name = "model_0"
        self.model = tf.keras.models.load_model(f"./Assets/{name}.h5")
        # set servos
        self.servo.setServoPwm('0',self.servostands[0])
        self.servo.setServoPwm('1',self.servostands[1])
        # set color to geen
        self.led.color_wipe(self.led.strip, Color(128,128,128))
        # buzzer ot sign it works
        self.buzzer.run_seconds(1)

    def move_car(self, forward, direction):
        self.forward = forward
        self.direction = direction
        logging.debug(f"DataCollection.move_car was called with forward:{forward} direction:{direction}")
        # forward and input between -1 and 1, scale to 2000
        move = int(round(forward * 2000))
        # count for direction
        if direction > 0:
            # make right wheels slower
            direction = 1 - direction
            slowmove = int(round(move * direction))
            self.motor.set_motor_model(move, move, slowmove, slowmove)
        else:
            # make left wheels slower
            direction = 1 + direction
            slowmove = int(round(move * direction))
            self.motor.set_motor_model(slowmove, slowmove, move, move)
    
    def get_direction(self):
        img = [self.webcam.get_img(self.display, size=[66,200])]
        prediction = self.model.predict(np.asarray(img))
        print(float(prediction[0]))
        return float(prediction[0])
        
    
    def setting_recollor(self, sleep=0):
        time.sleep(sleep)
        if self.setting == 0: self.led.color_wipe(self.led.strip, Color(128,128,128))
        if self.setting == 1: self.led.color_wipe(self.led.strip, Color(0,255,0))
        if self.setting == 2: self.led.color_wipe(self.led.strip, Color(255,0,0))

    def run(self):
        # set the setting
        option = self.js.get_js('options')
        if option != self.old_option and option == 1 :
            self.setting += 1
            self.setting_recollor()
            threading.Thread(target=self.buzzer.run_seconds, args=(1,)).start()
        self.old_option = option

        # look at setting
        if self.setting == 0:
            # get controller input
            forward = self.js.get_js('axis1')
            direction = self.js.get_js('axis3')
            # move the car
            threading.Thread(target=self.move_car, args=(forward, direction,)).start()
            # get image
            if self.display: img = self.webcam.get_img(self.display)

        if self.setting == 1:
            # save the data
            direction = self.get_direction()
            threading.Thread(target=self.move_car, args=(0.7, direction,)).start()

        if self.setting == 2:
            self.setting = 0
            threading.Thread(target=self.setting_recollor, args=(1,)).start()


if __name__=='__main__':
    # start the logging
    logconfig.from_json(os.getcwd() + "/logconfig.json")
    log = logging.getLogger()
    logging.info("Program DataUsage started")
    # look if argument show is given
    data_usage = DataUsage()

    try:
        if len(sys.argv) >= 2:
            if sys.argv[1] == "show":
                data_usage.display = True
        while True:
            data_usage.run()
    except KeyboardInterrupt:
        pass
    finally:
        data_usage.motor.set_motor_model(0,0,0,0)
        data_usage.led.color_wipe(data_usage.led.strip, Color(0,0,0))
        logging.info("end of program")
