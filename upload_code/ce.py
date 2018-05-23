#coding:utf-8
#使用docsim方法：doc2bow、similarities判断相似性
from gensim import models,corpora,similarities
import jieba.posseg as pseg
import os
import data_pro

def a_sub_b(a,b):
    ret = []
    for el in a:
        if el not in b:
            ret.append(el)
    return ret


def d2b():
    #读取文件
    raw_documents=[]
    a=os.listdir("C:\Users\mxf\Desktop\docsim-master\\traindata")
    a.sort(key= lambda x:int(x[:-4]))
    # print a
    for name in a:
        f = open(os.path.join("C:\Users\mxf\Desktop\docsim-master\\traindata", name), 'r')
        # raw = str(os.path.join(root, name))+" "
        raw=""
        raw += f.read()
        # raw即文档内容
        raw_documents.append(raw)

    # 去除停用词
    stop = [line.strip().decode('utf-8') for line in open('stopwordd2b.txt').readlines() ]

    #创建语料库
    corpora_documents = []
    for item_text in raw_documents:
        item_str=[]
        item= (pseg.cut(item_text)) #使用jieba分词
        for i in list(item):
            item_str.append(i.word)
        item_str=a_sub_b(item_str,list(stop))
        corpora_documents.append(item_str)

    # 生成字典和向量语料
    dictionary = corpora.Dictionary(corpora_documents) #把所有单词取一个set，并对set中每一个单词分配一个id号的map
    corpus = [dictionary.doc2bow(text) for text in corpora_documents]  #把文档doc变成一个稀疏向量，[(0,1),(1,1)]表明id为0,1的词出现了1次，其他未出现。
    similarity = similarities.Similarity('-Similarity-index11', corpus, num_features=len(dictionary))

    f=open('test_data.txt','r')
    fa=f.readlines()
    dt=dict()
    for li in fa:
        print li
        test_data_1=li.split('\n')[0].split('，')
        ind=test_data_1[0]
        test_cut = pseg.cut(test_data_1[1])
        test_cut_raw_1=[]
        for i in list(test_cut):
            test_cut_raw_1.append(i.word)
        test_corpus_1 = dictionary.doc2bow(test_cut_raw_1)

         # 返回前101条记录，为了尽可能计算两种方法返回的TOP100的值
        similarity.num_best = 101
        print('################################')
        for i in similarity[test_corpus_1]:
            sim=""
            for j in corpora_documents[i[0]]:
                sim+=j
            ind2=i[0]+1
            print ind,i[0]+1,i[1]     #2784对应的句子所在的序号：i[0]+1 # i[1]序号对应的分值  # 如2784，2784，1.0
            if(ind==ind2):
                print "same"
            else:
                data_pro.addtodict2(dt, int(ind), int(ind2), i[1])
    return dt