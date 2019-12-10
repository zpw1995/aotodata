# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 22:17:58 2019

@author: 朱小五

微信公众号: 凹凸玩数据

"""

import requests
from pyquery import PyQuery as pq
import pandas as pd
import time
import random  
from fake_useragent import UserAgent
ua = UserAgent()

headers = {'User-Agent':ua.random}

def main():
    data = []
    n = 1
    for i in range(4543,4550): #自己设置id范围
        dic = {}
        url = 'https://www.lxybaike.com/index.php?doc-view-'+str(i)+'.html'
        print('已成功采集{}条数据'.format(n))
        html = requests.get(url,headers=headers).text
        doc = pq(html)
        dic['tittle'] = doc('#doctitle').text()
        dic['num'] = doc('#doc-aside > div.columns.ctxx > ul > li:nth-child(1)').text().replace('浏览次数：','').replace(' 次','')
        dic['zan'] = doc('#ding > span').text().replace('[','').replace(']','')
        dic['id'] = i
        data.append(dic)
        time.sleep(random.random())
        n = n + 1
    return data  

if __name__ == '__main__':
    data = main()
    final_result = pd.DataFrame(data)
    final_result.to_csv('凹凸玩数据.csv',encoding="utf_8",index = False)