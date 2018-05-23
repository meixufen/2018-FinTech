#coding:utf-8
#使用docsim方法：doc2bow、similarities判断相似性
from gensim import models,corpora,similarities
import jieba.posseg as pseg
import os
import jieba

def a_sub_b(a,b):
    ret = []
    for el in a:
        if el not in b:
            ret.append(el)
    return ret
    
#读取文件
raw_documents=[]
walk = os.walk(os.path.realpath("C:\Users\mxf\Desktop\docsim-master"))
raw=""
f=open('10.txt','r')
raw += f.read()
# print raw
raw_documents.append(raw)
# print raw_documents[0]
stop = [line.strip().decode('utf-8') for line in open('stopword.txt').readlines() ]
ft=open('10.txt','r')
fa=ft.readlines()
item_str=[]
corpora_documents = []
for item_text in fa:
    item_text=item_text.split('\n')[0]
    print item_text
    item = jieba.cut(item_text)
    item_str.append(item)
    item_str = a_sub_b(item_str, list(stop))
corpora_documents.append(item_str)
#创建语料库

# for item_text in raw_documents:
#     print item_text
#     item_str=[]
#     item=jieba.cut(item_text)
#     # item= (pseg.cut(item_tiext)) #使用jieba分词
#     l=''
#     w=open('11.txt','w')
#     for i in list(item):
#         print i
#         # item_str.append(i)
#         for seg in item:
#             l += seg
#             l += ' '
#         print l
#         w.write(l.encode("utf8") + '\n')
#     item_str=a_sub_b(item_str,list(stop))
#     corpora_documents.append(item_str)

# 生成字典和向量语料
dictionary = corpora.Dictionary(corpora_documents) #把所有单词取一个set，并对set中每一个单词分配一个id号的map
corpus = [dictionary.doc2bow(text) for text in corpora_documents]  #把文档doc变成一个稀疏向量，[(0,1),(1,1)]表明id为0,1的词出现了1次，其他未出现。
similarity = similarities.Similarity('-Similarity-index', corpus, num_features=999999999)

test_data_1 = "本报讯全球最大个人电脑制造商戴尔公司８日说，由于市场竞争激烈，以及定价策略不当，该公司今年第一季度盈利预计有所下降。"
print test_data_1
test_cut = pseg.cut(test_data_1)
test_cut_raw_1=[]
for i in list(test_cut):
    # print i
    test_cut_raw_1.append(i.word)
test_corpus_1 = dictionary.doc2bow(test_cut_raw_1)
similarity.num_best = 5
print similarity[test_corpus_1]  # 返回最相似的样本材料,(index_of_document, similarity) tuples
for i in similarity[test_corpus_1]:
    sim=""
    print('################################')
    print i[0]
    for j in corpora_documents[i[0]]:
        sim+=j
    print sim