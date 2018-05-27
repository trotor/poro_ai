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
sizex = 256
sizey = 256
classifier.add(Conv2D(64, (3, 3), input_shape = (sizex, sizey, 3), activation = 'relu')) 
classifier.add(MaxPooling2D(pool_size = (2, 2)))
classifier.add(Flatten())
#Should this be equal to x or y?
classifier.add(Dense(units = sizex, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])


from keras.preprocessing.image import ImageDataGenerator


train_datagen = ImageDataGenerator(rescale = 1./255,
shear_range = 0.1,
zoom_range = 0.1, 
horizontal_flip = False) # No flipping, always same

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('training_set',
target_size = (sizex, sizey),
batch_size = 8,
class_mode = 'binary')

test_set = test_datagen.flow_from_directory('test_set',
target_size = (sizex, sizey),
batch_size = 8,
class_mode = 'binary')

#This trains it...
classifier.fit_generator(training_set,
steps_per_epoch = 50, #how many images
epochs = 5,
validation_data = test_set,
validation_steps = 50)



classifier.save('poroai.h5')

