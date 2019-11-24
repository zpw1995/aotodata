# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 14:27:43 2019

@author: 朱小五

微信公众号: 凹凸玩数据

"""
import json
import requests
import time
import pandas as pd


## 设置headers和cookie，数据爬取
header = '设置自己的header'
cookie = '设置自己的cookie'

def stampToTime(stamp): #时间转换
    datatime = time.strftime("%Y-%m-%d",time.localtime(float(str(stamp)[0:10])))
    return datatime

resou = pd.DataFrame(columns=['datetime','title','searchCount'])

for i in range(1,20):
    url= 'https://www.enlightent.cn/research/top/getWeiboRankSearch.do?keyword=王思聪&from='+ str(i) +'&t=395201742&type=realTimeHotSearchList'
    html = requests.get(url=url, cookies=cookie, headers=header).content
    data = json.loads(html.decode('utf-8'))
    for j in range(20): #一页20个
        resou = resou.append({'datetime':stampToTime(data['rows'][j]['updateTime']),
                'title':data['rows'][j]['keywords'],'searchCount':data['rows'][j]['searchNums'],
                              },ignore_index=True)

resou.to_csv("resou.csv", index_label="index_label",encoding='utf-8-sig')



resou_dt = resou.groupby('datetime',as_index=False).agg({'searchCount':['mean']})
resou_dt.columns = ['date','avg_count']

## 绘制日历图
from pyecharts import options as opts
from pyecharts import Calendar
data = [
        [resou_dt['date'][i], resou_dt['avg_count'][i]]
        for i in range(resou_dt.shape[0])
    ]

calendar = (
        Calendar(init_opts=opts.InitOpts(width='1800px',height='1500px'))
        .add("", data,calendar_opts=opts.CalendarOpts(range_=['2019-01-01', '2019-07-12']))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2019每日热搜平均指数",pos_left='15%'),
            visualmap_opts=opts.VisualMapOpts(
                max_=3600000,
                min_=0,
                orient="horizontal",
                is_piecewise=False,
                pos_top="230px",
                pos_left="100px",
                pos_right="10px"
            )
            )
        .render('日期热力图.html')     
     )

