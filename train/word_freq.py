from sklearn.feature_extraction.text import CountVectorizer
from tool import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier#K近邻分类器
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import accuracy_score#准确率
from sklearn.metrics import recall_score#召回率
from tool import matrix
import numpy as np
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectKBest
from sklearn import svm
from sklearn import preprocessing#对数据进行预处理
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier#集成学习中的随机森林分类器
from scipy.sparse import csr_matrix



data = datasets.load_data()
# print(data)
y = datasets.load_target()
# print(y)

#转为词频矩阵

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data)
# print(X.toarray())

#random_state是一个随机种子
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33,random_state=42)
#
# knn = KNeighborsClassifier(n_neighbors=6)
# knn.fit(X_train,y_train)
# y_pred = knn.predict(X_test)
# print(metrics.accuracy_score(y_test,y_pred))#0.587719298246

#使用tfidf
# transform = TfidfTransformer()
# tfidf = transform.fit_transform(X)
#
#
# X_train, X_test, y_train, y_test = train_test_split(tfidf, y, test_size=0.33,random_state=42)
#
# knn = KNeighborsClassifier(n_neighbors=6)
# knn.fit(X_train,y_train)
# y_pred = knn.predict(X_test)
# print(metrics.accuracy_score(y_test,y_pred))#0.644736842105

#归一化，将每个样本缩放到单位范数之间，该方法适用于文本分类和聚类中
#对SVM无效，反而降低准确率
def normalization(X):
    X_normalized = preprocessing.normalize(X,norm='l2')
    return X_normalized

#标准化处理，公式：(X-mean)/std  计算时对每个属性/每列分别进行
'''
对使用TF-IDf值的svm分类器有效
'''
def preprocess_scale(X):
    #处理稀疏矩阵不能带with_mean
    X_scale = preprocessing.scale(X,with_mean=False)
    # #处理后数据的均值
    # print(X_scale.mean(axis=0))
    # #处理后数据的方差
    # print(X_scale.std(axis=0))
    return X_scale

'''
将属性缩放到一个指定的最大和最小值（通常是1-0）之间，这可以通过preprocessing.MinMaxScaler类实现。
使用这种方法的目的包括：
1、对于方差非常小的属性可以增强其稳定性。
2、维持稀疏矩阵中为0的条目。
'''
def preprocess_scaleToArange(X_train,X_test):
    min_max_scaler = preprocessing.MaxAbsScaler()#MaxAbsScaler()试用于稀疏向量
    X_scale_train = min_max_scaler.fit_transform(X_train)
    #同样的缩放方式可用于测试集
    X_scale_test = min_max_scaler.transform(X_test)
    return X_scale_train,X_scale_test

