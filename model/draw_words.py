import jieba
import xlrd
import jieba.posseg as posg#用于词性标注

'''
jieba分词有三种模式：精确模式、全模式、搜索模式
# 精确模式，试图将句子最精确地切开，适合文本分析；  
# 全模式，把句子中所有的可以成词的词语都扫描出来, 速度非常快，但是不能解决歧义；  
# 搜索引擎模式，在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。
默认是精确模式
步骤：
1.定义个人词典
2.过滤停用词
'''
def cut_words(path):
    data = xlrd.open_workbook(path,'r')
    sheets = data.sheets()
    sheet = sheets[0]
    rows = sheet.nrows
    cols = sheet.nrows

    #定义个人词典
    jieba.load_userdict(r'C:\Users\ypdeng\PycharmProjects\untitled\entity_dic\name_dict.txt')

    with open('训练数据.txt','a+',encoding='utf-8') as f:
        for i in range(1,rows):
            content = sheet.cell_value(i,0)
            entity1 = sheet.cell_value(i,1)
            entity2 = sheet.cell_value(i,2)
            relation = sheet.cell_value(i,3)

            contents = seg_sentence(content)
            f.write(contents)
            f.write('\n')
            str = entity1+' '+entity2+' '+relation
            f.write(str)
            f.write('\n')

def stopwordslist(path):
    stopwords = [line.strip() for line in open(path,'r',encoding='utf-8').readlines()]
    return stopwords

def seg_sentence(sentence):
    contents = jieba.cut(sentence.strip())
    stopwords = stopwordslist(r'C:\Users\ypdeng\PycharmProjects\untitled\model\stop_words.txt')
    result = ''
    for word in contents:
        if word not in stopwords:
            if word != ' \t':
                result = result+word
                result = result+' '
    return result

if __name__ == '__main__':
    path = r'C:\Users\ypdeng\Desktop\训练数据.xls'
    cut_words(path)
