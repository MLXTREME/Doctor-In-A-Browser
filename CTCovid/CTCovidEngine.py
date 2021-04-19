"""
cd CTCovid
python CTCovidEngine.py
"""
import os
import matplotlib.pyplot as plt
import numpy as np
from keras.preprocessing import image
from skimage import io
import warnings
from tensorflow import keras
CurrDir = os.path.dirname(os.path.abspath(__file__))

ModelPath = os.path.join(CurrDir, "Best_Model88")
Model = keras.models.load_model(ModelPath)

warnings.filterwarnings("ignore")


def preprocessImg(img):
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x /= 255
    return x


def RunInferences(imgPath, display=True):
    img = image.load_img(imgPath, grayscale=False, target_size=(64, 64))
    x = preprocessImg(img)
    custom = Model.predict(x)
    if display:
        displayImg = image.load_img(
            imgPath, grayscale=False, target_size=(256, 256))
        plt.imshow(displayImg)
        plt.xticks([])
        plt.yticks([])
        plt.show()

    a = custom[0]
    ind = np.argmax(a)
    print("Class Probabilities :", a)
    print('Prediction:', CLASS_LABELS[ind])
    return ind



CLASS_LABELS = {0: 'non-COVID', 1: 'COVID'}

if __name__=="__main__":
    imgPath = 'Sample_CT_Covid.png'
    RunInferences(imgPath, display=False)
