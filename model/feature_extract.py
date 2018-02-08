from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

def create_target():
    file1 = open(r'target.txt','w',encoding='utf-8')
    with open(r'C:\Users\ypdeng\PycharmProjects\untitled\model\target1.txt','r',encoding='utf-8') as f:
        for line in f.readlines():
            lines = line.strip().split(' ')
            if lines[2].strip().__len__()==0:
                num = 3
            else:
                num = 2
            if lines[num].find('买卖') != -1:
                file1.write('0')
            elif lines[num].find('合作') != -1:
                file1.write('1')
            elif lines[num].find('合并') != -1:
                file1.write('2')
            elif lines[num].find( '股票') != -1 :
                file1.write('3')
            elif lines[num].find('角色') != -1:
                file1.write('4')
            elif lines[num].find('从属') != -1:
                file1.write('5')
            file1.write('\n')
    file1.close()

if __name__ == '__main__':

    # str = '你们 好  厉害'
    # strs = str.split(' ')

    # print(strs.__len__()) 输出结果为4

    # create_target()

    corpus = []
    #读取文本信息
    with open(r'C:\Users\ypdeng\PycharmProjects\untitled\model\data.txt','r',encoding='utf-8') as f:
        for line in f.readlines():
            corpus.append(line.strip())
    print(corpus)
    # target = []
    # #读取类别信息
    # with open(r'C:\Users\ypdeng\PycharmProjects\untitled\model\target.txt','r',encoding='utf-8') as f:
    #     for line in f.readlines():
    #         target.append(line.strip())
    #
    # #将文本中的词语转为词频矩阵
    # vectorizer = CountVectorizer()
    # X = vectorizer.fit_transform(corpus)
    #
    #
    # print(X.toarray())
    # print(vectorizer.vocabulary_)

    # # 计算Tf-IDf值
    # transform = TfidfTransformer()
    # data = transform.fit_transform(X)
    # data1 = data.toarray()
    # for i in range(len(data1)):
    #     print(data1[i])
    #
    # feature = SelectKBest(chi2,k=10).fit_transform(data1,target)
    # for i in range(len(feature)):
    #     print(feature[i])