import numpy as np
import cv2
import tensorflow as tf
tf.reset_default_graph()
from darkflow.net.build import TFNet
import os 
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' 

predict_dir = './Demo02'
test = os.listdir(predict_dir)
saver = tf.train.import_meta_graph('bus_model/model.ckpt.meta')
with tf.Session() as sess:
    saver.restore(sess,'bus_model/model.ckpt')
    for index, data_dir in enumerate(test):
        new=predict_dir+'/'+data_dir
        for filename in os.listdir(new):
            image=cv2.imread(new+'/'+filename)
            one_image=np.reshape(image, [-1, 416, 416, 3])
            input_x=tf.get_default_graph().get_tensor_by_name('input:0')
            output=tf.get_default_graph().get_tensor_by_name('out:0')
            out=sess.run(output,feed_dict={input_x:one_image})
            pre_label=np.argmax(out,1)
            print(filename)
            print(out[0])
            if pre_label.all()==[0]:
                print('大都會汽車客運(M)')
            else:
                print('首都汽車客運(C)')
            print('-----')