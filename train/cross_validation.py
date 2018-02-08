from sklearn.neighbors import KNeighborsClassifier#K近邻分类器
from tool import datasets
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import cross_val_score#交叉验证中最简单的方法
from sklearn.pipeline import make_pipeline#可以将数据预处理和模型结合起来
from sklearn import preprocessing
from sklearn.model_selection import cross_validate#不同于cross_val_score，允许使用多个度量方法，返回一个字典
from sklearn.model_selection import ShuffleSplit

data = datasets.load_data()
target = datasets.load_target()

X = CountVectorizer().fit_transform(data)
tfidf = TfidfTransformer().fit_transform(X)

# knn = KNeighborsClassifier(n_neighbors=6)
# #当cv时一个数字时，默认使用K折交叉验证，scoring='f1_macro'(宏平均)可以指定性能度量方法，F1指的就是F值
# scores = cross_val_score(knn,X,target,cv=5,scoring='f1_macro')
# print(scores.mean())

# clf = make_pipeline(preprocessing.StandardScaler(),KNeighborsClassifier(n_neighbors=6))
# scores = cross_val_score(clf,X.toarray(),target,cv = 10)
# print(scores)

# scoring = ['precision_macro', 'recall_macro','f1_macro']
# knn = KNeighborsClassifier(n_neighbors=6)
# scores = cross_validate(knn,X,target,scoring=scoring,cv=5,return_train_score=False)
#
# precision = scores['test_precision_macro']
# recall = scores['test_recall_macro']
# F = scores['test_f1_macro']
#
# print('准确率：',precision)
# print('召回率：',recall)
# print('F值：',F)

#对交叉验证中的验证次数，测试集大小，以及随机划分的种子进行指定
cv = ShuffleSplit(n_splits=3,test_size=0.33,random_state=0)
knn = KNeighborsClassifier(n_neighbors=6)
scores = cross_val_score(knn,X,target,scoring='precision_macro',cv=cv)
print(scores)



