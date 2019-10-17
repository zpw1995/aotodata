# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:23:14 2019

@author: 朱小五

微信公众号: 凹凸玩数据

哈哈还有一个：凹凸数读
"""




from bs4 import BeautifulSoup
import pandas as pd
import requests

url = 'http://comment.bilibili.com/123519261.xml'
html = requests.get(url)
html.encoding='utf8'

soup = BeautifulSoup(html.text, 'lxml')
results = soup.find_all('d')

comments = [comment.text for comment in results]
comments_dict = {'comments': comments}

df = pd.DataFrame(comments_dict)
df.to_csv('bili_ai5.csv', encoding='utf-8-sig')