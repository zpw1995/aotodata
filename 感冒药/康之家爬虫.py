# -*- coding: utf-8 -*-
"""
Created on Sat May 25 16:03:02 2019

@author: aotodata

微信公众号: 凹凸数读
"""
from pyquery import PyQuery as pq
import pandas as pd
import time
import random
from fake_useragent import UserAgent

cookies = {'Cookie':'$KzjProp=true; NTKF_T2D_CLIENTID=guestC21E477B-CB74-2340-36B6-15C782DC58D6; LXB_REFER=localhost; nTalk_CACHE_DATA={uid:kf_9704_ISME9754_guestC21E477B-CB74-23,tid:1555171864307738}; LiveWSLRW17853002=959198e7b249437bb5ab14da472a9454; NLRW17853002fistvisitetime=1558155536800; Hm_lvt_bcc3591c984f78c5c26329ce462fd35a=1558155537; JSESSIONID=2E896AE2DEAA651DE78A59142132BF68; LiveWSLRW17853002sessionid=0888ad2ad07a406893f4f8395129a273; NLRW17853002visitecounts=3; NLRW17853002IP=%7C223.20.142.234%7C113.47.40.160%7C; Hm_lpvt_bcc3591c984f78c5c26329ce462fd35a=1558772613; NLRW17853002lastvisitetime=1558772613203; NLRW17853002visitepages=20; NLRW17853002lastinvite=1558772616369; NLRW17853002LR_check_data=4%7C1558772616426%7C%7C%7C'}
ua = UserAgent()
headers = {'User-Agent':ua.random} #伪装headers


def get_url(url,num):  # 获取药品链接
    dic = []
    for n in range(1, num +1):
        u = url+ str(n)+ '.html'
        doc = pq(u,headers=headers,cookies=cookies)
        for i in range(1,33): #一页32种药品
            ca1 = doc.find('li:nth-child('+str(i)+') > div.t-info > a').attr('href')
            cb = ('http://www.kzj365.com' + ca1)
            dic.append(cb)
            time.sleep(random.random())
        print('已采集%s页药品链接' %n)
    print('药品链接采集完毕')
    return dic
    

def get_informations(u):  # 获取药品说明书
    dic = {}
    doc = pq(u)
    for i in range(1,22):
        ca1 = doc('body > div.clearfix.goods-detail.wid1200 > div.gd-right > div.detail-con > div.detail-grid.detail-manual > table > tr:nth-child('+str(i)+')> td:nth-child(1)').text()
        ca2 = doc('body > div.clearfix.goods-detail.wid1200 > div.gd-right > div.detail-con > div.detail-grid.detail-manual > table > tr:nth-child('+str(i)+')> td:nth-child(2)').text()
        dic['%s' %ca1] = ca2
        ca3 = doc('#goods_info_spec').attr('value')
        ca4 = doc.find('#rprice').text()
        ca5 = doc('#goodsInfoApprovalNumber').attr('value')
        dic['规格'] = ca3
        dic['现价'] = ca4
        if 'H' in ca5: #直接判断中西药
            dic['中西药'] = '西药'
        elif 'Z' in ca5:
            dic['中西药'] = '中药'
        else :
            dic['中西药'] = '缺失数据'
    return dic  


def main(): # 采集数据
    n=0
    data = []
    urls = get_url('http://www.kzj365.com/category-13-page-', 5)  #爬取n页
    for i in urls:
        n+=1
        a = get_informations(i)
        data.append(a)
        final_result = pd.DataFrame(data)
        final_result.to_csv("ganmaoyao.csv", index_label="index_label",encoding='utf-8-sig')
        print('已采集%s条数据' %n)
        time.sleep(random.random()*3)
    return final_result


if __name__ == "__main__":
    final_result = main()

