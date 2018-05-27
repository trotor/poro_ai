import numpy as np
from keras.preprocessing import image

from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import load_model
import os

classifier = load_model("poroai.h5")

def predict(filename):
    imgx = 256;
    imgy = 256;
    test_image = image.load_img(filename, target_size = (imgx, imgy))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = classifier.predict(test_image)
    #training_set.class_indices
    if result[0][0] == 1:
        prediction = 'bad'
    else:
        prediction = 'good'
    print  (filename + ": " + prediction + str(result) + " " + str(result[0][0]) )

	
	
dir = r"images\\"
for file in os.listdir(dir):
    if file.endswith(".jpg"):
        filu = os.path.join(dir, file)
        predict(filu)