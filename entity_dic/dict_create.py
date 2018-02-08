import xlrd

'''读取标注好的实体'''

#path是文件路径，col1和col2是实体名所在的列
def add_dict(path,col1,col2):
    data = xlrd.open_workbook(path, 'r')
    sheets = data.sheets()
    sheet_1 = sheets[0]
    rows = sheet_1.nrows
    cols = sheet_1.ncols
    entity = []
    for i in range(rows):
        if i == 0:
            continue
        name_1 = sheet_1.cell_value(i, col1)
        print(name_1)
        name_2 = sheet_1.cell_value(i, col2)
        print(name_2)
        entity.append(name_1)
        entity.append(name_2)
    entity = set(entity)

    entity1 = []
    with open('name_dict.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            entity1.append(str(line.strip()))
    entity1 = set(entity1)

    entity2 = entity | entity1
    with open('name_dict.txt', 'w', encoding='utf-8') as f:
        for j in entity2:
            f.write(str(j))
            f.write('\n')

if __name__ == '__main__':
    path = r'C:\Users\ypdeng\Desktop\训练数据.xls'
    add_dict(path,1,2)