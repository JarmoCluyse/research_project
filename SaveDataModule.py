import pandas as pd
import os
import cv2
from datetime import datetime

class SaveData:
    def __init__(self):
        # make list of images and steering
        self.imgList = []
        self.featureList = []
        # make a new folder for images
        self.countFolder = 0
        self.make_new_folder()
        # count the images
        self.count = 0
    
    def make_new_folder(self):
        self.myDirectory = os.path.join(os.getcwd(), 'DataCollected/')
        while os.path.exists(os.path.join(self.myDirectory,f'Data{str(self.countFolder)}')):
            # make new path
            self.countFolder += 1
        self.newPath = self.myDirectory +"/Data"+str(self.countFolder)
        os.makedirs(self.newPath)
    
    def saveData(self,img,features):
        # get the time
        now = datetime.now()
        timestamp = str(datetime.timestamp(now)).replace('.', '')
        # save image
        fileName = os.path.join(self.newPath,f'Image_{timestamp}.jpg')
        cv2.imwrite(fileName, img)
        # add to lists
        self.imgList.append(fileName)
        self.featureList.append(features)
        print(self.newPath)
    
    def saveLog(self):
        rawData = {'Image': self.imgList,
                    'Features': self.featureList}
        df = pd.DataFrame(rawData)
        df.to_csv(os.path.join(self.myDirectory,f'log_{str(self.countFolder)}.csv'), index=False, header=False)
        print('Log Saved')
        print('Total Images: ',len(self.imgList))
    
if __name__ == '__main__':
    save = SaveData()
    cap = cv2.VideoCapture(0)
    for x in range(10):
        _, img = cap.read()
        print(str(img.shape))
        save.saveData(img, 0.5)
        cv2.waitKey(1)
        # cv2.imshow("Image", img)
    save.saveLog()

