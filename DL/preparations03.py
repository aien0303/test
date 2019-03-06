import numpy as np
from os import listdir
from random import shuffle
from PIL import Image

# image_path=["./data/A", "./data/B"]
image_path=[r"./training/images"]

def preprocess_to_data_file(data_dir_list):
    total_list=[] 
    with open('trainval.txt','w') as f:
        for index, data_dir in enumerate(data_dir_list):
            for filename in listdir(data_dir):
                f.write('{}\n'.format(filename.replace(' ','').replace('.jpg',''),index))

# train資料比例(ratio)
preprocess_to_data_file(image_path)