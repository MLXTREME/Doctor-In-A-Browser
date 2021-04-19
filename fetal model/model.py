import warnings
warnings.filterwarnings('ignore')
import pickle
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from numpy import genfromtxt
import pandas as pd


def predict_rf(a):
    """
    shape of a = (21,1)
    """
    filename = 'rf_model.pkl'
    # try:
    loaded_model = pickle.load(open(filename, 'rb'))
    predict = loaded_model.predict(a)
    print(predict)
    print("prediction done :)")
    return predict

if __name__=="__main__":
    my_data = pd.read_csv("fetal_health.csv")

    iloc = np.array(my_data.iloc[2,:])
    a= np.reshape(iloc, (-1,my_data.iloc[2,:].shape[0]))

    predict_rf1 = predict_rf(a)
    print(predict_rf1)


