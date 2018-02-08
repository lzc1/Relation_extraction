from tool import datasets
from gensim import corpora
from gensim import models
import jieba

'''
使用gensim的doc2bow实现词袋模型
'''
def get_rawdata():
    data = datasets.load_data()
    rawdata  = []
    for doc in data:
        words = doc.strip().split(' ')
        rawdata.append(words)
    return rawdata

if __name__ == '__main__':
    #建立词典
    rawdata = get_rawdata()
    # print(rawdata)
    dictionary = corpora.Dictionary(rawdata)#此处的rawdata为集合的集合，是分词后的句子的集合
    # for i in dictionary:
    #     print(i,'------',dictionary[i])

    #得到词袋
    docbow = [dictionary.doc2bow(text) for text in rawdata]
    # print(docbow)
    # for i in docbow:
    #     print(i)

    #tf-idf模型
    tfidf_model = models.TfidfModel(docbow)#参数是词袋模型
    tfidf = tfidf_model[docbow]
    # print(tfidf)
    for i in tfidf:
        print(i)


    #test
    # raw_documents = [
    #     '0无偿居间介绍买卖毒品的行为应如何定性',
    #     '1吸毒男动态持有大量毒品的行为该如何认定',
    #     '2如何区分是非法种植毒品原植物罪还是非法制造毒品罪',
    #     '3为毒贩贩卖毒品提供帮助构成贩卖毒品罪',
    #     '4将自己吸食的毒品原价转让给朋友吸食的行为该如何认定',
    #     '5为获报酬帮人购买毒品的行为该如何认定',
    #     '6毒贩出狱后再次够买毒品途中被抓的行为认定',
    #     '7虚夸毒品功效劝人吸食毒品的行为该如何认定',
    #     '8妻子下落不明丈夫又与他人登记结婚是否为无效婚姻',
    #     '9一方未签字办理的结婚登记是否有效',
    #     '10夫妻双方1990年按农村习俗举办婚礼没有结婚证 一方可否起诉离婚',
    #     '11结婚前对方父母出资购买的住房写我们二人的名字有效吗',
    #     '12身份证被别人冒用无法登记结婚怎么办？',
    #     '13同居后又与他人登记结婚是否构成重婚罪',
    #     '14未办登记只举办结婚仪式可起诉离婚吗',
    #     '15同居多年未办理结婚登记，是否可以向法院起诉要求离婚'
    # ]
    # texts = [[word for word in jieba.cut(document, cut_all=True)] for document in raw_documents]
    # print(texts)