import cv2
import os
import time
import sys

cap = cv2.VideoCapture(0)

def get_img(display= False, size=[480,240]):
    _, img = cap.read()
    img = cv2.resize(img,(size[0],size[1]))
    if display:
        cv2.imshow('IMG',img)
        key = cv2.waitKey(1) & 0xFF
    return img

def test_camera():
    for i in range(5):
        img = get_img()
        fileName = os.path.join(myDirectory,f'Image_{i+1}.jpg')
        cv2.imwrite(fileName, img)
        print("img %s saved" % (i+1))
        time.sleep(1)
    print("stop")

if __name__ == '__main__':
    myDirectory = os.path.join(os.getcwd(), 'test_images')
    try:
        print("program starting WebcamModule")
        if len(sys.argv) >= 2:
            if sys.argv[1] == "show":
                while True:
                    img = get_img(True)
            elif sys.argv[1] == "save":
                test_camera()
        else:
            print("need 1 more argument")
    except KeyboardInterrupt:
        print("end of program")