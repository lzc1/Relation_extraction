from gensim import corpora
from gensim import models
import pickle

def split_data(file):
    judge = True
    file1 = open('data.txt','w',encoding='utf-8')
    file2 = open('target.txt','w',encoding='utf-8')
    with open(file,'r',encoding='utf-8') as f:
        for line in f.readlines():
            if judge:
                judge=False
                file1.write(line)
                #file1.write('\n')
            else:
                judge = True
                file2.write(line)
                #file2.write('\n')
    file2.close()
    file1.close()

def read_data(file):
    corpus = []
    with open(file,'r',encoding='utf-8') as f:
        for line in f.readlines():
            corpus.append(line.strip())
    return corpus

def test():
    x= 1
    y = 1
    return x,y

if __name__ == '__main__':
    # split_data(r'C:\Users\ypdeng\PycharmProjects\untitled\model\训练数据.txt')
    # dictionary = corpora.Dictionary()
    # with open('data.txt','r',encoding='utf-8') as f:
    #     for line in f.readlines():
    #         lines = line.strip().split(' ')
    #         for i in range(lines.__len__())[::-1]:#去掉数字
    #             if lines[i].isdigit():
    #                 lines.pop(i)
    #             if lines[i].find('.'):
    #                 lines.pop(i)
    #             # elif lines[i].find('%'):
    #             #     lines.pop(i)
    #         #print(type(lines))
    #         dictionary.add_documents([lines])
            #print(type([lines]))
    # for i in dictionary:
    #     print(i,dictionary[i])

    #可以使用pickle来存储模型
    # pickle存储方式默认是二进制方式
    # file = open('dictionary.txt','wb+')
    # pickle.dump(dictionary,file)
    # file.close()
    #使用pickle得到保存的模型
    # with open('dictionary.txt','rb') as f:
    #     dic = pickle.load(f)
    #     # print(dic)

    # #去掉词典中出现次数少的低频词
    # few_freqIds = [num for num,word in dictionary.dfs.items() if word<5]
    # dictionary.filter_tokens(few_freqIds)
    # dictionary.compactify()
    # dictionary.save('dictionary.txt')

    # dictionary = corpora.Dictionary.load('dictionary.txt')
    # dictionary.filter_tokens([0])
    # dictionary.save('dictionary.txt')
    # print('-----')
    # for i in dictionary:
    #     print(i,dictionary[i])

    dictionary = corpora.Dictionary.load('dictionary.txt')
    for i in dictionary:
        print(i,dictionary[i])

   # 词袋模型形成的词向量
    bow = []
    with open('data.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
                lines = line.strip().split(' ')
                word_bow = dictionary.doc2bow(lines)
                bow.append(word_bow)
    # for i in bow:
    #     print(i)

    #tfidf向量
    # corpus = read_data(r'data.txt')
    # for i in corpus:
    #     print(i)
    tfidf_model = models.TfidfModel(bow)
    corpus_tfidf = tfidf_model[bow]
    for item in corpus_tfidf:
        print(item)
    # for i in tfidf_model:
    #     print(i)
    # for doc in corpus:
    #     print(tfidf_model[doc])

    # print(tfidf_model['宣亚国际 终止 收购 映客  股票 巨量 封死 跌停'])
    # for i in tfidf_model:
    #     print(i)
    # print(type(tfidf_model))
    # corpus_tfidf = [tfidf_model[doc] for doc in corpus]
    # for i in corpus_tfidf:
    #     print(i)

    # 测试
    # num1= test()
    # print(num1)

    # str = '中华人民共和国万岁'
    # str1,str2 = str.split(':',1)
    # print(str1,str2)
    #ValueError: not enough values to unpack (expected 2, got 1)

    # str = '中华人民共和国万岁'
    # str1 = ''
    # for i in str:
    #     str1 = str1+i
    #     str1 = str1+' '
    # print(str1.strip())