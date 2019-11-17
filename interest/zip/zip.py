# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 11:29:56 2019

@author: 朱小五

微信公众号: 凹凸玩数据

"""

'''
#生成全部的六位数字密码
f = open('passdict.txt','w')
for id in range(1000000):
    password = str(id).zfill(6)+'\n'
    f.write(password)
f.close()
'''

import zipfile
 
def extractFile(zipFile, password):
    try:
        zipFile.extractall(pwd= bytes(password, "utf8" ))
        print("李大伟的压缩包密码是" + password)  #破解成功
    except:
        pass  #失败，就跳过
        
def main():
    zipFile = zipfile.ZipFile('李大伟.zip')   
    PwdLists = open('passdict.txt')   #读入所有密码
    for line in PwdLists.readlines():   #挨个挨个的写入密码
        Pwd = line.strip('\n')
        guess = extractFile(zipFile, Pwd)

if __name__ == '__main__':
    main()