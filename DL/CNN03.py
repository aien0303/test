import tensorflow as tf
# import theano
# theano.config.device = 'gpu'
# theano.config.floatX = 'float32'

# 類別
num_classes=10

# 輸入維度
image_size_width=28
image_size_height=28
num_channels=1
input_shape=(image_size_width,image_size_height,num_channels)

# 載入資料 打散加入train與test
(x_train, y_train),(x_test, y_test)=tf.contrib.keras.datasets.mnist.load_data()

# 格式轉換
x_train=x_train.reshape(x_train.shape[0],image_size_width,image_size_height,num_channels)
x_test=x_test.reshape(x_test.shape[0],image_size_width,image_size_height,num_channels)

# 標準化
x_train=x_train.astype('float32')
x_test=x_test.astype('float32')
x_train/=255
x_test/=255

print('x_train shape:',x_train.shape)
print(x_train.shape[0],'train samples')
print(x_test.shape[0],'test samples')

# one_hot_encoding
y_train=tf.contrib.keras.utils.to_categorical(y_train,num_classes)
y_test=tf.contrib.keras.utils.to_categorical(y_test,num_classes)

# 建立模型
model=tf.contrib.keras.models.Sequential()

# 2D的Convolution Layer，接層ReLU的Activation函數
model.add(tf.contrib.keras.layers.Conv2D(32,kernel_size=(3,3),
                 activation='relu',
                 input_shape=input_shape))

# 二層2D的Convolution Layer
model.add(tf.contrib.keras.layers.Conv2D(64,(3,3), activation='relu'))

# 2D的Max-Pooling Layer
model.add(tf.contrib.keras.layers.MaxPooling2D(pool_size=(2,2)))

# Dropout Layer
model.add(tf.contrib.keras.layers.Dropout(0.25))

# 2D影像轉1D向量
model.add(tf.contrib.keras.layers.Flatten())

# Fully Connected Layer 接ReLU的Activation函數
model.add(tf.contrib.keras.layers.Dense(128,activation='relu'))

# Dropout Layer
model.add(tf.contrib.keras.layers.Dropout(0.5))

# Fully Connected Layer 接Softmax的Activation函數
model.add(tf.contrib.keras.layers.Dense(num_classes,activation='softmax'))

# Loss Optimizer metrics(正確率)
model.compile(loss=tf.contrib.keras.losses.categorical_crossentropy,
              optimizer=tf.contrib.keras.optimizers.Adadelta(),
              metrics=['accuracy'])

# 訓練模型
model.fit(x_train,y_train,
          batch_size=128*2,
          epochs=12,
          verbose=1, # 進度日誌
          validation_data=(x_test,y_test))

model.save('h5/number.h5')