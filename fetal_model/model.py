"""
cd fetal_model
python model.py
"""

import warnings
warnings.filterwarnings('ignore')
import pickle
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from numpy import genfromtxt
import pandas as pd
import os
ModelDir = os.path.dirname(os.path.abspath(__file__))

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

def FetalInferences(FetalDetails):
    """
    baseline value,accelerations,fetal_movement,uterine_contractions,light_decelerations,severe_decelerations,
    prolongued_decelerations,abnormal_short_term_variability,mean_value_of_short_term_variability,
    percentage_of_time_with_abnormal_long_term_variability,mean_value_of_long_term_variability,
    histogram_width,histogram_min,histogram_max,histogram_number_of_peaks,histogram_number_of_zeroes,
    histogram_mode,histogram_mean,histogram_median,histogram_variance,histogram_tendency,fetal_health
    """
    DetailsArr = np.array(list(FetalDetails.values()))
    a= np.reshape(DetailsArr, (-1,DetailsArr.shape[0]))

    predict_rf1 = predict_rf(a)
    preds = predict_rf1[0]
    print(preds)
    return preds
    
    

if __name__=="__main__":
    """
    my_data = pd.read_csv("fetal_health.csv")

    iloc = np.array(my_data.iloc[2,:])
    a= np.reshape(iloc, (-1,my_data.iloc[2,:].shape[0]))

    predict_rf1 = predict_rf(a)
    print(predict_rf1)
    """
    columns = {'bv':0 ,'a':0, 'fm':0, 'uc':0, 'ld':0, 'sd':0,'pd':0,'astv':0,'mvstv':0,'ptwaltv':0,'mvltv':0,'hw':0,'hmin':0,'hmax':0,'hpeak':0,'hzero':0,'hmode':0,'hmean':0,'hmedian':0,'hvariance':0,'ht':0}
    print(FetalInferences(columns))


