import os
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import cv2

model = load_model('h5/number.h5')
model.summary()
predict_dir = './Demo03'
test = os.listdir(predict_dir)

for index, data_dir in enumerate(test):
    new=predict_dir+'/'+data_dir
    for filename in os.listdir(new):
        image=cv2.imread(new+'/'+filename,0)
        image=cv2.resize(image,(28,28))
        one_image=np.reshape(image,[-1,28,28,1])
        pre_y = model.predict(one_image)
        print(filename)
        print(pre_y[0])
        print(np.where(pre_y[0]==1))
        print('-----')