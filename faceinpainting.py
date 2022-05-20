from numpy import zeros
from numpy import ones
from numpy.random import randint
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.initializers import RandomNormal
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import Conv2DTranspose
from tensorflow.keras.layers import LeakyReLU
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Concatenate
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import BatchNormalization
from matplotlib import pyplot as plt
from tensorflow.keras.utils import plot_model
from os import listdir
from numpy import asarray, load
from numpy import vstack
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from numpy import savez_compressed
from matplotlib import pyplot
import numpy as np
import cv2
from tensorflow.keras.applications import MobileNetV2


def preprocess(src_image):
    X1 = src_image[0]
    X1 = (X1 - 127.5) / 127.5
    return [X1]


# plot source, generated images
def plot_images1(src_img, gen_img):
    images = vstack((src_img, gen_img))
    # scale from [-1,1] to [0,1]
    images = (images + 1) / 2.0
    titles = ['Source', 'Generated']
    # plot images row by row
    for i in range(len(images)):
        # define subplot
        pyplot.subplot(1, 2, 1 + i)
        # turn off axis
        pyplot.axis('off')
        # plot raw pixel data
        pyplot.imshow(images[i])
        # show title
        pyplot.title(titles[i])
    pyplot.show()


#Test trained model on a few images...

from tensorflow.keras.models import load_model
from numpy.random import randint
model = load_model("model_080000.h5")


a = []
img = cv2.imread("a.jpg")
img = cv2.resize(img,(256,256),cv2.INTER_CUBIC)
a.append(img)
src_img=asarray(a)
src_img = preprocess(src_img)
src_img = asarray(src_img)
gen_img = model.predict(src_img)
# plot all three images
plot_images1(src_img, gen_img)
