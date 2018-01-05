import jieba
import xlrd
import xlwt
import re
import xlsxwriter
from xlutils.copy import copy
import pandas as pd


# book = xlwt.Workbook(encoding='utf-8')
# sheet = book.add_sheet('训练数据',cell_overwrite_ok=True)
# sheet.write(0,0,'句子')
# sheet.write(0,1,'实体1')
# sheet.write(0,2,'句子2')
# sheet.write(0,3,'关系')
# book.save( r'C:\Users\ypdeng\Desktop\训练数据.xls')

#将标注好的句子从read_path抽取出来，写入write_path
def sentences_extraction(read_path,write_path):
    book1 = xlrd.open_workbook(read_path,'r')
    sheets = book1.sheets()
    sheet1 = sheets[0]
    rows1 = sheet1.nrows
    cols1 = sheet1.ncols

    book_2 = xlrd.open_workbook(write_path)
    book2 = copy(book_2)
    sheet2 = book2.get_sheet(0)
    rows2 = book_2.sheets()[0].nrows
    cols2 = book_2.sheets()[0].ncols
    # writer = pd.ExcelWriter(write_path)


    regex = r'。|！|？'
    pattern = re.compile(regex)


    for i in range(1,rows1):
        str = sheet1.cell_value(i,0)
        print(type(str))
        str = str + '。'
        print(type(str))
        str = str + sheet1.cell_value(i,1)
        str = str+''
        print(type(str))
        print(str)
        entity1 = sheet1.cell_value(i,2)
        entity2 = sheet1.cell_value(i,3)
        relation = sheet1.cell_value(i,4)

        try:
            senten = find_sentence(pattern,str,entity1,entity2)
            print(type(senten))
            # print('奋斗')
            # senten = str(senten)
            senten = remove_bracket(senten)
            sheet2.write(rows2,0,senten)
            sheet2.write(rows2,1,entity1)
            sheet2.write(rows2,2,entity2)
            sheet2.write(rows2,3,relation)
            rows2 = rows2 + 1
        except:
            #忽略错误，继续执行
            continue
        finally:
            book2.save(write_path)

    book2.save(write_path)

#找到实体对所在的句子
def find_sentence(pattern,str,entity_1,entity_2):
    sentences = pattern.split(str)
    sent = []
    for i in sentences:
        i = i+ ''
        print(type(i))
        if i.find(entity_1) != -1:
            if i.find(entity_2) != -1:
                sent.append(i)
                print(i,entity_1,entity_2)
                return i+''
    #return sent

#去掉句子中的括号
def remove_bracket(senten):
    pattern = re.compile(r'（|）|\(|\)')
    sentens = pattern.split(senten)

    result = ''
    for i in range(len(sentens)):
        if i % 2 != 0:
            continue
        else:
            result = result + sentens[i]
    print(result)
    return result



if __name__ == '__main__':
    sentences_extraction( r'C:\Users\ypdeng\Desktop\数据\train_data.xls', r'C:\Users\ypdeng\Desktop\训练数据.xls')