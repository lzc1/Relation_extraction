import re
'''
把句子括号里面的内容不要了
只针对中文括号
刘志成
'''
senten = '中华人民共和国（简称中国）位于亚洲（东亚），是世界上面积第三大的国家'

pattern = re.compile(r'（|）')
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