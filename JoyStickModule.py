# -This module get the joystick values
# and puts them in a single dictionary in realtime.
# -The values can be accessed through the keys

# imports
import pygame
from time import sleep

# controller
pygame.init()
controller = pygame.joystick.Joystick(0)
controller.init()
print(controller.get_numbuttons)

buttons = {'x': 0, 'o': 0, 't': 0, 's': 0,
           'L1': 0, 'R1': 0, 'L2': 0, 'R2': 0,
           'share': 0, 'options': 0,
           'axis0': 0., 'axis1': 0., 'axis3': 0., 'axis4': 0.}
axiss = [0., 0., 0., 0., 0., 0.]

# functions
def get_js(name=''):
    global buttons
    # retrieve any events
    for event in pygame.event.get():  
        # Analog Sticks
        if event.type == pygame.JOYAXISMOTION:
            axiss[event.axis] = round(event.value, 2)
        # When button pressed
        elif event.type == pygame.JOYBUTTONDOWN:  
            for x, (key, val) in enumerate(buttons.items()):
                if x < 10:
                    if controller.get_button(x): buttons[key] = 1
        # When button released
        elif event.type == pygame.JOYBUTTONUP:  
            for x, (key, val) in enumerate(buttons.items()):
                if x < 10:
                    if event.button == x: buttons[key] = 0

    # change polartiy 1 and 4 to make more sense 
    buttons['axis0'], buttons['axis1'], buttons['axis3'], buttons['axis4'] = [axiss[0], (axiss[1] * -1), axiss[3], (axiss[4] * -1)]
    if name == '':
        return buttons
    else:
        return buttons[name]


def test_js():
    # print(get_js())
    sleep(0.05)
    # print(getJS('axis4'))  # To get a single value
    # sleep(0.05)


if __name__ == '__main__':
    print("program starting JoystickModule")
    try:
        while True:
            test_js()
    except KeyboardInterrupt:
        print("end of program")