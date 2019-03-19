import numpy as np
from random import shuffle
from PIL import Image
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.python.framework import graph_util
# from keras.backend.tensorflow_backend import set_session
# config = tf.ConfigProto()
# config.gpu_options.per_process_gpu_memory_fraction = 0.45
# set_session(tf.Session(config=config))
import os
os.environ["CUDA_VISIBLE_DEVICES"]="0"

def one_hot_encoding(label):

    values=np.asarray(label)
    n_class=np.max(values) + 1
    encoding_result=np.eye(n_class)[values]
    return encoding_result 

# 讀路徑
def load_data(file_path):

    with open(file_path,"r") as lines:
        data_list=[]
        for line in lines:
            data_list.append(line.replace('\n',''))

        shuffle(data_list) 

    data_path=[]
    data_label=[]
    for data in data_list:
        data_path.append(data.split(' ')[0])
        data_label.append(int(data.split(' ')[1]))

    return data_path,data_label

# 讀圖片
def load_batch_data(data_path, labels):
    
    batch_data=[]
    for index,im in enumerate(data_path): 
        raw_image=Image.open(im)
        # normalized 
        resize_image=raw_image.resize((416,416))
        normalized_image=np.asarray(resize_image)/255.0
        batch_data.append(normalized_image)

    batch_label=one_hot_encoding(labels)

    batch_data=np.asarray(batch_data, np.float32)
    batch_label=np.asarray(batch_label, np.float32)
    return batch_data, batch_label

print('loading image path......')
train_data,train_label=load_data('train_data.txt')
test_data,test_label=load_data('test_data.txt')

print('number of train image is {}'.format(len(train_data)))
print('number of test image is {}'.format(len(test_data)))

image_size_width=416
image_size_height=416
num_labels=2 # B C
num_channels=3 # RGB
batch_size=224 # 一次採樣圖片數 32*
kernel_size=5 # 特徵值
num_steps=3001

# create CNN model

x=tf.placeholder(tf.float32,[None,image_size_height,image_size_width,num_channels],name='input')
y=tf.placeholder(tf.float32,[None,num_labels])

# initial variables
layer1_weights=tf.Variable(tf.truncated_normal([kernel_size, kernel_size,num_channels,32],stddev=0.1))
layer1_biases=tf.Variable(tf.zeros([32]))
layer2_weights=tf.Variable(tf.truncated_normal([kernel_size, kernel_size,32,64],stddev=0.1))
layer2_biases=tf.Variable(tf.constant(1.0,shape=[64]))
# layer3
layer3_weights=tf.Variable(tf.truncated_normal([kernel_size,kernel_size,64,128],stddev=0.1))
layer3_biases=tf.Variable(tf.constant(1.0,shape=[128]))

# 前面==reshape
layer4_weights=tf.Variable(tf.truncated_normal([43264,1024], stddev=0.1))
layer4_biases=tf.Variable(tf.constant(1.0, shape=[1024]))
layer5_weights=tf.Variable(tf.truncated_normal([1024, num_labels],stddev=0.1))
layer5_biases=tf.Variable(tf.constant(1.0,shape=[num_labels]))

# CNN model detail
def model(input_image):
    conv1=tf.nn.conv2d(input_image, layer1_weights,[1,2,2,1],padding='SAME')
    hidden1=tf.nn.relu(conv1+layer1_biases)
    pool1=tf.nn.max_pool(hidden1,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')

    conv2=tf.nn.conv2d(pool1,layer2_weights,[1,2,2,1],padding='SAME')
    hidden2=tf.nn.relu(conv2 + layer2_biases)
    pool2=tf.nn.max_pool(hidden2,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')
    # layer3
    conv3 = tf.nn.conv2d(hidden2, layer3_weights, [1, 2, 2, 1], padding='SAME')
    hidden3=tf.nn.relu(conv3 + layer3_biases)
    
    shape=pool2.get_shape().as_list()

    reshape=tf.reshape(pool2,[-1,shape[1]*shape[2]*shape[3]])
    # print(reshape)
    hidden=tf.nn.relu(tf.matmul(reshape,layer4_weights)+layer4_biases)
    return tf.nn.bias_add(tf.matmul(hidden,layer5_weights),layer5_biases)

# build model
logits=model(x)
out=tf.nn.softmax(logits,name="out")

# define cost
loss=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y,logits=logits))

# optimization
optimizer=tf.train.AdamOptimizer(1e-4).minimize(loss)
# show prediction result
prediction=tf.equal(tf.argmax(logits,1),tf.argmax(y,1))
accuracy=tf.reduce_mean(tf.cast(prediction, tf.float32))

saver=tf.train.Saver()

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print('start training......')
    for step in range(num_steps):
        offset=(step * batch_size)%(len(train_data)-batch_size)
        batch_data_path=train_data[offset:(offset+batch_size)]
        batch_label_path=train_label[offset:(offset+batch_size)]

        train_batch_data,train_batch_labels=load_batch_data(batch_data_path,batch_label_path)

        feed_dict={x:train_batch_data,y:train_batch_labels}
        _,l,train_accuracy_=sess.run([optimizer,loss,accuracy],feed_dict=feed_dict)


        if (step%100==0):
            saver.save(sess,'bus_model/model.ckpt')
            print('step={},loss={}, accuracy={}'.format(step,l,train_accuracy_))
            test_batch_data,test_batch_labels=load_batch_data(test_data[:],test_label[:])
            feed_dict={x:test_batch_data,y:test_batch_labels}
            test_accuracy_=sess.run(accuracy, feed_dict=feed_dict)
            print('test accuracy={}'.format(test_accuracy_))
    
    # constant_graph = graph_util.convert_variables_to_constants(sess=session,
    #                                                             input_graph_def=session.graph_def,
    #                                                             output_node_names=['out','input'])# 重要變數
    # with tf.gfile.FastGFile("bus.pb", mode='wb') as f:
    #     f.write(constant_graph.SerializeToString())
