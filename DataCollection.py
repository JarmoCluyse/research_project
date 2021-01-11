import math
import sys
import logconfig
import logging
from Modules.LedModule import *
from Modules.JoyStickModule import *
from Modules.MotorModule import *
from Modules.ServoModule import *
from Modules.WebcamModule import *

# variables
display=False
old_look = [0,0,0,0]
servostands = [120,90]

def move_car(forward, direction):
    # forward and input between -1 and 1
    # scale to motor
    move = int(round(forward * 2000))
    # count for direction
    if direction > 0:
        direction = 1 - direction
        slowmove = int(round(move * direction))
        motor.set_motor_model(move, move, slowmove, slowmove)
    else:
        direction = 1 + direction
        slowmove = int(round(move * direction))
        motor.set_motor_model(slowmove, slowmove, move, move)

def look_around():
    # code to change serbo motors with controller
    global old_look, servostands
    look = [js.get_js('s'), js.get_js('o'), js.get_js('t'), js.get_js('x')]
    for i in range(4):
        if look[i] != old_look[i] and look[i] == 1 :
            if i == 0: servostands[0] -=2
            if i == 1: servostands[0] +=2
            if i == 2: servostands[1] +=2
            if i == 3: servostands[1] -=2
    old_look = look
    servo.setServoPwm('0',servostands[0])
    servo.setServoPwm('1',servostands[1])

if __name__=='__main__':
    # start the logging
    logconfig.from_json(os.getcwd() + "/logconfig.json")
    log = logging.getLogger()
    logging.info("Program DataCollection started")
    # initialize classes
    motor=Motor()
    led=Led()
    servo=Servo()
    webcam = Webcam()
    js = Joystick()
    # main program
    try:
        # look if argument show is given
        if len(sys.argv) >= 2:
            if sys.argv[1] == "show":
                display = True
        # set color to geen
        led.color_wipe(led.strip, Color(0,128,0))
        while True:
            # get controller input
            forward = js.get_js('axis1')
            direction = js.get_js('axis3')
            # move the car
            move_car(forward, direction)
            # look if button is pressed
            look_around()
            # get image
            img = webcam.get_img(display)

    except KeyboardInterrupt:
        pass
    finally:
        motor.set_motor_model(0,0,0,0)
        led.color_wipe(led.strip, Color(0,0,0))
        logging.info("end of program")
