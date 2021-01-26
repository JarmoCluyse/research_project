import os
import sys
import cv2
import time
import logconfig
import logging

class Webcam:
    def __init__(self):
        logging.info("Webcam was instanciated")
        # get videocapture
        self.cap = cv2.VideoCapture(0)

    def get_img(self, display = False, size=[480,240]):
        logging.debug(f"Webcam.get_img was called with display:{display}, size={size}")
        # get the image
        _, img = self.cap.read()
        img = cv2.resize(img,(1920,1080))
        # if you want image shown only works on rpi with screen
        if display:
            logging.debug(f"Webcam.get_img showed an image")
            cv2.imshow('IMG',img)
            key = cv2.waitKey(1) & 0xFF
        img = cv2.resize(img,(size[0],size[1]))
        return img
    

if __name__ == '__main__':
    # start the logging
    logconfig.from_json(os.getcwd() + "/logconfig.json")
    log = logging.getLogger()
    logging.info("Program WebcamModule started")
    # instanciate the webcam class
    webcam = Webcam()
    try:
        if len(sys.argv) >= 2:
            # if you gave an argument show the image will be displayed
            if sys.argv[1] == "show":
                while True:
                    img = webcam.get_img(True)
        else:
            # print the shape of the image
            img = webcam.get_img()
            logging.debug(f"got image with shape: {str(img.shape)}")
    except KeyboardInterrupt:
        pass
    finally:
        logging.info("Program WebcamModule ended")