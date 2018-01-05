import re
'''
把句子括号里面的内容不要了
只针对中文括号
刘志成
'''
senten = '本文为必康股份(26.380, 0.03, 0.11%)实际控制人李宗松专访'

# pattern = re.compile(r'（|）')
# pattern = re.compile(r'\(|\)')
pattern = re.compile(r'（|）|\(|\)')
sentens = pattern.split(senten)

print(len(sentens))
for i in sentens:
    print(i)

result = ''
for i in range(len(sentens)):
    if i%2!=0:
        continue
    else:
        result = result+sentens[i]
print(result)