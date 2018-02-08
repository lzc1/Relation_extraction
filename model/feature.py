from sklearn.datasets import load_iris #IRIS（鸢尾花）数据集
from sklearn.preprocessing import StandardScaler#针对数据进行预处理，标准化
from sklearn.preprocessing import MinMaxScaler#针对数据进行预处理，区间缩放法
from sklearn.preprocessing import Normalizer#针对数据进行预处理，归一化
from sklearn.preprocessing import Binarizer#针对数据进行预处理，对定量特征二值化
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

iris = load_iris()
#特征矩阵
data = iris.data
#目标向量
target = iris.target
for i, v in zip(data,target):
    print(i, "----", v)
print('-----------------')



# #量钢化
# #标准化
# data1 = StandardScaler().fit_transform(data)
# print(data1)
# print('-----------------')
# #区间缩放法
# data2 = MinMaxScaler().fit_transform(data)
# print(data2)
# print('-----------------')
# #归一化
# data3= Normalizer().fit_transform(data)
# print(data3)
# print('-----------------')
# #对定量特征二值化
# data4 = Binarizer(3).fit_transform(data)
# print(data4)
# print('-----------------')
# #卡方检验进行特征选择
# feature = SelectKBest(chi2,k=2).fit_transform(data,target)
# print(feature)




