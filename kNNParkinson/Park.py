"""
cd kNNParkinson
python Park.py
"""



from sklearn.preprocessing import StandardScaler
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import pickle

from sklearn.neighbors import KNeighborsClassifier
import warnings
from sklearn import metrics
CLASS_LABELS_Park = {0 : "healthy", 1: "parkinson"}
def ScaleData(data):
  scaler = StandardScaler()
  # transform data
  scaled = scaler.fit_transform(data)
  return scaled

SIZE= 128
def rgba2rgb( rgba, background=(255,255,255) ):
    row, col, ch = rgba.shape

    if ch == 3:
        return rgba

    assert ch == 4, 'RGBA image has 4 channels.'

    rgb = np.zeros( (row, col, 3), dtype='float32' )
    r, g, b, a = rgba[:,:,0], rgba[:,:,1], rgba[:,:,2], rgba[:,:,3]

    a = np.asarray( a, dtype='float32' ) / 255.0

    R, G, B = background

    rgb[:,:,0] = r * a + (1.0 - a) * R
    rgb[:,:,1] = g * a + (1.0 - a) * G
    rgb[:,:,2] = b * a + (1.0 - a) * B

    return np.asarray( rgb, dtype='uint8' )


def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])


def dispimgs(path,disp=0):
    # reading png image file
    im = plt.imread(path)
    if im.shape[-1]==4:
        im = rgba2rgb(im)
    im = cv2.resize(im,(SIZE,SIZE))
    im = rgb2gray(im)
    return im

def RunParkinsonInferences(imgPath):
  img = dispimgs(imgPath)
  imgres = ScaleData(img.reshape(1,-1))
  pred = model.predict(imgres)
  return pred[0],CLASS_LABELS_Park[pred[0]]

kNNModelPath = "kNNModel.p"
model = pickle.load( open( kNNModelPath , "rb" ) )
print(RunParkinsonInferences("Sample_Parkinson.png"))