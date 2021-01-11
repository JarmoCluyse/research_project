import pandas as pd
import os
import cv2
from datetime import datetime
import logging
import logconfig

class SaveData:
    def __init__(self):
        # make list of images and steering
        self.img_list = []
        self.feature_list = []
        # make a new folder for images
        self.count_folder = 0
        self.make_new_folder()
        # count the images
        self.count = 0

    
    def make_new_folder(self):
        # get directory where to store images
        self.current_directory = os.path.join(os.getcwd(), 'DataCollected')
        # look what folders are there
        while os.path.exists(os.path.join(self.current_directory,f'Data{str(self.count_folder)}')):
            self.count_folder += 1
        # add a new folder
        self.new_path = self.current_directory +"/Data"+str(self.count_folder)
        os.makedirs(self.new_path)
    
    def save_data(self,img,features):
        # get the time
        now = datetime.now()
        timestamp = str(datetime.timestamp(now)).replace('.', '')
        # save image
        file_name = os.path.join(self.new_path,f'Image_{timestamp}.jpg')
        cv2.imwrite(file_name, img)
        # add to lists
        self.img_list.append(file_name)
        self.feature_list.append(features)
    
    def save_log(self):
        # make dictionary
        rawData = {'Image': self.img_list,
                    'Features': self.feature_list}
        # save
        df = pd.DataFrame(rawData)
        df.to_csv(os.path.join(self.current_directory,f'log_{str(self.count_folder)}.csv'), index=False, header=False)
        print('Log Saved')
        print('Total Images: ',len(self.img_list))
    
if __name__ == '__main__':
    logconfig.from_json(os.getcwd() + "/logconfig.json")
    log = logging.getLogger()
    save = SaveData()
    cap = cv2.VideoCapture(0)
    for x in range(15):
        _, img = cap.read()
        save.save_data(img, 0.5)
        cv2.waitKey(1)
    save.save_log()

