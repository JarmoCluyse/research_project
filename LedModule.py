import time
from rpi_ws281x import *
# LED strip configuration:
LED_COUNT      = 8      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
# Define functions which animate LEDs in various ways.

class Led:
    def __init__(self):
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
        B=R_G_B & 255
        G=R_G_B >> 8 & 255
        R=R_G_B >> 16 & 255 
        Led_type=["GRB","GBR","RGB", "RBG","BRG","BGR"]
        color = [Color(G,R,B),Color(G,B,R),Color(R,G,B),Color(R,B,G),Color(B,R,G),Color(B,G,R)]
        if order in Led_type:
            return color[Led_type.index(order)]

    def color_wipe(self,strip, color, wait_ms=50):
        # change all the leds
        color=self.LED_TYPR(self.ORDER,color)
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)
            self.strip.show()
    
    def semi_color_Wipe(self,side,R,G,B):
        # change one side the leds
        if side == "l":
            for led_i in self.ledlist_left:
                self.led_index(led_i, R, G, B)
        elif side == "r":
            for led_i in self.ledlist_right:
                self.led_index(led_i, R, G, B)


    def led_index(self,index,R,G,B):
        # change 1 led
        color=self.LED_TYPR(self.ORDER,Color(R,G,B))
        for i in range(8):
            if index & 0x01 == 1:
                self.strip.setPixelColor(i,color)
                self.strip.show()
            index=index >> 1


def test_led(led):
    # test every function
    print("red")
    led.color_wipe(led.strip, Color(255,0, 0))
    time.sleep(2)
    print("green")
    led.color_wipe(led.strip, Color(0, 255, 0))
    time.sleep(2)
    print("blue")
    led.color_wipe(led.strip, Color(0, 0, 255))
    time.sleep(2)
    led.color_wipe(led.strip, Color(0, 0, 0))
    print("left")
    led.semi_color_Wipe("l",255,125,0)
    time.sleep(2)
    led.semi_color_Wipe("l",0,0,0)
    led.semi_color_Wipe("r",255,125,0)
    print("right")
    time.sleep(2)
    print("1 led at a time")
    led.color_wipe(led.strip, Color(0, 0, 0))
    for led_i in led.ledlist:
        led.led_index(led_i,255,255,255)
        time.sleep(.5)
        led.led_index(led_i,0,0,0)

if __name__ == '__main__':
    led=Led()     
    print("program starting LedModule")
    try:
        while True:
            test_led(led)
    except KeyboardInterrupt:
        led.color_wipe(led.strip, Color(0,0,0),10)
        print("end of program")

        
            
        
                    




   
