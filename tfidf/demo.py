#encoding=utf-8

from zhcnSegment import *
from fileObject import FileObj
from sentenceSimilarity import SentenceSimilarity
from sentence import Sentence
import os
# 添加值到二位字典中
def addtodict2(thedict, key_a, key_b, val):
    adic=thedict.keys()  #key是key_a的值
    if key_a in adic:
        thedict[key_a].update({key_b: val})
    else:
        thedict.update({key_a:{key_b: val}})

def tf():
    dt = {}
# if __name__ == '__main__':
    # 读入训练集
    file_obj = FileObj(r"train_data.txt")
    train_sentences = file_obj.read_lines()

    # 读入测试集
    file_obj = FileObj(r"test_data.txt")
    test1_sentences = file_obj.read_lines()

    # 分词工具，基于jieba分词，我自己加了一次封装，主要是去除停用词
    seg = Seg()

    # 训练模型
    ss = SentenceSimilarity(seg)
    ss.set_sentences(train_sentences)
    ss.TfidfModel()         # tfidf模型
    # ss.LsiModel()         # lsi模型
    # ss.LdaModel()         # lda模型

    # 测试集1
    right_count = 0
    # w=open("result510tf.txt",'w')
    # w.write(str("source_id") + '\t' + str("target_id") + '\n')
    for i in range(len(test1_sentences)):
        print "*********************"
        print i
        print test1_sentences[i]
        test=str(test1_sentences[i].encode("utf-8"))
        t=test.split('，')[0]
        dict = ss.similarity(test1_sentences[i])
        # dict的key为句子的（序号-1），value为计算出的距离
        for k,v in dict:
            print t,k+1,v   # 如2784 2784 1.0
            ind2=k+1
            if(str(k+1)==str(t)):
                print "same"
            else:
                # w.write(str(t) + '\t' + str(k+1) + '\n')
                addtodict2(dt, int(t), int(ind2), v)
    # w.close()
    return dt
        # print test1_sentences[i]
        # print sentence.origin_sentence
        # print sentence.score
    #     if i != sentence.id:
    #         print str(i) + " wrong! score: " + str(sentence.score)
    #     else:
    #         right_count += 1
    #         print str(i) + " right! score: " + str(sentence.score)
    #
    # print "正确率为: " + str(float(right_count)/len(train_sentences))