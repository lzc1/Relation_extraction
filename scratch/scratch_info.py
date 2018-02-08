# -*- coding: utf-8 -*-
import urllib
from urllib import request
from lxml import etree
import xlwt
import xlrd

def scratch_url(index1 = 0):
     #创建Excel保存页面的url
    #创建一个新的工作簿
    book = xlwt.Workbook(encoding='utf-8')
    #添加一个sheet,，第一个参数是名称，第二个参数允许重复写入
    sheet = book.add_sheet('news_url',cell_overwrite_ok=True)
    sheet.write(0,0,"文章链接")
    sheet.write(0,1,"文章标题")

    '''爬取页面新闻的url'''
    #不同页面的共同前缀
    prefix = 'http://roll.finance.sina.com.cn/finance/zq1/ssgs/index'
    #页面的下标
    index = ''
    #页面的完整url
    URL = ''
    num = 0
    for i in range(1,41):
        print(i)
        if i ==1:
            index = 'index_1.shtml'
        else:
            index = 'index_'+str(i)+ '.shtml'
        URL = prefix+index
        #构建到某一个页面的请求
        response = urllib.request.urlopen(URL)
        #读取返回的内容
        html = response.read()
        #使用xpath解析网页
        selector = etree.HTML(html)
        #获取到ul标签下各个新闻的链接
        href = selector.xpath('//ul[@class="list_009"]/li/a/@href')
        #获取url的文章标题
        news_title = selector.xpath('//ul[@class="list_009"]/li/a/text()')
        for j in range(len(href)):
            num = num + 1
            sheet.write(num,0,href[j])
            sheet.write(num,1,news_title[j])
    #保存
    save_path = r'C:\Users\ypdeng\Desktop\news_link'+str(index1)+'.xls'
    book.save(save_path)
    return save_path



def scratch_article(path=r'C:\Users\ypdeng\Desktop\数据\news_link.xls',index = 0):
     #创建Excel保存页面内容
    book_1 = xlwt.Workbook(encoding='utf-8')
    sheet_1 = book_1.add_sheet('news_content1',cell_overwrite_ok=True)
    sheet_1.write(0,0,"标题")
    sheet_1.write(0,1,"内容")
    sheet_1.write(0,2,"实体1")
    sheet_1.write(0,3,"实体2")
    sheet_1.write(0,4,"关系")

    '''读取新闻内容'''
    #打开文件
    data = xlrd.open_workbook(path,'r')
    #获得工作表
    sheets = data.sheets()
    sheet1 = sheets[0]
    #获得行数和列数
    rows = sheet1.nrows
    cols = sheet1.ncols

    save_path = r'C:\Users\ypdeng\Desktop\train_data'+str(index)+'.xls'
    num_1 = 0
    for i in range(0,rows):
        if i ==0:
            continue
        print(i)
        #页面链接
        link = sheet1.cell_value(i,0)
        # print(link)
        title = sheet1.cell_value(i,1)
        # print(title)
        try:
            response_1 = urllib.request.urlopen(link)
            html_1 = response_1.read()
            selector_1 = etree.HTML(html_1)
            #获取文章内容
            content = selector_1.xpath('//meta[@name="description"]/@content')
            num_1 = num_1+1
            sheet_1.write(num_1,0,title)
            sheet_1.write(num_1, 1, content)
        except:
            #忽略错误，继续执行
            continue
        finally:
            book_1.save(save_path)
    book_1.save(save_path)

if __name__ == '__main__':
    #link_path = scratch_url(1)
    # link_path = r'C:\Users\ypdeng\Desktop\news_link1.xls'
    # scratch_article(link_path,2)

    #index1 = 2,index = 3
    link_path = scratch_url(2)
    scratch_article(link_path,3)
    print('爬虫结束')

