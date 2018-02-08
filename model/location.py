
#test
# str = '为中华民族之崛起而读书'
# print(str.index('为'))

# file = open('location.txt','w',encoding='utf-8')
# judge = True
# str1 = ''
# str2 = ''
# with open(r'C:\Users\ypdeng\PycharmProjects\untitled\model\训练数据.txt','r',encoding='utf-8') as f:
#     for line in f.readlines():
#         if judge:
#             judge = False
#             str1 = line
#         else:
#             judge = True
#             str2 = line.strip().split(' ')
#             # for i in str2:
#             #     if i.strip().__len__()==0:
#             #         str2.remove(i)无效
#             try:
#                 num1 = str1.index(str2[0])#实体1的位置
#                 num2 = str1.index(str2[1])#实体2的位置
#                 if num1>num2:
#                     num3 = 0
#                 else:
#                     num3 = 1
#                 file.write(str(num1))
#                 file.write(' ')
#                 file.write(str(num2))
#                 file.write(' ',)
#                 file.write(str(num3))
#                 file.write('\n')
#             except:
#                 continue
# file.close()

#删除多余的空格
# with open(r'C:\Users\ypdeng\PycharmProjects\untitled\model\训练数据.txt','r',encoding='utf-8') as f:
#     for line in f.readlines():
#         lines = line.split(' ')

# str3 = ' 我 爱 中华 人 民共  和   国 '
# str4 = str3.strip().split(' ')
# print(len(str4))
# for i in str4:
#     if len(i.strip())==0:
#         str4.remove(i)
# print('--------')
# print(len(str4))
# for i in str4:
#     print(i)

file = open('location.txt','w',encoding='utf-8')
f1 = open(r'C:\Users\ypdeng\PycharmProjects\untitled\model\data.txt','r',encoding='utf-8')
f2 = open(r'C:\Users\ypdeng\PycharmProjects\untitled\model\target1.txt','r',encoding='utf-8')
num = 0
for line1,line2 in zip(f1.readlines(),f2.readlines()):
    line3 = line2.strip().split(' ')
    for i in line3:
        print(i)
    num1 = line1.index(line3[0])
    num4 = num1+len(line3[0])-1
    num2 = line1.index(line3[1])
    num5 = num2+len(line3[1])-1
    if num1 > num2:
        num3 = 0
    else:
        num3 = 1
    print(num)
    file.write(str(num1))
    file.write(' ')
    file.write(str(num4))
    file.write(' ')
    file.write(str(num2))
    file.write(' ')
    file.write(str(num5))
    file.write(' ',)
    file.write(str(num3))
    file.write('\n')
    num = num + 1

f1.close()
f2.close()
file.close()

#test
# str1 = '12 月 6 日 海虹控股 回复 深交所 问询 函中 透露 中海恒 偿还 金融机构 借款 本息 合计 41 亿元 其所持 海虹控股 2.29 亿股 质押 用于 借款 占 持股 总数 91.98%'
# str2 = '中海恒 海虹控股 股票'
#
# str3 = str2.strip().split(' ')
# for i in str3:
#     print(i)
#
# print(str1.index(str3[0]))
# print(str1.index(str3[1]))

#test
# str1= '中国人民 万岁  '
# str2= '中国人民'
# print(str1.index(str2)+len(str2))