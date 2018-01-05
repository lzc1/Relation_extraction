import xlrd

'''读取标注好的实体'''
path = r'C:\Users\ypdeng\Desktop\train_data.xls'
data = xlrd.open_workbook(path,'r')
sheets = data.sheets()
sheet_1 = sheets[0]
rows = sheet_1.nrows
cols = sheet_1.ncols
entity = []
for i in range(rows):
    if i==0:
        continue
    name_1 = sheet_1.cell_value(i,2)
    print(name_1)
    name_2 = sheet_1.cell_value(i,3)
    print(name_2)
    entity.append(name_1)
    entity.append(name_2)
entity = set(entity)

with open('name_dict.txt','w',encoding='utf-8') as f:
    for j in entity:
        f.write(str(j))
        f.write('\n')