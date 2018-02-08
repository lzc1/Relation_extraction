from sklearn.feature_extraction.text import CountVectorizer

corpus = ['宣亚国际 终止 收购 映客 股票 巨量 封死 跌停 ',
'日前 永辉超市 公告 称 腾讯 拟 42 亿元 受让 5% 公司 股份',
'腾讯 京东 唯品会 投资 8.63 亿美元 ',
'本文 必康股份 控制 李宗松 专访' ]

vectorizer = CountVectorizer(ngram_range=(2, 2),token_pattern=r'\b\w+\b', min_df=1)
X = vectorizer.fit_transform(corpus)
vocabulary = vectorizer.get_feature_names()
for i in vocabulary:
    print(i)