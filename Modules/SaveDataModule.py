import os
import cv2
import pandas as pd
from datetime import datetime
import logconfig
import logging

class SaveData:
    def __init__(self):
        logging.info("SaveData was instanciated")
        # make list of images and steering
        self.img_list = []
        self.forward_list = []
        self.direction_list = []
        self.ultrasonic_list = []
        # make a new folder for images
        self.count_folder = 0
        self.make_new_folder()
        # count the images
        self.count = 0
    
    def make_new_folder(self):
        logging.debug("SaveData.make_new_folder was called")
        # get directory where to store images
        self.current_directory = os.path.join(os.getcwd(), "DataCollected")
        # look what folders are there
        while os.path.exists(os.path.join(self.current_directory,f"Data{str(self.count_folder)}")):
            self.count_folder += 1
        # add a new folder
        self.new_path = self.current_directory +"/Data" + str(self.count_folder)
        os.makedirs(self.new_path)
        logging.debug(f"SaveData.make_new_folder new folder was made {self.new_path}")
    
    def save_data(self,img,features):
        logging.debug(f"SaveData.save_data was called with img:{img.shape} features:{features}")
        # get the time
        now = datetime.now()
        timestamp = str(datetime.timestamp(now)).replace(".", "")
        # save image
        file_name = os.path.join(self.new_path,f"Image_{timestamp}.jpg")
        cv2.imwrite(file_name, img)
        logging.debug(f"image was saved as Image_{timestamp}.jpg")
        # add to lists
        self.img_list.append(file_name)
        self.forward_list.append(features["forward"])
        self.direction_list.append(features["direction"])
        self.ultrasonic_list.append(features["ultrasonic"])
    
    def save_log(self):
        logging.debug("SaveData.save_log was called")
        # make dictionary
        rawData = {"Image": self.img_list,
                    "Forward": self.forward_list,
                    "Direction": self.direction_list,
                    "Ultrasonic": self.ultrasonic_list}
        # save
        df = pd.DataFrame(rawData)
        df.to_csv(os.path.join(self.current_directory,f"log_{str(self.count_folder)}.csv"), index=False, header=False)
        logging.info(f"Logs were saved Total images {len(self.img_list)}")
    
if __name__ == "__main__":
    # start the logging
    logconfig.from_json(os.getcwd() + "/logconfig.json")
    log = logging.getLogger()
    logging.info("Program SaveDataModule started")
    try:
        # instanciate the SaveData class
        save = SaveData()
        # get the video capture
        cap = cv2.VideoCapture(0)
        # save 15 images
        for x in range(15):
            _, img = cap.read()
            save.save_data(img, 0.5)
            cv2.waitKey(1)
        save.save_log()
    except KeyboardInterrupt:
        pass
    finally:
        logging.info("Program SaveDataModule ended")

