import os
from rpi_ws281x import *
import time
import logconfig
import logging

# LED strip configuration:
LED_COUNT      = 8      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

class Led:
    def __init__(self):
        logging.info("Led was instanciated")
        #Control the sending order of color data
        self.ORDER = "RGB"  
        # Create NeoPixel object with appropriate configuration.
        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        # Intialize the library (must be called once before other functions).
        self.strip.begin()
        # leds in this config
        self.ledlist = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]
        self.ledlist_left = [0x04, 0x08, 0x10, 0x20]
        self.ledlist_right = [0x01, 0x02, 0x40, 0x80]

    def LED_TYPR(self,order,R_G_B):
        logging.debug(f"Led.LED_TYPR was called with order:{order} R_G_B:{R_G_B}")
        B=R_G_B & 255
        G=R_G_B >> 8 & 255
        R=R_G_B >> 16 & 255 
        Led_type=["GRB","GBR","RGB", "RBG","BRG","BGR"]
        color = [Color(G,R,B),Color(G,B,R),Color(R,G,B),Color(R,B,G),Color(B,R,G),Color(B,G,R)]
        if order in Led_type:
            return color[Led_type.index(order)]

    def color_wipe(self,strip, color, wait_ms=50):
        logging.debug(f"Led.color_wipe was called with strip:{strip} color:{color} wait_ms:{wait_ms}")
        # change all the leds
        color=self.LED_TYPR(self.ORDER,color)
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)
            self.strip.show()
    
    def semi_color_Wipe(self,side,R,G,B):
        logging.debug(f"Led.semi_color_Wipe was called with side:{side} R:{R} G:{G} B:{B}")
        # change one side the leds
        if side == "l":
            for led_i in self.ledlist_left:
                self.led_index(led_i, R, G, B)
        elif side == "r":
            for led_i in self.ledlist_right:
                self.led_index(led_i, R, G, B)


    def led_index(self,index,R,G,B):
        logging.debug(f"Led.led_index was called with index:{index} R:{R} G:{G} B:{B}")
        # change 1 led
        color=self.LED_TYPR(self.ORDER,Color(R,G,B))
        for i in range(8):
            if index & 0x01 == 1:
                self.strip.setPixelColor(i,color)
                self.strip.show()
            index=index >> 1
        logging.debug(f"led_index {index} was set to: {R}, {G}, {B}")


def test_led(led):
    logging.debug(f"LedModule.test_led was called")
    # test every function
    logging.info("color red")
    led.color_wipe(led.strip, Color(255,0, 0))
    time.sleep(2)
    logging.info("color green")
    led.color_wipe(led.strip, Color(0, 255, 0))
    time.sleep(2)
    logging.info("color blue")
    led.color_wipe(led.strip, Color(0, 0, 255))
    time.sleep(2)
    led.color_wipe(led.strip, Color(0, 0, 0))
    logging.info("left")
    led.semi_color_Wipe("l",255,125,0)
    time.sleep(2)
    led.semi_color_Wipe("l",0,0,0)
    led.semi_color_Wipe("r",255,125,0)
    logging.info("right")
    time.sleep(2)
    logging.info("1 led at a time")
    led.color_wipe(led.strip, Color(0, 0, 0))
    for led_i in led.ledlist:
        led.led_index(led_i,255,255,255)
        time.sleep(.5)
        led.led_index(led_i,0,0,0)

if __name__ == '__main__':
    # start the logging
    logconfig.from_json(os.getcwd() + "/logconfig.json")
    log = logging.getLogger()
    logging.info("Program LedModule started")
    # instanciate the Led class
    led=Led()    
    try:
        while True:
            test_led(led)
    except KeyboardInterrupt:
        pass
    finally:
        led.color_wipe(led.strip, Color(0,0,0),10)
        logging.info("Program LedModule ended")

        
            
        
                    




   
