from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pickle


#计算词频
corpus = []
num =0
with open(r'C:\Users\ypdeng\PycharmProjects\untitled\model\训练数据.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        if num==0:
            num=1
            corpus.append(line.strip().split(' '))
        elif num==1:
            num=0
    #print(corpus)
#将文本中的词语转化为词频矩阵
vectorizer = CountVectorizer()
#计算词语在文本中出现的次数
X = vectorizer.fit_transform(corpus)
#获取词袋中所有文本关键词
word = vectorizer.get_feature_names()
print(len(word))
# print(word)
# print(X.toarray())

#计算Tf-IDf值
transform = TfidfTransformer()
print(transform)
tfidf = transform.fit_transform(X)
weight = tfidf.toarray()
for i in range(len(weight)):  # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
    print(u"-------这里输出第", i, u"类文本的词语tf-idf权重------")
    for j in range(len(word)):
        print(word[j], weight[i][j] )

