# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 23:24:10 2019

@author: aotodata

微信公众号: 凹凸数读
"""


import matplotlib.pyplot as plt #绘图
import matplotlib as mpl #配置字体
import pandas as pd
import seaborn as sns
mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
mpl.rcParams['axes.unicode_minus']


f = open('大额优惠券.csv',encoding='utf-8-sig')

data = pd.read_csv(f)
data['返利比例'] = data['返利']*100/data['券后']


plt.figure(figsize=(8,5))
sns.violinplot(x= data['券值'],palette="Set2")
plt.show()

plt.figure(figsize=(8,5))
sns.violinplot(x= data['返利'],palette="Set2")
plt.show()
