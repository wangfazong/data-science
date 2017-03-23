#!/bin/bash
#-*-coding:utf-8-*-

import pandas as pd
import numpy as np

df = pd.DataFrame()
index = ['alpha', 'beta', 'gamma', 'delta', 'eta']
for i in range(5):
    a = pd.DataFrame([np.linspace(i, 5*i, 5)], index=[index[i]])
    df = pd.concat([df, a], axis=0)

print(df)

print(df[1])

df.columns = ['a', 'b', 'c', 'd', 'e']
df.columns = ['A', 'B', 'C', 'd', 'e']
print(df)