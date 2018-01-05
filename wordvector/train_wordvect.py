import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

import gensim
import sys
import  importlib
from lxml import etree
import  jieba
from gensim.models import  word2vec

importlib.reload(sys)
print(sys.getdefaultencoding())

# fp = open('text.txt','w',encoding='utf-8')
# with open(r'C:\Users\ypdeng\Desktop\news_sohusite_xml.smarty.dat','r',encoding='utf-8') as f:
#     str = ''
#     for i in f.readlines():
#         str = str+i
#         if i.find('</doc>')!=-1:
#             print('成功')
#             selector = etree.XML(str)
#             text = selector.xpath('//content/text()')
#             for j in text:
#                 fp.write(j)
#             str = ''
# fp.close()
# with open(r'C:\Users\ypdeng\Desktop\content.txt','r',encoding='utf-8') as f:
#     for line in f.readlines():
#         text = jieba.cut(line.strip())
#         for j in text:
#             fp.write(j)
#             fp.write('\n')

sentences = word2vec.Text8Corpus(u'text.txt')
#size是神经网络层数
model = word2vec.Word2Vec(sentences,size=50)
#保存模型
model.save('word2vec')
#加载模型
model_1 = gensim.models.Word2Vec.load('word2vec')
#判断两个词的相似度
y = model.similarity(u'没有',u'眼睛')
print(y)

print(model.most_similar(u'没有'))