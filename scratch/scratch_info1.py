import xlwt
import xlrd
import urllib
from urllib import request
from lxml import etree

#打开网页链接的Excel
path = r'C:\Users\ypdeng\Desktop\news_link.xls'
book = xlrd.open_workbook(path,'r')
sheets = book.sheets()
sheet = sheets[0]

#创建保存文本内容的Excel
book_1 = xlwt.Workbook(encoding='utf-8')
sheet_1 = book_1.add_sheet('news content',cell_overwrite_ok=True)
sheet_1.write(0,0,"标题")
sheet_1.write(0,1,"内容")
sheet_1.write(0,2,"实体1")
sheet_1.write(0,3,"实体2")
sheet_1.write(0,4,"关系")

rows = sheet.nrows
num = 0
for i in range(100):
    if i ==0:
        continue

    try:
        link = sheet.cell_value(i,0)
        title = sheet.cell_value(i,1)
        response = urllib.request.urlopen(link)
        html = response.read()
        selector = etree.HTML(html)
        text = selector.xpath('//div/p/text()')
        num = num +1
        sheet_1.write(num,0,title)
        str = ''
        for j in range(0,3):
            str = str + text[j]
        sheet_1.write(num,1,str)
    except:
        continue
    finally:
        book_1.save(r'C:\Users\ypdeng\Desktop\data.xls')
book_1.save(r'C:\Users\ypdeng\Desktop\data.xls')