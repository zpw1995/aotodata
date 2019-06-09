# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 21:47:11 2019

@author: aotodata

微信公众号: 凹凸数读
"""

import urllib.request
import urllib.parse
import json
import jsonpath
import pandas as pd
import time
import random  
from fake_useragent import UserAgent
ua = UserAgent()

def get_json(url):
    headers = {'User-Agent':ua.random}
    request=urllib.request.Request(url=url,headers=headers)
    json_text=urllib.request.urlopen(request).read().decode()
    return(json_text)
        
def stampToTime(stamp): #时间转换
    datatime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(float(str(stamp)[0:10])))
    datatime = datatime+'.'+str(stamp)[10:]
    return datatime
    
def get_informations(url,num,name_r):
    data = []
    doc = get_json(url)
    obj=json.loads(doc)
    jobs=obj['entities']['data']
    for job in jobs:
        dic = {}
        viewCount=jsonpath.jsonpath(job,'$..viewCount')[0] #播放量
        likeCount=jsonpath.jsonpath(job,'$..likeCount')[0] #点赞数
        title=jsonpath.jsonpath(job,'$..title')[0] #标题
        content=jsonpath.jsonpath(job,'$..content')[0] #主题
        id_r=jsonpath.jsonpath(job,'$..idStr')[0] #视频id
        videoURL=jsonpath.jsonpath(job,'$..videoURL')[0] #视频下载地址
        shareURL=jsonpath.jsonpath(job,'$..shareURL')[0] #视频在线播放地址
        duration=jsonpath.jsonpath(job,'$..duration')[0] #时长
        createTime=jsonpath.jsonpath(job,'$..createTime')[0] #发布时间
        createTime_r= stampToTime(createTime)
        user=jsonpath.jsonpath(job,'$..user')[0] #user
        if jsonpath.jsonpath(user,'$..ageSection') is False:
            ageSection = '无'
        else:
            ageSection=jsonpath.jsonpath(user,'$..ageSection')[0] #年龄

        followerCount=jsonpath.jsonpath(user,'$..followerCount')[0] #关注人数
        
        if jsonpath.jsonpath(user,'$..gender') is False:
            gender = '无'
        else:
            gender=jsonpath.jsonpath(user,'$..gender')[0] #性别
        
        isVlogger=jsonpath.jsonpath(user,'$..isVlogger')[0] #是否为大V
        if jsonpath.jsonpath(user,'$..location') is False:
            location = '无'
        else:
            location=jsonpath.jsonpath(user,'$..location')[0] #地址
        
        name=jsonpath.jsonpath(user,'$..name')[0] #昵称
        postCount=jsonpath.jsonpath(user,'$..postCount')[0] #视频数量
        username=jsonpath.jsonpath(user,'$..username')[0] #用户ID
        if jsonpath.jsonpath(user,'$..horoscope') is False:
            horoscope = '无'
        else:
            horoscope=jsonpath.jsonpath(user,'$..horoscope')[0] #星座
            
        if jsonpath.jsonpath(user,'$..profession') is False:
            profession = '无'
        else:
            profession=jsonpath.jsonpath(user,'$..profession')[0] #职业
            
        dic['频道id'] = num
        dic['频道名称'] = name_r
        dic['视频id'] = str(id_r)
        dic['videoURL'] = videoURL
        dic['shareURL'] = shareURL
        dic['时长'] = duration
        dic['发布时间'] = createTime_r
        dic['播放量'] = viewCount
        dic['点赞数'] = likeCount
        dic['标题'] = title
        dic['主题'] = content
        dic['星座'] = horoscope
        dic['职业'] = profession
        dic['年龄'] = ageSection
        dic['关注人数'] = followerCount
        dic['性别'] = gender
        dic['是否为大V'] = isVlogger
        dic['地址'] = location
        dic['昵称'] = name
        dic['视频数量'] = postCount
        dic['用户ID'] = username
        data.append(dic)
        #time.sleep(random.random())
    return data  



 #汇总
def main(num,name_r):
    final_result = pd.DataFrame()
    data = []
    n = 1
    #循环爬取n页
    for i in range(0,999):
        i = i*10
        urls = 'https://api.vuevideo.net/api/v1/topics/'+ num +'/all?&start=' + str(i) + '&length=10&sessionCount=200&p=VUE&f=Android&v=3.2.2.1&vc=117&lang=zh-hans&and_model=OPPO%20R11&and_brand=OPPO%20&country=CN&channel=002&nw=WIFI&gid=fdf8873a-7cb0-494c-a982-9e021f98ed3d&did=8c1645ea51c65674&longitude=110.56798285590278&latitude=23.998358018663193'
        dic =  get_informations(urls,num,name_r)
        data.extend(dic)
        final_result = pd.DataFrame(data)
        final_result.to_csv("vlog_" + num + name_r +".csv", index_label="index_label",encoding='utf-8-sig')
        print('已成功采集%i页\n' % n)
        n = n+1
        time.sleep(random.random())
    return final_result

  
data_r = [
('67','我的日常不无聊')] #把频道ID和名称放在此处

if __name__ == "__main__":
    for i,n in data_r:
        final_result = main(i,n)
        print(i,n,'该频道爬取完毕')
        time.sleep(3 + random.random())

        
        
        
        