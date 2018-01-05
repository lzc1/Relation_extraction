import xlwt #向Excel表格写入
import xlrd#从Excel表格读出

#创建一个新的工作簿
book = xlwt.Workbook(encoding='utf-8')
#添加一个sheet,，第一个参数是名称，第二个参数允许重复写入
sheet = book.add_sheet('train data',cell_overwrite_ok=True)

#往Excel表格写入
sheet.write(0,0,'company')
#保存
book.save(r'C:\Users\ypdeng\Desktop\标注.xls')
sheet.write(1,0,'city')
book.save(r'C:\Users\ypdeng\Desktop\标注.xls')
sheet.write(2,0,'data')
book.save(r'C:\Users\ypdeng\Desktop\标注.xls')

# #文件路径
# path = r'C:\Users\ypdeng\Desktop\标注.xls'
# #打开文件
# data = xlrd.open_workbook(path,'r')
# #获得工作表
# sheets = data.sheets()
# sheet_1 = sheets[0]
#
# print(sheet_1.row_values(0))
# #获得行数和列数
# rows = sheet_1.nrows
# cols = sheet_1.ncols
# #
# print(sheet_1.cell(0,0).value)