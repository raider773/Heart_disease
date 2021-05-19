import pandas as pd
import numpy as np
import pickle

#functions for pre-processing data to predict with model

def clusters (data):
    'add clusters as features with trained k-means model'
    with open('model_scaler.pkl', 'rb') as f_model_scalar:
        scaler = pickle.load(f_model_scalar) 
    with open('model_kmeans.pkl', 'rb') as f_model_kmeans:
        kmeans = pickle.load(f_model_kmeans) 
    
    data_std = scaler.transform(data)
    data["cluster"] = kmeans.predict(data_std)    
    return data



def intervals (data):
    'adds thalach intervals as a new feature'
    interval_range = pd.interval_range(start=70.0, freq=20, end=210)
    data['thalach_Intervals'] = pd.cut(data.thalach, bins = interval_range ,duplicates='raise')
    return data


def log (data):
    'apllys log transformation +1 to trestbps and chol'
    data['log+1_trestbps'] = (data['trestbps'] + 1 ).transform(np.log)
    data['log+1_chol'] = (data['chol'] + 1 ).transform(np.log)    
    return data

def onehot(data):
    'uses onehotencoder already trained in train sample for category values'
    with open('model_ohe.pkl', 'rb') as f_model_ohe:
        onehotencoder = pickle.load(f_model_ohe) 
        dummy_oneHot = onehotencoder.transform(data[['thalach_Intervals']])
        dummy_oneHot = pd.DataFrame(dummy_oneHot.toarray())
        dummy_oneHot.rename(columns = {0:'thalach_Intervals_(90.0, 110.0]',1:'halach_Intervals_(110.0, 130.0]',2:'thalach_Intervals_(130.0, 150.0]',3:'thalach_Intervals_(150.0, 170.0]',4:'thalach_Intervals_(170.0, 190.0]',5:'thalach_Intervals_(190.0, 210.0]'},inplace = True)
        
        data = pd.merge(data, dummy_oneHot , on= data.index)
        data.drop(inplace = True,columns =['thalach_Intervals'])
        
        return data
    
    
def feature_engineering (data):
    'uses all functions at once. This is the function you need to import'
    data.columns = ['age',
                     'sex',
                     'cp',
                     'trestbps',
                     'chol',
                     'fbs',
                     'restecg',
                     'thalach',
                     'exang',
                     'oldpeak',
                     'slope',
                     'ca',
                     'thal']   
    data = clusters (data)
    data = intervals (data)
    data = log (data)
    data = onehot (data)   
    data = data.drop(columns = ['key_0'])  
    
    
    return data