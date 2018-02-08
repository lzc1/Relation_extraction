#!/usr/bin/python
# -*- coding: utf-8 -*-
import pickle
'''
为词语建立键值对
通过字典来搜索提高搜索效率
'''
#
# with open(r'C:\Users\ypdeng\PycharmProjects\untitled\wordvector\news12g_bdgbk20g_nov90g_dim128.txt',
#           'r',encoding='utf-8') as f:
#     for line in f.readlines():
#         if '贾跃亭' in line:
#             print(line)

#为词语建立字典，通过索引来获取词向量
# a = {'a':1,'b':2}
# with open('text.txt','w',encoding='utf-8') as f:
#     f.write(str(a))
#
# with open('text.txt','r',encoding='utf-8') as f:
#     data = f.read()
#     b = eval(data)
#     print(b['a'])

# dic = {}
# with open(r'C:\Users\ypdeng\PycharmProjects\untitled\wordvector\news12g_bdgbk20g_nov90g_dim128.txt','r',
#           encoding='utf-8') as f:
#     num = 0
#
#     for line in f.readlines():
#         str = line.split(' ',1)
#         dic[str[0]] = str[1]
#         # print(str[0],' ',str[1])
#
#     #删除第一个键值对
#     del dic['6115353']
    # print(dic['专访'])
    # print(type(dic))

# with open('wordvec_dic.txt','w',encoding='utf-8') as f:
#     f.write(str(dic))
#
# with open('wordvec_dic.txt','r',encoding='utf-8') as f:
#     data = f.read()
#     dic = eval(data)
#     print(dic['专访'])
#pickle存储方式默认是二进制方式
# with open('wordvec_dic.txt','wb+') as f:
#     pickle.dump(dic,f)
#
# print('finished')
with open('wordvec_dic.txt','rb') as f:
    a = pickle.load(f)
    print(a['宣亚国际'])
    print(a['阿里巴巴'])
    f.close()