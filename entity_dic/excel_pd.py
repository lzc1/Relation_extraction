import pandas as pd

writer = pd.ExcelWriter(r'C:\Users\ypdeng\Desktop\训练数据.xls')

df0 = pd.read_excel( r'C:\Users\ypdeng\Desktop\data.xls',0)
a = ['日本和中国是邻国','日本','中国']

