# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 02:13:20 2019

@author: 朱小五

微信公众号: 凹凸玩数据

哈哈还有一个：凹凸数读
"""

import json
dict_data = {
    "animals": {
        "dog": [
            {
                "name": "Rufus",
                "age":15
            },
            {
                "name": "Marty",
                "age": 'null'
            }
        ]
    }
}
# 将dict格式数据转换成json格式字符串
dump_data = json.dumps(dict_data)
load_data = json.loads(dump_data)
data = load_data.get("animals").get("dog")
result1 = []
for i in data:
    result1.append(i.get("name"))
print(result1)


import jsonpath
load_data = json.loads(dump_data)
jobs=load_data['animals']['dog']
result2 = []
for i in data:
    result2.append(jsonpath.jsonpath(i,'$..name')[0])
print(result2)










