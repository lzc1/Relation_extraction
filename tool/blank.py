
#删除字符串中的空格，传入一个list
def remove_listblank(list1):
    for i in list1:
     if ' ' in list1:
         list1.remove(' ')
    return list1

#删除字符串中的空格，传入一个字符串
def remove_strblank(str1 = ' '):
    str2 = str1.strip().split()
    return remove_listblank(str2)

#去除掉文章中的空格，每个词之间以' '隔开
def remove_fileblank(file1):
    corpus = []
    with open(file1, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            corpus.append(remove_strblank(line))
    with open(file1, 'w', encoding='utf-8') as f:
        for i in corpus:
            line = ' '.join(i)
            f.write(line)
            f.write('\n')

if __name__ == '__main__':
    #test
    # str1 = ' 我 爱 中 华 人          民         共  和   国 '
    # print(len(str1))
    # str2 = remove_strblank(str1)
    # print(len(' '.join(str2)))
    # for i in str2:
    #     print(i)

    remove_fileblank(r'C:\Users\ypdeng\PycharmProjects\untitled\model\训练数据.txt')
    remove_fileblank(r'C:\Users\ypdeng\PycharmProjects\untitled\model\data.txt')
    remove_fileblank(r'C:\Users\ypdeng\PycharmProjects\untitled\model\target1.txt')
    print('success')