def data_split(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
    return  X_train, X_test, y_train, y_test

#k近邻
def knn_train(X_train, X_test, y_train, y_test):
    knn = KNeighborsClassifier(n_neighbors=6)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    return  accuracy_score(y_test, y_pred)#,recall_score(y_test, y_pred)

#svm
def svm_train(X_train, X_test, y_train, y_test):
    #decision_function_shape ： ‘ovo’ 一对一, ‘ovr’ 一对多  or None 无, default=None
    clf = svm.SVC(decision_function_shape='ovr')
    clf.fit(X_train,y_train)
    y_pred = clf.predict(X_test)
    return  accuracy_score(y_test, y_pred)

def matrix_combine(X,location):
    return np.column_stack((X,location))

#高斯朴素贝叶斯算法，传入的特征必须是稠密矩阵0.460526315789
def gaussian_NB_train(X_train, X_test, y_train, y_test):
    gnb = GaussianNB()
    gnb.fit(X_train,y_train)
    y_pred = gnb.predict(X_test)
    return accuracy_score(y_test,y_pred)

#分类效果0.780701754386，适用于tfidf值
def bernoulli_NB_train(X_train, X_test, y_train, y_test):
    bnb = BernoulliNB()
    bnb.fit(X_train,y_train)
    y_pred = bnb.predict(X_test)
    return accuracy_score(y_test, y_pred)

#分类效果0.802631578947 特征向量维度150,适用于词频矩阵
def multinomial_NB_train(X_train, X_test, y_train, y_test):
    mnb = MultinomialNB()
    mnb.fit(X_train, y_train)
    y_pred = mnb.predict(X_test)
    return accuracy_score(y_test, y_pred)

#随机森林分类,效果不错 特征为100时：词频矩阵，随机森林分类器： 0.767543859649，tf—idf值，随机森林分类器： 0.745614035088
#500时：词频矩阵，随机森林分类器： 0.811403508772，tf—idf值，随机森林分类器： 0.719298245614
def rfc_train(X_train, X_test, y_train, y_test):
    clf = RandomForestClassifier(n_estimators=200)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    return accuracy_score(y_test, y_pred)

if __name__ == '__main__':
    data = datasets.load_data()
    y = datasets.load_target()
    location = datasets.load_location()

    # 转为词频矩阵
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(data)
    #进行特征选择
    X_new = SelectKBest(chi2,k=500).fit_transform(X,y)#准确率 0.728070175439
    print(type(X_new))
    # X_scale = preprocess_scale(X)
    # X_scale = normalization(X)
    # X_new = SelectKBest(chi2, k=100).fit_transform(X_scale, y)
    # print(type(X_new))

    #稀疏矩阵直接转化为数组，就可以进行矩阵的合并了
    # X_new = X_new.toarray()
    # print(type(X_new))
    # print(type(location))
    # b = matrix_combine(X_new,location)
    # X_new = csr_matrix(b)
    # print(type(X_new))
    # for i in X_new:
    #     print(i)
    # print(type(b))
    # for i in b:
    #     print(i)

    # X_train, X_test, y_train, y_test = data_split(X_new,y)
    # X_train_scale,X_test_scale = preprocess_scaleToArange(X_train,X_test)
    # accuray = knn_train( X_train, X_test, y_train, y_test)
    # print('词频矩阵')
    # print('k近邻准确率：',accuray)
    # accuray1 = svm_train(X_train, X_test, y_train, y_test)
    # print('svm准确率：',accuray1)
    # print('召回率',recall)

    # accuracy4 = gaussian_NB_train(X_train, X_test, y_train, y_test)
    # print('词频矩阵，高斯朴素贝叶斯分类器：',accuracy4)
    #
    # accuracy5 = bernoulli_NB_train(X_train, X_test, y_train, y_test)
    # print('词频矩阵，伯努利贝叶斯分类器：',accuracy5)
    #
    # accuracy6 = multinomial_NB_train(X_train, X_test, y_train, y_test)
    # print('词频矩阵，多项式叶斯分类器：',accuracy6)

    # accuracy7 = rfc_train(X_train, X_test, y_train, y_test)
    # print('词频矩阵，随机森林分类器：',accuracy7)
    #
    # # 使用tfidf
    # transform = TfidfTransformer()
    # tfidf = transform.fit_transform(X)

    # # tfidf_scale = preprocess_scale(tfidf)
    # tfidf_scale = normalization(tfidf)
    # tfidf_new = SelectKBest(chi2,k=100).fit_transform(tfidf,y)#准确率 0.706140350877
    # tfidf_new = tfidf_new.toarray()
    # tfidf_new = matrix_combine(tfidf_new,location)
    # tfidf_new = tfidf_new.toarray()
    # X_train, X_test, y_train, y_test = data_split(tfidf_new, y)
    # # X_train_scale, X_test_scale = preprocess_scaleToArange(X_train, X_test)
    # accuray2 = knn_train(X_train, X_test, y_train, y_test)
    # print('tf—idf值')
    # print('k近邻准确率：', accuray2)
    # accuray3 = svm_train(X_train, X_test, y_train, y_test)
    # print('svm准确率：', accuray3)
    # print('召回率', recall1)

    # accuracy4 = gaussian_NB_train(X_train, X_test, y_train, y_test)
    # print('tf—idf值，高斯朴素贝叶斯分类器：',accuracy4)
    #
    # accuracy5 = bernoulli_NB_train(X_train, X_test, y_train, y_test)
    # print('tf—idf值，伯努利贝叶斯分类器：',accuracy5)
    #
    # accuracy6 = multinomial_NB_train(X_train, X_test, y_train, y_test)
    # print('tf—idf值，多项式叶斯分类器：',accuracy6)

    # accuracy7 = rfc_train(X_train, X_test, y_train, y_test)
    # print('tf—idf值，随机森林分类器：', accuracy7)

def test():
    print('test')
    # print(type(X) , type(location))
    # print(X.shape)
    # print(location.shape)
    # X = matrix.matrix_combine(X,location)
    #
    # print(X.shape)
    # m = np.squeeze(np.asarray(X))
    # print(m.shape)
    # print(type(X))
    # X = np.matrix(X,dtype=type(X))
    # print(X)
    # print(X.shape)
    # print(location.shape)
    # print(type(X))
    # print(type(location))
    #
    #
    # print(X.shape)
    # accuray,recall = knn_train(data_split(X,y))
    # print('词频矩阵')
    # print('准确率',accuray)
    # print('召回率',recall)
    #
    # print('------------')
    #
    #
    # combination = []
    # for i,j in zip(X,location):
    #     combination.append(list(i).append(list(j)))
    # X = np.array(combination).reshape(-1,-1)
