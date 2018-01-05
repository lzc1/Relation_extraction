# # -*- coding: utf-8 -*-
#
# import urllib2
# from lxml import etree
# import re
#
# request = urllib2.Request('http://finance.sina.com.cn/topnews/#1')
# url = 'http://finance.sina.com.cn/topnews/#1'
# posfix_num = 2 #用于跳转到下一页面
# response = urllib2.urlopen(request)
# html = response.read()
# print(html)
#
# # selector = etree.HTML(html)
# # href = selector.xpath('//tr/td/text()')
# # for i in href:
# #     print i
#
# # regex = "<a href=\"(http.*?)[\u4e00-\u9fa5]*?\""
# # pattern = re.compile(regex)
# # content = re.findall(pattern,html)
# # print 'dd'
# # for i in content:
# #     print i