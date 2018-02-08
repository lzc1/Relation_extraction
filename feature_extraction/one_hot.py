from sklearn import preprocessing
from sklearn.feature_extraction.text import CountVectorizer

#1,4,7,10是第一类别的取值；2,5,8,11是第二类别的取值，以此类推
# one_hot = preprocessing.OneHotEncoder()
# one_hot.fit([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# result = one_hot.transform([[4,8,12]]).toarray()
# print(result)

corpus = [
     'This is the first document is.',
     'This is the second second document.',
     'And the third one.',
     'Is this the first document?',
 ]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus).toarray()
feature = vectorizer.get_feature_names()
print(feature)
for i in X:
    print(i)
