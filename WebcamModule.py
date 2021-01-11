import cv2
import os
import time
import sys

class Webcam:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def get_img(self, display = False, size=[480,240]):
        _, img = self.cap.read()
        img = cv2.resize(img,(size[0],size[1]))
        if display:
            cv2.imshow('IMG',img)
            key = cv2.waitKey(1) & 0xFF
        return img

if __name__ == '__main__':
    webcam = Webcam()
    myDirectory = os.path.join(os.getcwd(), 'test_images')
    try:
        print("program starting WebcamModule")
        if len(sys.argv) >= 2:
            if sys.argv[1] == "show":
                while True:
                    img = webcam.get_img(True)
            else:
                img = webcam.get_img()
                print("got image with shape: %s" % str(img.shape))
        else:
            print("need 1 more argument")
    except KeyboardInterrupt:
        print("end of program")