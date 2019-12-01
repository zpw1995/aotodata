# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:27:03 2019

@author: 朱小五

微信公众号: 凹凸玩数据
"""

import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import time
import random

def get_soup(year, month):
    url = 'http://www.tianqihoubao.com/lishi/' + 'beijing/' + 'month' + '/' + str(year) + str(month) + '.html'
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, 'lxml')
        return soup
    except:
        return "Error"


def saveTocsv(data, fileName): #将天气数据保存至csv文件
    result_weather = pd.DataFrame(data, columns=['date', 'tq', 'temp', 'wind'])
    result_weather.to_csv(fileName, index=False, encoding='gbk')
    print('获取天气成功!')

def get_data(year, month):
    soup = get_soup(year, month)
    all_weather = soup.find('div', class_="wdetail").find('table').find_all("tr")
    data = list()
    for tr in all_weather[1:]:
        td_li = tr.find_all("td")
        for td in td_li:
            s = td.get_text()
            data.append("".join(s.split()))
    res = np.array(data).reshape(-1, 4)
    return res


if __name__ == '__main__':
    years = ['2019']
    months = ['11']
    #years = ['2011','2012','2013','2014','2015','2016','2017','2018','2019']
    #months = ['01','02','03','04','05','06','07','08','09','10','11','12']

    for year in years:
        for month in months:
                data = get_data(year,month)
                saveTocsv(data, '北京'+str(year)+str(month)+'.csv')
                time.sleep(random.random()+10)  #文明爬虫
#微信公众号: 凹凸玩数据