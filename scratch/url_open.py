
# -*- coding: utf-8 -*-

import urllib
from urllib import request
import re
from lxml import etree
from urllib import error

# resp = urllib2.urlopen('http://www.baidu.com')
# print resp.read()

# request ='http://finance.sina.com.cn/roll/2017-12-12/doc-ifypnyqi3844807.shtml'#构建一个request请求
# response = urllib.request.urlopen('http://finance.sina.com.cn/stock/s/2017-12-18/doc-ifyptkyk5056447.shtml')
# html_data = response.read()
# print response.read()

#r表示原生字符串
# pattern = re.compile(r'hello')
#
# match = re.search(pattern,'1hello world')#会扫描整个string查找匹配
# if re.match(pattern,'1hello122'):#match只有在0位置匹配成功的话才有返回
#     print  '匹配成功'
# else:
#     print  '匹配失败'
#
# if match:
#     print match.group()

#正则表达式解析
# pattern = re.compile(r'\W+')
# text = re.findall(pattern,response.read())
# for i in text:
#     print i

# #Xpath解析网页
# selector = etree.HTML(html_data)
# text = selector.xpath('//meta[@name="description"]/@content')#用来获取标题
# # text_2 = selector.xpath('//p/text()')
# for i in text:
#     print(i)

# for i in text_2:
#     print i
# text_1 = selector.xpath('/html/head//title/text()')#/是用来获取子元素的，如果不是子元素就用//
# for i in text_1:
#     print i

#直接解析HTML文件
# html = etree.parse('C:/Users/ypdeng/Desktop/hello.html')
# result = etree.tostring(html,pretty_print=True)
# print result

# request = urllib2.Request('http://finance.sina.com.cn/topnews/#3')#构建一个request请求
# response = urllib2.urlopen(request)
# html_data = response.read()
#
# selector = etree.HTML(html_data)
# text = selector.xpath('//a/@href')
# for i in text:
#     print i


for i in range(0,5):
    try:
        print(i)
        response = urllib.request.urlopen('http:i')
    except:
        continue