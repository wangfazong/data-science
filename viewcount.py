#!/usr/bin/env python
#coding=utf-8

import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn import preprocessing
import numpy as np
from dateutil.parser import parse
import re

path = "/Users/wangfazong/dataScience/dataset/"

#计算访问量
# less_user_view = pd.read_table(path+"user_view.txt", sep=',', header=None, error_bad_lines=False)
# extra_user_view = pd.read_table(path+"extra_user_view.txt", sep=',', header=None, error_bad_lines=False)
# user_view = pd.concat([less_user_view, extra_user_view])
# user_view.rename(columns = {0:"user_id", 1:"shop_id", 2:"time_stamp"}, inplace=True)
# print(less_user_view.shape[0] + extra_user_view.shape[0] == user_view.shape[0])
# tmp = pd.DatetimeIndex(user_view['time_stamp'])
# del user_view['time_stamp']

# user_view['date'] = tmp.date
# user_view_count = user_view.groupby(['', ''date','shop_id']).size()
# user_view_count.to_csv(path+"view.csv" , encoding='utf8')
# print("-------")

# # order count
# user_pay = pd.read_table(path+"user_pay.txt", sep=',', header=-1, error_bad_lines=False)
# user_pay.rename(columns = {0:"user_id", 1:"shop_id", 2:"time_stamp"}, inplace=True)
# tmp = pd.DatetimeIndex(user_pay['time_stamp'])
# del user_pay['time_stamp']
#
# user_pay['date'] = tmp.date
# user_view_count = user_pay.groupby(['date','shop_id']).size()
# user_view_count.to_csv(path+"pay_by_day.csv" , encoding='utf8')
# print("-------")

# 整合天气节假日数据
shop_info = pd.read_table(path+"shop_info.txt", sep=',', header=None, error_bad_lines=False)
shop_info.rename(columns = {0:'shop_id', 1:"city_name", 2:"location_id", 3:"per_pay", 4:"score", 5:"comment_cnt",
                     6:"shop_level", 7:"cate_1_name", 8:"cate_2_name", 9:"cate_3_name"},inplace=True)

def _map(data, air):
    for index, row in data.iterrows():   # 获取每行的index、row
        date = row['date']
        city = row['city_name']
        row['air'] = air.get_value(date, city) # 把结果返回给data
    return data

def weather_map(str):
    pattern = re.compile(r'(\S+)转\S*')
    pattern2 = re.compile(r'(\S+)~\S*')
    value1 = re.findall(pattern,str)
    if(len(value1) > 0):
        return value1[0]
    value2 = re.findall(pattern2, str)
    if (len(value2) > 0):
        return value2[0]
    return str

# #转换天气
# weather = pd.read_csv(path+"weather_all.csv", header=-1)
# weather.rename(columns = {0:"city_name", 1:"date", 2:"high", 3:"low", 4:"weather", 5:'wind', 6:'wind_power'}, inplace=True)
# del weather['wind']
# del weather['wind_power']
#
# weather['weather'] = weather['weather'].apply(weather_map)
# print(pd.value_counts(weather['weather']))
# weather.to_csv(path+"weather_edit.csv",index=False , encoding='utf8')

weather = pd.read_csv(path+"weather_edit.csv", index_col="date")
holiday = pd.read_csv(path+"holiday.csv")
air = pd.read_csv(path+"air.csv", index_col="Date")

# train = data.loc[data['source']=="train"]
# test = data.loc[data['source']=="test"]
#
# #Drop unnecessary columns:
# test.drop(['Item_Outlet_Sales','source'],axis=1,inplace=True)
# train.drop(['source'],axis=1,inplace=True)
#
# #Export files as modified versions:
# train.to_csv("train_modified.csv",index=False)
# test.to_csv("test_modified.csv",index=False)

# #按日期划分数据
startDate=pd.to_datetime('2016-11-30')
endDate=pd.to_datetime('2016-11-15')
weather.index = pd.to_datetime(weather.index)
weather = weather[(weather.index >= startDate)]


# print(weather.truncate(before='2016-11-02', after='2016-11-15'))
# weather.reindex(index=weather['date'])




