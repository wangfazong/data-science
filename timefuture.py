#!/usr/bin/env python
#coding=utf-8

import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn import preprocessing
import numpy as np

data = pd.read_csv("train.csv", header=0, error_bad_lines=False)
tmp = pd.DatetimeIndex(data['datetime'])
data['date'] = tmp.date
data['time'] = tmp.time
data['hour'] = pd.to_datetime(data.time, format='%H:%M:%S')
data['hour'] = pd.Index(data['hour']).hour

data['dayofweek'] = pd.DatetimeIndex(data.date).dayofweek
data['dateDays'] = (data.date - data.date[0]).astype("timedelta64[D]")


byday=data.groupby('dayofweek')
byday['casual'].sum().reset_index()

byday['registered'].sum().reset_index()
data['Saturday']=0
data.Saturday[data.dayofweek == 5]=1 #0表示没用到车，1表示用了

data['Sunday']=0
data.Sunday[data.dayofweek==6]=1

featureConCols = ['temp','atemp','humidity','windspeed','dateDays','hour']
dataFeatureCon = data[featureConCols]
print(dataFeatureCon)
dataFeatureCon = dataFeatureCon.fillna( 'NA' ) #in case I missed any
print("------")

X_dictCon = dataFeatureCon.T.to_dict().values()


featureCatCols = ['season','holiday','workingday','weather','Saturday', 'Sunday']
dataFeatureCat = data[featureCatCols]
dataFeatureCat = dataFeatureCat.fillna( 'NA' ) #in case I missed any
X_dictCat = dataFeatureCat.T.to_dict().values()

vec=DictVectorizer(sparse=False)
X_vec_cat=vec.fit_transform(X_dictCat)
X_v=vec.fit_transform(X_dictCon)
print(type(X_v))

scaler = preprocessing.StandardScaler().fit(X_v)
X_vec_con_ed=scaler.transform(X_v)
print(X_vec_con_ed)
#对离散值进行one-hot编码
enc=preprocessing.OneHotEncoder()
enc.fit(X_vec_cat)
X_vec_cat_ed=enc.transform(X_vec_cat).toarray()

print(X_vec_cat_ed)
#把离散特征和连续特征组合
X_vec=np.concatenate((X_vec_con_ed,X_vec_cat_ed),axis=1)

# print (data.head())
