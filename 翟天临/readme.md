## 分析30万条微博评论，看毕业生与翟天临的爱恨情仇

主要的文件为：
- 微博评论_简.py : 利用python爬取微博评论

#### 运行环境：
- python3.6

#### 需要安装的包：
- headers_raw_to_dict
- BeautifulSoup
- requests
- time
- random
- re

**注：公众号对应文章为《[分析30万条微博评论，看毕业生与翟天临的爱恨情仇](https://mp.weixin.qq.com/s/aA3SkLPLCDkJwwVvT1_rNA)》**

#### 爬虫思路：
- 因为爬取微博主页weibo.com或者m.weibo.cn较为困难，所以我爬取了weibo.cn，这是一个塞班年代的网页，没有混淆等一系列新技术，用户动态等从html里面就可以获取，爬取相对来说比较简单。希望对大家能够有所参考。
- 这个简易的爬取思路参考了这篇文章：《[简书文章](https://www.jianshu.com/p/e7f3bcc19fc1)》，在此非常感谢作者