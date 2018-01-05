import re

'''分句'''
'''传入一个字符串，对字符串进行分句，并返回分句后的结果（list）'''
def extract_senten(content):
    regex = r'。|！|？'
    pattern = re.compile(regex)
    sentences = pattern.split(content)
    for i in sentences:
        print(i.strip())
    return sentences

def extractSentenByPath(path):
    with open(path,'r',encoding='utf-8') as f:
        str = f.read()
        return extract_senten(str)


'''sentences是字符串list，返回含有实体对的字符串list'''
def identify_relation_sentence(sentences,entity_1,entity_2):
    sent = []
    for i in sentences:
        i = str(i)
        if i.find(entity_1)!=-1:
            if i.find(entity_2)!=-1:
                sent.append(i)
    return sent




if __name__ == '__main__':
    # path = 'C:/Users/ypdeng/Desktop/content.txt'
    # with open(path,'r',encoding='utf-8') as f:
    #     str = f.read()
    #     extract_senten(str)

    # regex = '。|！|？'
    # sent = '你们好，我是来自中国的黄晓明。很高兴认识你们！'
    # pattern = re.compile(regex)
    # print(pattern.split(sent))

    # senten = '你们好啊，啊哈哈哈'
    # print(senten.find('hhh'))#不存在返回-1

    senten_1 = '12月18日，永辉超市（601933）复牌开盘涨停，市值再度突破1000亿大关，接近1030亿元。而目前A股商业连锁板块龙头苏宁云商的市值约为1168亿元。日前，永辉超市公告称腾讯拟42亿元受让5%公司股份。'
    sentences = extract_senten(senten_1)
    print(sentences)
    result = identify_relation_sentence(sentences,'永辉超市','腾讯')
    print(result)
    for i in result:
        print(i)