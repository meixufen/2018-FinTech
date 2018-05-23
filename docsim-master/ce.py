#coding:utf-8
#使用docsim方法：doc2bow、similarities判断相似性
from gensim import models,corpora,similarities
import jieba.posseg as pseg
import os

def a_sub_b(a,b):
    ret = []
    for el in a:
        if el not in b:
            ret.append(el)
    return ret

# 添加值到二位字典中
def addtodict2(thedict, key_a, key_b, val):
    adic=thedict.keys()  #key是key_a的值
    if key_a in adic:
        thedict[key_a].update({key_b: val})
    else:
        thedict.update({key_a:{key_b: val}})

# 将txt文件每行保存为一个文档
def getdoc():
    f = open('train_data.txt', 'r')
    fa = f.readlines()
    for inx, l in enumerate(fa):
        os.chdir("C:\Users\mxf\Desktop\docsim-master\\traindata")
        f1 = open("%d.txt" % inx, 'w')
        f1.write(l.split('\n')[0])
    print "done"

# getdoc()

#读取文件
raw_documents=[]

# mxf
a=os.listdir("C:\Users\mxf\Desktop\docsim-master\\traindata1000")  # 文件夹中包含的是每条训练数据处理后的文档，一条数据对应一个文档。
a.sort(key= lambda x:int(x[:-4]))
# print a
for name in a:
    # print name
    f = open(os.path.join("C:\Users\mxf\Desktop\docsim-master\\traindata1000", name), 'r')
    # raw = str(os.path.join(root, name))+" "
    raw=""
    raw += f.read()
    # raw即文档内容
    raw_documents.append(raw)

# 去除停用词
stop = [line.strip().decode('utf-8') for line in open('stopword.txt').readlines() ]

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
similarity = similarities.Similarity('-Similarity-index', corpus, num_features=len(dictionary))

f=open('test_data.txt','r')
fa=f.readlines()
w = open('resultd2b1000.txt', 'w')
w.write(str("source_id") + '\t' + str("target_id") + '\n')
dt=dict()
for li in fa:
    print li
    test_data_1=li.split('\n')[0].split('，')
    ind=test_data_1[0]
    test_cut = pseg.cut(test_data_1[1])
    test_cut_raw_1=[]
    for i in list(test_cut):
        # print i.word
        test_cut_raw_1.append(i.word)
    test_corpus_1 = dictionary.doc2bow(test_cut_raw_1)
    similarity.num_best = 21
    # print(similarity[test_corpus_1])  # 返回最相似的样本材料,(index_of_document, similarity) tuples
    print('################################')
    for i in similarity[test_corpus_1]:
        sim=""
        for j in corpora_documents[i[0]]:
            sim+=j
        print sim   #句子
        ind2=i[0]+1
        print ind,i[0]+1,i[1]     #2784对应的句子所在的序号：i[0]+1 # i[1]序号对应的分值  # 如2784，2784，1.0
        if(int(i[1]==1)):
            print "same"
        else:
            w.write(str(ind) + '\t'+ str(i[0]+1)+'\n')
            addtodict2(dt, int(ind), int(ind2), i[1])
w.close()

print dt
for i,d in dt.items():
    for k,v in d.items():
        print i,d,k,v  # i为最前一个item，d为里面一维字典，k为一维字典的第一个值，v为一维字典的第二个值