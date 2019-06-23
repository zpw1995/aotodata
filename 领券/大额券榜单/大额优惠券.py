# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 23:24:10 2019

@author: aotodata

微信公众号: 凹凸数读
"""

import pandas as pd
from pyquery import PyQuery as pq

def get_html():
    f = open("大额优惠券.html",'r',encoding="utf-8")
    data = f.read()     #读取html文件
    f.close()   #将文件关闭
    doc = pq(data)
    return doc


doc = get_html()
data = []
for i in range(1,201):
    a = doc.find('#dataList > li:nth-child('+str(i)+') > a > div.item-right > span').text()
    b = doc.find('#dataList > li:nth-child('+str(i)+') > a > div.item-right > div:nth-child(2) > span.line-group.coupon-tag-wrap > span.coupon-tag-right > span').text()
    c = doc.find('#dataList > li:nth-child('+str(i)+') > a > div.item-right > div:nth-child(2) > span.line-group.sell-out > span').text()
    d = doc.find('#dataList > li:nth-child('+str(i)+') > a > div.item-right > div:nth-child(3) > span > span.cl-dark').text()
    e = doc.find('#dataList > li:nth-child('+str(i)+') > a > div.item-right > div:nth-child(3) > span > span:nth-child(5)').text()
    f = doc.find('#dataList > li:nth-child('+str(i)+') > a > div.item-right > div.item-line.item-handle > div > span:nth-child(3)').text()
    dic = {}
    dic['名称'] = a
    dic['券值'] = b
    dic['已售'] = c
    dic['券后'] = d
    dic['原价'] = e
    dic['返利'] = f
    data.append(dic)
    print('已解析第%s条数据'%i)
df = pd.DataFrame(data)
df.to_csv('大额优惠券.csv', index_label="index_label",encoding='utf-8-sig')
             
             



             

             
             