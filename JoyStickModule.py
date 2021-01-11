
import pygame
from time import sleep

class Joystick:
    def __init__(self):
        # add controller
        pygame.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()
        # define the buttons
        self.buttons = {'x': 0, 'o': 0, 't': 0, 's': 0, 'L1': 0, 'R1': 0, 'L2': 0, 'R2': 0, 'share': 0, 'options': 0, 'axis0': 0., 'axis1': 0., 'axis3': 0., 'axis4': 0.}
        self.axiss = [0., 0., 0., 0., 0., 0.]

    # functions
    def get_js(self, name=''):
        # retrieve any events
        for event in pygame.event.get():  
            # Analog Sticks
            if event.type == pygame.JOYAXISMOTION:
                self.axiss[event.axis] = round(event.value, 2)
            # When button pressed
            elif event.type == pygame.JOYBUTTONDOWN:  
                for x, (key, val) in enumerate(self.buttons.items()):
                    if x < 10:
                        if self.controller.get_button(x): self.buttons[key] = 1
            # When button released
            elif event.type == pygame.JOYBUTTONUP:  
                for x, (key, val) in enumerate(self.buttons.items()):
                    if x < 10:
                        if event.button == x: self.buttons[key] = 0

        # change polartiy 1 and 4 to make more sense 
        self.buttons['axis0'], self.buttons['axis1'], self.buttons['axis3'], self.buttons['axis4'] = [self.axiss[0], (self.axiss[1] * -1), self.axiss[3], (self.axiss[4] * -1)]
        if name == '':
            return self.buttons
        else:
            return self.buttons[name]


def test_js(js):
    print(js.get_js())
    sleep(0.05)
    # print(getJS('axis4'))  # To get a single value
    # sleep(0.05)

if __name__ == '__main__':
    js = Joystick()
    print("program starting JoystickModule")
    try:
        while True:
            test_js(js)
    except KeyboardInterrupt:
        print("end of program")