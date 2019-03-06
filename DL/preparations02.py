import numpy as np
from os import listdir
from random import shuffle
from PIL import Image

# image_path=["./data/A", "./data/B"]
image_path=[r"./p/B",r"./p/C"]

def preprocess_to_data_file(data_dir_list,ratio=0.8):
    total_list=[] 
    with open('total_data.txt','w') as f:
        for index, data_dir in enumerate(data_dir_list):
            for filename in listdir(data_dir):
                f.write('{} {}\n'.format(data_dir_list[index]+'/'+filename.replace(' ',''), index))
                total_list.append(data_dir_list[index]+'/'+filename.replace(' ','')+' '+str(index))
    shuffle(total_list)
    train_list=total_list[:int(ratio*len(total_list))]
    test_list=total_list[int(ratio*len(total_list)):]

    with open('train_data.txt','w') as f:
        for i in train_list:
            f.write(i+'\n')
    if (ratio==1):
        pass
    else:
        with open('test_data.txt','w') as f:
            for i in test_list:
                f.write(i+'\n')

# train資料比例(ratio)
preprocess_to_data_file(image_path,0.9)