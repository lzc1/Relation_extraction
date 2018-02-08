from sklearn.feature_extraction.text import CountVectorizer
from  sklearn.feature_extraction.text import TfidfTransformer
# 语料
corpus = [
    'This is the first document.',
    'This is the second second document.',
    'And the third one.',
    'Is this the first document?',
]
# 将文本中的词语转换为词频矩阵
vectorizer = CountVectorizer()
# 计算个词语出现的次数
X = vectorizer.fit_transform(corpus)
#获取tfidf值
tfidf= TfidfTransformer().fit_transform(X)
# 获取词袋中所有文本关键词
word = vectorizer.get_feature_names()
print(word)
# 查看词频结果
print(X.toarray())
print(tfidf.toarray())