# user_view = pd.read_csv(path+"view.csv", header=-1)
# pay_by_day = pd.read_csv(path+"pay_by_day.csv", header=-1)
#
# user_view.rename(columns = {0: "date", 1: "shop_id", 2: "view_count"}, inplace=True)
# pay_by_day.rename(columns = {0: "date", 1: "shop_id", 2: "order_count"}, inplace=True)
#
# user_view_info = pd.merge(user_view, shop_info, on="shop_id")
# data1 = pd.merge(user_view_info, holiday, on="date")
# data2 = pd.merge(data1, weather, on=["city_name", "date"])
# view_with_other = _map(data2, air)
# view_with_other.to_csv(path+"view_with_other.csv",index=False , encoding='utf8')
# print('-----end----')
#
# pay_by_day_info = pd.merge(pay_by_day, shop_info, on="shop_id")
# pay1 = pd.merge(pay_by_day_info, holiday, on="date")
# pay2 = pd.merge(pay1, weather, on=["city_name", "date"])
# pay_with_other = _map(pay2, air)
# pay_with_other.to_csv(path+"pay_with_other.csv",index=False , encoding='utf8')
# print('-----end----')
#
# # 整合click order 天气节假日数据
# order_click = pd.merge(user_view, pay_by_day, on=["date", "shop_id"])
# order_click_info = pd.merge(order_click, shop_info, on="shop_id")
# order_click_info1 = pd.merge(order_click_info, holiday, on="date")
# order_click_info2 = pd.merge(order_click_info1, weather, on=["city_name", "date"])
# view_with_other = _map(order_click_info2, air)
# view_with_other.to_csv(path+"order_click_info_with_other.csv",index=False , encoding='utf8')
# print('-----end----')





# user_view = pd.read_csv(path+"view.csv")
# # testview['air'] = air[testview['date']][testview['city_name']]
# print(air.head(10))
# print(air.get_value("2015-10-21", "北京"))
# testview = _map(testview, air)
# print(testview.head(10))


# print(shop_info.describe())
# data = pd.merge(user_view, shop_info, on="shop_id")
# print(user_view.describe())
# print("----")
# print(data.describe())
# data.to_csv(path+"view.csv" , encoding='utf8')
#
# view = pd.read_csv(path+"view.csv")
# print("====================")
# print(view.head(10))

# user_view['time'] = tmp.time
# user_view['hour'] = pd.to_datetime(user_view.time, format='%H:%M:%S')
# user_view['hour'] = pd.Index(user_view['hour']).hour

# user_view['dayofweek'] = pd.DatetimeIndex(user_view.date).dayofweek
# user_view['dateDays'] = (user_view.date - user_view.date[0]).astype("timedelta64[D]")


#
# byday=data.groupby('dayofweek')
# byday['casual'].sum().reset_index()
#
# byday['registered'].sum().reset_index()
# data['Saturday']=0
# data.Saturday[data.dayofweek == 5]=1 #0表示没用到车，1表示用了
#
# data['Sunday']=0
# data.Sunday[data.dayofweek==6]=1
#
# featureConCols = ['temp','atemp','humidity','windspeed','dateDays','hour']
# dataFeatureCon = data[featureConCols]
# print(dataFeatureCon)
# dataFeatureCon = dataFeatureCon.fillna( 'NA' ) #in case I missed any
# print("------")
#
# X_dictCon = dataFeatureCon.T.to_dict().values()
#
#
# featureCatCols = ['season','holiday','workingday','weather','Saturday', 'Sunday']
# dataFeatureCat = data[featureCatCols]
# dataFeatureCat = dataFeatureCat.fillna( 'NA' ) #in case I missed any
# X_dictCat = dataFeatureCat.T.to_dict().values()
#
# vec=DictVectorizer(sparse=False)
# X_vec_cat=vec.fit_transform(X_dictCat)
# X_v=vec.fit_transform(X_dictCon)
# print(type(X_v))
#
# scaler = preprocessing.StandardScaler().fit(X_v)
# X_vec_con_ed=scaler.transform(X_v)
# print(X_vec_con_ed)
# #对离散值进行one-hot编码
# enc=preprocessing.OneHotEncoder()
# enc.fit(X_vec_cat)
# X_vec_cat_ed=enc.transform(X_vec_cat).toarray()
#
# print(X_vec_cat_ed)
# #把离散特征和连续特征组合
# X_vec=np.concatenate((X_vec_con_ed,X_vec_cat_ed),axis=1)
#
# # print (data.head())