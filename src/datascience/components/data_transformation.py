
from src.datascience.entity.config_entity import (DataTransformationConfig)
import pandas  as pd
import os
from src.datascience import logger
from sklearn.model_selection import train_test_split


class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config = config
    def train_test_split(self):
        ## uploading the data into the system
        data = pd.read_csv(self.config.data_path)
        ## splitting the data into training and test set
        train,test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir,'test.csv'),index = False)

        logger.info("splitted the data into training and testing data")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)