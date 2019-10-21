# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:51:35 2019

@author: 朱小五

微信公众号: 凹凸玩数据

哈哈还有一个：凹凸数读
"""


import time

#生成出生当年所有日期
def dateRange(year):
    fmt = '%Y-%m-%d'
    bgn = int(time.mktime(time.strptime(year+'-01-01',fmt)))
    end = int(time.mktime(time.strptime(year+'-12-31',fmt)))
    list_date = [time.strftime(fmt,time.localtime(i)) for i in range(bgn,end+1,3600*24)]
    return [i.replace('-','') for i in list_date]

data_time  = dateRange('1993')


from id_validator import validator

#遍历所有日期，print通过校验的身份证号码

def vali_dator(id1,id2,id3):
    for i in dateRange(id2):
        theid = id1 + i + id3
        if validator.is_valid(theid):
            print(theid)

vali_dator('330221','1993','4914')


#print(validator.get_info('330221199306084914'))




