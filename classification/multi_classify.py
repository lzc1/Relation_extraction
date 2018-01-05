from sklearn.neural_network import  MLPClassifier
from sklearn.externals import joblib

#基于多感知器的神经网络模型分类器
# X = [[0.,0.],[1.,1.]]
# Y = [0,1]
#
# clf = MLPClassifier(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(5,2),random_state=1)
# clf.fit(X,Y)
# #保存模型
# joblib.dump(clf,'train_model.m')
#将模型从本地调回
clf = joblib.load('train_model.m')

print(clf.predict([[2.,2.],[-1.,-2]]))