#!/bin/bash/
#!-*-coding:utf-8-*-

import pandas as pd

path = '/Users/wangfazong/Downloads/'

dataList = pd.read_html(path+"forms.xls")
data = pd.DataFrame(dataList[0])
data.to_csv(path+"forms.csv",index=False , encoding='utf8')

# print(data.ix[data['服务策略名'] =='poidirect'])
def _map(data1, data2):
    for index, row in data1.iterrows():   # 获取每行的index、row
        for index1, row1 in data2.iterrows():
            date = row['日期']
            click = row['点击率(点击SUG次数/请求数)']
            click = float(click[:len(click) - 1])
            click_ratio = row['点击设备比(点击SUG设备数/请求设备数)']
            click_ratio = float(click_ratio[:len(click_ratio) - 1])
            order = row['访购率(支付用户数/点击SUG设备数)']
            order = float(order[:len(order) - 1])
            order_num = row['搜索万设备订单数(支付数/点击SUG设备数)']
            order_num = float(order_num)
            date1 = row1['日期']
            click1 = row1['点击率(点击SUG次数/请求数)']
            click1 = float(click1[:len(click1) - 1])
            click_ratio1 = row1['点击设备比(点击SUG设备数/请求设备数)']
            click_ratio1 = float(click_ratio1[:len(click_ratio1) - 1])
            order1 = row1['访购率(支付用户数/点击SUG设备数)']
            order1 = float(order1[:len(order1) - 1])
            order_num1 = row1['搜索万设备订单数(支付数/点击SUG设备数)']
            order_num1 = float(order_num1)
            if date == date1:
                print(date)
                c = str(round((click - click1) / click1 * 100, 3)) + "%"
                print(c)
                c_r = str(round((click_ratio - click_ratio1) /click_ratio1 * 100, 3)) + "%"
                print(c_r)
                o = str(round((order- order1) /order1 *100, 3)) + '%'
                print(o)
                o_n = str(round((order_num- order_num1)/ order_num1 *100, 3)) +'%'
                print(o_n)
                row['order'] = o
    return  data1


data = pd.read_csv(path+"forms.csv", header=1)
poidirect = data.ix[data['服务策略名'] =='shoppingmall']
waimaicall = data.ix[data['服务策略名'] =='waimaicall']
# print(poidirect)
# print(poidirect['点击率(点击SUG次数/请求数)'])
poi_res = poidirect[['日期','点击率(点击SUG次数/请求数)','点击设备比(点击SUG设备数/请求设备数)','访购率(支付用户数/点击SUG设备数)','搜索万设备订单数(支付数/点击SUG设备数)']]
waimaicall_res = waimaicall[['日期','点击率(点击SUG次数/请求数)','点击设备比(点击SUG设备数/请求设备数)','访购率(支付用户数/点击SUG设备数)','搜索万设备订单数(支付数/点击SUG设备数)']]
res = _map(poi_res, waimaicall_res)
print(res)

# print (poi_res)

poi_res.to_csv(path+"shoppingmall.csv",index=False , encoding='utf8')
waimaicall_res.to_csv(path+"shoppingmall.csv",index=False , encoding='utf8', mode='a')