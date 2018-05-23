# Poro AI - Tero Ronkko 2018
# pip install keras
# conda install keras

#Modified from https://becominghuman.ai/building-an-image-classifier-using-deep-learning-in-python-totally-from-a-beginners-perspective-be8dbaf22dd8

from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import load_model



classifier = Sequential()
# TODO: We need bigger images than 64 x 64 now 128
classifier.add(Conv2D(32, (3, 3), input_shape = (128, 128, 3), activation = 'relu')) 
classifier.add(MaxPooling2D(pool_size = (2, 2)))
classifier.add(Flatten())
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])


from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
#shear_range = 0.2,
#zoom_range = 0.2, 
horizontal_flip = False) # No flipping, always same

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('training_set',
target_size = (128, 128),
batch_size = 32,
class_mode = 'binary')

test_set = test_datagen.flow_from_directory('test_set',
target_size = (128, 128),
batch_size = 32,
class_mode = 'binary')

#This trains it...
classifier.fit_generator(training_set,
steps_per_epoch = 500, #how many images
epochs = 10,
validation_data = test_set,
validation_steps = 500)



model.save('poroai.h5')

