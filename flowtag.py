from dateutil.parser import parse
import pandas as pd

path = "/Users/wangfazong/Downloads/"
info = pd.read_table(path+"shoppingmall.txt", sep='\t', error_bad_lines=False)
info.to_csv(path+"xxxx.csv",index=False , encoding='utf8')

# print(info.head(10))

info = pd.read_csv(path+"xxxx.csv")
flow01 = info.ix[info['flowtag'] =='flow01']
flow02 = info.ix[info['flowtag'] =='flow02']
other = info.ix[info['flowtag'] =='other']

flow01.to_csv(path+"flow01.csv",index=False , encoding='utf8')
other.to_csv(path+"other.csv",index=False , encoding='utf8' ,mode='a')
# print(info)
# print(info.groupby(['flowtag','dt']))

def _map(data1, data2):
    for index, row in data1.iterrows():   # 获取每行的index、row
        for index1, row1 in data2.iterrows():
            date = row['dt']
            flowtag = row['flowtag']
            date1 = row1['dt']
            flowtag1 = row1['flowtag']
            if date == date1 and flowtag == 'other' and flowtag1=='flow01':
                schuuid = row['schuuid']
                schuuid1 = row1['schuuid']
                payuser = row['payuser']
                payuser1 = row1['payuser']
                ratio = row['ratio']
                ratio1 = row1['ratio']
                print(date)
                print(schuuid - schuuid1)
                print(payuser - payuser1)
                print(round((ratio - ratio1)/ratio1 * 100 ,3))

# info['ratio'] = str(round(float(info['ratio']),3)) + '%'
# info['ratio'] = info['ratio'].apply(round(),3)
# print(info)
_map(info, info)
# print(info)