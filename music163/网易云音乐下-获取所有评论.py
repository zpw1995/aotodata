# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 17:11:24 2019

@author: aotodata

微信公众号: 凹凸数读

微信公众号: 凹凸玩数据
"""
import requests
import jsonpath
import pandas as pd
import time
from fake_useragent import UserAgent
ua = UserAgent()
import random


headers = {'User-Agent':ua.random}


def get_json(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            json_text=response.json()
            return json_text
    except Exception:
        print('此页有问题！')
        return None
    

def stampToTime(stamp): #时间转换
    datatime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(float(str(stamp)[0:10])))
    datatime = datatime+'.'+str(stamp)[10:]
    return datatime


def get_comments(url,k):
    data = []
    doc = get_json(url)
    jobs=doc['hotComments']
    for job in jobs:
        dic = {}
        dic['content']=jsonpath.jsonpath(job,'$..content')[0].replace('\r', '')
        dic['time']= stampToTime(jsonpath.jsonpath(job,'$..time')[0])
        dic['userId']=jsonpath.jsonpath(job['user'],'$..userId')[0]  #用户ID
        dic['nickname']=jsonpath.jsonpath(job['user'],'$..nickname')[0]#用户名
        dic['likedCount']=jsonpath.jsonpath(job,'$..likedCount')[0] 
        dic['name']= k
        data.append(dic)
    return data  


 #汇总
def main():
    final_result = pd.DataFrame()
    data_pinglun = []
    n = 1
    data2 =pd.read_csv('huayu_data.csv',header=0,encoding="utf-8") 
    for index, row in data2.iterrows():
        k = row['name']
        urls = 'http://music.163.com/api/v1/resource/comments/R_SO_4_' + str(row['id']) + '?limit=20&offset=0'
        dic =  get_comments(urls,k)
        data_pinglun.extend(dic)
        final_result = pd.DataFrame(data_pinglun)
        final_result.to_csv("热评_凹凸数读.csv", index_label="index_label",encoding='utf-8-sig')
        print('已成功采集%i首歌曲的热评\n' % n)
        time.sleep(random.random()) #礼貌爬虫
        n = n+1
    return final_result


if __name__ == "__main__":
    final_result = main()





