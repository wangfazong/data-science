#!/usr/bin/env python
#coding=utf-8

from sklearn.svm import LinearSVC
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectFromModel

iris = load_iris()

x,y = iris.data, iris.target

print(x.shape)


lsvc = LinearSVC(C=0.01).fit(x,y)
model=SelectFromModel(lsvc,prefit=True)

x_new=model.transform(x)

print(x_new.shape)