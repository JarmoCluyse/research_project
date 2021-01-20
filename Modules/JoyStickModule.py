
import os
import pygame
from time import sleep
import logconfig
import logging

class Joystick:
    def __init__(self):
        logging.info("Joystick was instanciated")
        # add controller
        pygame.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()
        # define the buttons
        self.buttons = {'x': 0, 'o': 0, 't': 0, 's': 0, 'L1': 0, 'R1': 0, 'L2': 0, 'R2': 0, 'share': 0, 'options': 0, 'axis0': 0., 'axis1': 0., 'axis3': 0., 'axis4': 0.}
        self.axiss = [0., 0., 0., 0., 0., 0.]
        logging.debug("controller was detected")

    # functions
    def get_js(self, name=''):
        logging.debug(f"Joystick.get_js was called with name:{name}")
        buttons_new = self.buttons
        axis_new = self.axiss
        # retrieve any events
        for event in pygame.event.get():  
            # Analog Sticks
            if event.type == pygame.JOYAXISMOTION:
                axis_new[event.axis] = round(event.value, 2)
            # When button pressed
            elif event.type == pygame.JOYBUTTONDOWN:  
                for x, (key, val) in enumerate(buttons_new.items()):
                    if x < 10:
                        if self.controller.get_button(x): buttons_new[key] = 1
            # When button released
            elif event.type == pygame.JOYBUTTONUP:  
                for x, (key, val) in enumerate(buttons_new.items()):
                    if x < 10:
                        if event.button == x: buttons_new[key] = 0

        # change polartiy 1 and 4 to make more sense 
        buttons_new['axis0'], buttons_new['axis1'], buttons_new['axis3'], buttons_new['axis4'] = [axis_new[0], (axis_new[1] * -1), axis_new[3], (axis_new[4] * -1)]
        logging.debug(buttons_new)
        if name == '':
            return buttons_new
        else:
            return buttons_new[name]


def test_js(js):
    logging.debug(f"JoystickModule.test_js was called")
    logging.info(js.get_js())
    # js.get_js()
    sleep(0.05)
    # logging.debug(getJS('axis4'))  # To get a single value
    # sleep(0.05)

if __name__ == '__main__':
    # start the logging
    logconfig.from_json(os.getcwd() + "/logconfig.json")
    log = logging.getLogger()
    logging.info("Program JoystickModule started")
    # try:
    # instanciate the Joystick class
    js = Joystick()
    try:
        while True:
            test_js(js)
    except KeyboardInterrupt:
        pass
    finally:
        logging.info("Program JoystickModule ended")
    # except Exception as ex:
        # logging.info(f"exception {ex}")
        