from sklearn.datasets import load_iris#数据集
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier#K近邻分类器
from sklearn import metrics

iris = load_iris()
X = iris.data
y = iris.target

#对数据集进行不同程度的划分，进行交叉验证
for i in range(1,5):
    print('random_state is ',i,'，and accuracy score is ')
    X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=i)#random_state是一个随机种子

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train,y_train)
    y_pred = knn.predict(X_test)
    print(metrics.accuracy_score(y_test,y_pred))
