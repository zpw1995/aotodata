 
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 23:51:31 2019

@author: Administrator
"""
'''
抓取并保存 正文、图片、发布时间、点赞数、评论数、转发数
'''
 
 
# -*-coding:utf8-*-
# 需要的模块
import os
import urllib
import urllib.request
import time
import json
import xlwt 
import random
# 定义要爬取的微博大V的微博ID
id='5661505070'
 
# 设置代理IP
proxy_addr="122.241.72.191:808"
 
# 定义页面打开函数
def use_proxy(url,proxy_addr):
	req=urllib.request.Request(url)
	req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
	proxy=urllib.request.ProxyHandler({'http':proxy_addr})
	opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
	urllib.request.install_opener(opener)
	data=urllib.request.urlopen(req).read().decode('utf-8','ignore')
	return data
 
# 获取微博主页的containerid，爬取微博内容时需要此id
def get_containerid(url):
	data=use_proxy(url,proxy_addr)
	content=json.loads(data).get('data')
	for data in content.get('tabsInfo').get('tabs'):
		if(data.get('tab_type')=='weibo'):
			containerid=data.get('containerid')
	return containerid
 
# 获取微博大V账号的用户基本信息，如：微博昵称、微博地址、微博头像、关注人数、粉丝数、性别、等级等
def get_userInfo(id):
	url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+id
	data=use_proxy(url,proxy_addr)
	content=json.loads(data).get('data')
	profile_image_url=content.get('userInfo').get('profile_image_url')
	description=content.get('userInfo').get('description')
	profile_url=content.get('userInfo').get('profile_url')
	verified=content.get('userInfo').get('verified')
	guanzhu=content.get('userInfo').get('follow_count')
	name=content.get('userInfo').get('screen_name')
	fensi=content.get('userInfo').get('followers_count')
	gender=content.get('userInfo').get('gender')
	urank=content.get('userInfo').get('urank')
	print("微博昵称：" + name + "\n" + "微博主页地址：" + profile_url + "\n" + "微博头像地址：" + profile_image_url + "\n" + "是否认证：" + str(verified) + "\n" + "微博说明：" + description + "\n" + "关注人数：" + str(guanzhu) + "\n" +  "粉丝数：" + str(fensi) + "\n" + "性别：" + gender + "\n" + "微博等级：" + str(urank) + "\n")
	return name
 

# 获取微博内容信息,并保存到文本中，内容包括：每条微博的内容、微博详情页面地址、点赞数、评论数、转发数等
def get_weibo(id,file):
	i=1
	while True:
		url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+id
		weibo_url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+id+'&containerid='+get_containerid(url)+'&page='+str(i)
		try:
			data=use_proxy(weibo_url,proxy_addr)
			content=json.loads(data).get('data')
			cards=content.get('cards')
			if(len(cards)>0):
				for j in range(len(cards)):
					print("-----正在爬取第"+str(i)+"页，第"+str(j)+"条微博------")
					card_type=cards[j].get('card_type')
					if(card_type==9):
						mblog=cards[j].get('mblog')
						attitudes_count=mblog.get('attitudes_count')	# 点赞数
						comments_count=mblog.get('comments_count')	  # 评论数
						created_at=mblog.get('created_at')			  # 发布时间
						reposts_count=mblog.get('reposts_count')		# 转发数
						scheme=cards[j].get('scheme')				   # 微博地址
						text=mblog.get('text')						  # 微博内容
						pictures=mblog.get('pics')           # 正文配图，返回list
						pic_urls = []                          # 存储图片url地址
						if pictures:
							for picture in pictures:
								pic_url = picture.get('large').get('url')
								pic_urls.append(pic_url)
							# print(pic_urls)
 
						# 保存文本
						with open(file,'a',encoding='utf-8') as fh:
							if len(str(created_at)) < 6:
								created_at = '2019-'+ str(created_at)
							# 页数、条数、微博地址、发布时间、微博内容、点赞数、评论数、转发数、图片链接
							fh.write(str(i)+'\t'+str(j)+'\t'+str(scheme)+'\t'+str(created_at)+'\t'+text+'\t'+str(attitudes_count)+'\t'+str(comments_count)+'\t'+str(reposts_count)+'\t'+str(pic_urls)+'\n')
				i+=1
				'''休眠1s以免给服务器造成严重负担'''
				time.sleep(random.random())
			else:
				break
		except Exception as e:
			print(e)
			pass
 
 
 
def txt_xls(filename,xlsname):
	"""
	:文本转换成xls的函数
	:param filename txt文本文件名称、
	:param xlsname 表示转换后的excel文件名
	"""
	try:
		with open(filename,'r',encoding='utf-8') as f:
			xls=xlwt.Workbook()
			#生成excel的方法，声明excel
			sheet = xls.add_sheet('sheet1',cell_overwrite_ok=True)
			# 页数、条数、微博地址、发布时间、微博内容、点赞数、评论数、转发数
			sheet.write(0, 0, '爬取页数')
			sheet.write(0, 1, '爬取当前页数的条数')
			sheet.write(0, 2, '微博地址')
			sheet.write(0, 3, '发布时间')
			sheet.write(0, 4, '微博内容')
			sheet.write(0, 5, '点赞数')
			sheet.write(0, 6, '评论数')
			sheet.write(0, 7, '转发数')
			sheet.write(0, 8, '图片链接')
			x = 1
			while True:
				#按行循环，读取文本文件
				line = f.readline()
				if not line:
					break  #如果没有内容，则退出循环
				for i in range(0, len(line.split('\t'))):
					item=line.split('\t')[i]
					sheet.write(x,i,item) # x单元格行，i 单元格列
				x += 1 #excel另起一行
		xls.save(xlsname) #保存xls文件
	except:
		raise
 
 
 
if __name__=="__main__":
	name = get_userInfo(id)
	file = str(name) + id+".txt"
	get_weibo(id,file)
 
	txtname = file 
	xlsname = str(name) + id + ".xls"
	txt_xls(txtname, xlsname)
	
print('finish')
 
 
 