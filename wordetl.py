#!/bin/bash/
#!-*-coding:utf-8-*-

import pandas as pd

path = '/Users/wangfazong/Downloads/'

dt_str = '日期'
click_str = '点击率(点击SUG次数/请求数)'
click_ratio_str = '点击设备比(点击SUG设备数/请求设备数)'
order_str = '访购率(支付用户数/点击SUG设备数)'
order_num_str = '搜索万设备订单数(支付数/点击SUG设备数)'
view_ratio_str = '展现率(展示次数/请求次数)'
tactics_str = '服务策略名'

sug_stg = 'poidirect'

# dataList = pd.read_html(path+"forms.xls")
# data = pd.DataFrame(dataList[0])
# data.to_csv(path+"forms.csv",index=False , encoding='utf8')

data = pd.read_csv(path+"forms.csv", header=1)
poidirect = data.ix[data[tactics_str] == sug_stg]
waimaicall = data.ix[data[tactics_str] =='waimaicall']

# print(data.ix[data['服务策略名'] =='poidirect'])
def _map(data1, data2):
    for index, row in data1.iterrows():   # 获取每行的index、row
        for index1, row1 in data2.iterrows():
            date = row[dt_str]
            click = row[click_str]
            click = float(click[:len(click) - 1])
            click_ratio = row[click_ratio_str]
            click_ratio = float(click_ratio[:len(click_ratio) - 1])
            order = row[order_str]
            order = float(order[:len(order) - 1])
            order_num = row[order_num_str]
            order_num = float(order_num)
            date1 = row1[dt_str]
            click1 = row1[click_str]
            click1 = float(click1[:len(click1) - 1])
            click_ratio1 = row1[click_ratio_str]
            click_ratio1 = float(click_ratio1[:len(click_ratio1) - 1])
            order1 = row1[order_str]
            order1 = float(order1[:len(order1) - 1])
            order_num1 = row1[order_num_str]
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

# sug
# poi_res = poidirect[[dt_str, click_str, click_ratio_str, order_str, order_num_str]]
# waimaicall_res = waimaicall[[dt_str, click_str, click_ratio_str, order_str, order_num_str]]
# res = _map(poi_res, waimaicall_res)
# print(res)

def _map2(data1, data2):
    for index, row in data1.iterrows():   # 获取每行的index、row
        for index2, row2 in data2.iterrows():
            date = row[dt_str]
            view_ratio = row[view_ratio_str]
            view_ratio = float(view_ratio[:len(view_ratio) - 1])

            date2 = row2[dt_str]
            view_ratio2 = row2[view_ratio_str]
            view_ratio2 = float(view_ratio2[:len(view_ratio2) - 1])
            if date == date2:
                print(date)
                c = round((view_ratio - view_ratio2) / view_ratio2 * 100, 3)
                print(c)
                row.loc['order'] = 2
    return  data1

# #展现率
poi_res = poidirect[[dt_str, view_ratio_str]]
waimaicall_res = waimaicall[[dt_str, view_ratio_str]]
poi_res['order'] = 1
res = _map2(poi_res, waimaicall_res)

print(res)

poi_res.to_csv(path+ sug_stg +".csv",index=False , encoding='utf8')
waimaicall_res.to_csv(path+ sug_stg +".csv",index=False , encoding='utf8', mode='a')

