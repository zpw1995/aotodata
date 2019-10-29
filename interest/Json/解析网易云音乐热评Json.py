# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 02:58:39 2019

@author: 朱小五

微信公众号: 凹凸玩数据

哈哈还有一个：凹凸数读
"""

import requests
import jsonpath
import pandas as pd
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}

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


def get_comments(url):
    data = []
    doc = get_json(url)
    jobs=doc['hotComments']
    for job in jobs:
        dic = {}
        #从根节点开始，匹配content节点
        dic['content']=jsonpath.jsonpath(job,'$..content')[0] #评论
        dic['time']= stampToTime(jsonpath.jsonpath(job,'$..time')[0]) #时间
        dic['userId']=jsonpath.jsonpath(job['user'],'$..userId')[0]  #用户ID
        dic['nickname']=jsonpath.jsonpath(job['user'],'$..nickname')[0]#用户名
        dic['likedCount']=jsonpath.jsonpath(job,'$..likedCount')[0] #赞数
        data.append(dic)
    return pd.DataFrame(data)

final_result = get_comments('http://music.163.com/api/v1/resource/comments/R_SO_4_483671599?limit=10&offset=0')





