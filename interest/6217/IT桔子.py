# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 21:22:22 2019

@author: 朱小五

微信公众号: 凹凸玩数据

"""

import requests
import json
import pandas as pd
import time
import random
from fake_useragent import UserAgent
ua = UserAgent()
headers = {'User-Agent':ua.random} #伪装请求头

def main():
    data = pd.DataFrame(columns=['com_name','born','close','live_time','total_money','cat_name','com_prov','closure_type'])
    for i in range(1,2): #设置爬取N页
        url= 'https://www.itjuzi.com/api/closure?com_prov=&fund_status=&sort=&page='+ str(i)
        html = requests.get(url=url, headers=headers).content
        doc = json.loads(html.decode('utf-8'))['data']['info']
        for j in range(10): #一页10个死亡公司
            data = data.append({'com_name':doc[j]['com_name'],'born':doc[j]['born'],'cat_name':doc[j]['cat_name'],
                    'closure_type':doc[j]['closure_type'],'close':doc[j]['com_change_close_date'],'com_prov':doc[j]['com_prov'],
                    'live_time':doc[j]['live_time'],'total_money':doc[j]['total_money']},ignore_index=True)
            time.sleep(random.random())
    return data

if __name__ == "__main__":
    final_result = main()
    #final_result.to_csv("final_result.csv", index_label="index_label",encoding='utf-8-sig')

