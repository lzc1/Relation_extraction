import pickle
import numpy as np

def read_data(file):
    corpus = []
    with open(file,'r',encoding='utf-8') as f:
        for line in f.readlines():
            corpus.append(line.strip())
    file = open('data.pk','wb')
    pickle.dump(corpus,file)
    file.close()
    return corpus

def read_target(file):
    target  = []
    with open(file,'r',encoding='utf-8') as f:
        for line in f.readlines():
            target.append(line.strip())
    file = open('target.pk','wb')
    pickle.dump(target,file)
    file.close()
    return target

def read_loaction(file):
    location = []
    with open(file,'r',encoding='utf-8') as f:
        for line in f.readlines():
            lines = line.strip().split(' ')
            location.append(list(map(int,lines)))
    #将list转为矩阵
    location = np.array(location)
    print(location.shape)
    file = open('location.pk','wb')
    pickle.dump(location,file)
    file.close()
    return location

def load_data():
    file = open(r'C:\Users\ypdeng\PycharmProjects\untitled\tool\data.pk','rb')
    corpus = pickle.load(file)
    file.close()
    return corpus

def load_target():
    file = open(r'C:\Users\ypdeng\PycharmProjects\untitled\tool\target.pk','rb')
    target = pickle.load(file)
    file.close()
    #将字符串转为数字
    target = list(map(int,target))
    return target

def load_location():
    file = open(r'C:\Users\ypdeng\PycharmProjects\untitled\tool\location.pk', 'rb')
    location = pickle.load(file)
    file.close()
    return location

if __name__ == '__main__':
    # read_data(r'C:\Users\ypdeng\PycharmProjects\untitled\data\data.txt')
    # read_target(r'C:\Users\ypdeng\PycharmProjects\untitled\data\target.txt')
    # data = load_data()
    # target = load_target()
    # for i,j in zip(data,target):
    #     print(i,'-----',j)

    read_loaction(r'C:\Users\ypdeng\PycharmProjects\untitled\model\location.txt')
    location = load_location()
    print(location)

