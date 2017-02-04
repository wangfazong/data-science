#!/bin/python
#-*-coding: utf-8-*-

import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
import seaborn as sns

path = '/Users/wangfazong/dataScience/'
data = pd.read_csv(path+'iris.data', header=-1)
data.rename(columns={0:'SepalLengthCm',1:'SepalWidthCm',2:'PetalLengthCm',3:'PetalWidthCm',4:'Species'},inplace=True)
print(data["Species"].value_counts())

# sns.FacetGrid(data, hue='Species', size=6).map(sns.kdeplot, 'PetalLengthCm').add_legend()
# plt.show()

# sns.pairplot(data, hue='Species', size=5)
# sns.pairplot(data, hue="Species", size=3, diag_kind="kde")
# plt.show()

# data.boxplot(by='Species', figsize=(12,6))
# plt.show()

# data.plot(kind='scatter', x='SepalLengthCm', y='SepalWidthCm')
# sns.jointplot(x='SepalLengthCm', y='SepalWidthCm', s=15, data=data, size=5)
# plt.show()

# sns.FacetGrid(data, hue='Species', size=4).map(plt.scatter, 'SepalLengthCm', 'SepalWidthCm').add_legend()
# plt.show()

# sns.boxplot(x="Species", y="PetalLengthCm", data=data)
# sns.stripplot(x="Species", y="PetalLengthCm", data=data, jitter=True, edgecolor="gray")
# plt.show()

# sns.violinplot(x='Species', y='PetalLengthCm', data=data, size=6)
# plt.show()

# sns.jointplot(x='SepalLengthCm', y='SepalWidthCm', s=15,  data=data, kind="kde", space=0, color="#6AB27B")
# plt.show()

sns.jointplot(x='SepalLengthCm', y='SepalWidthCm', s= 15, data=data, color="k").plot_joint(sns.kdeplot, zorder=0, n_levels=6)
plt.show()