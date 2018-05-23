# encoding=utf-8

import jieba
import re,os
import csv
import Levenshtein
import data_pro
import json

# 添加值到二位字典中
def addtodict2(thedict, key_a, key_b, val):
    adic=thedict.keys()  #key是key_a的值
    if key_a in adic:
        thedict[key_a].update({key_b: val})
    else:
        thedict.update({key_a:{key_b: val}})


# 比较两个句子之间的Levenshtein距离，获得距离值
def cpsimi(a,b):
    ftr=open(a,'r')
    fte=open(b,'r')
    fa = ftr.readlines()
    fb = fte.readlines()
    ftr.close()
    fte.close()
    dt=dict()
    for i1,line1 in enumerate(fa):
        print line1
        for i2,line2 in enumerate(fb):
            li1=str(line1).split('，')
            ind1=li1[0]
            li2 = str(line2).split('，')
            ind2 = li2[0]
            dis=Levenshtein.distance(li1[1],li2[1])
            addtodict2(dt,int(ind1),int(ind2),dis)
        print dt.keys()
    print dt
    for i,key in enumerate(dt.keys()):
        print i,key
        dt[key] = [(k, v) for (k, v) in dt[key].iteritems()]
        dt[key] = sorted(dt[key], key=lambda x: x[1], reverse=False)[0:21]
    print dt
    dd=dt
    dt=sorted(dt.items())
    w = open('result58.txt', 'w')
    w.write(str("source_id")+'\t'+str("target_id")+'\n')
    for i in range(len(dt)):
        k=dt[i][0]
        v=dt[i][1]
        for i,j in v:
            if(str(k)==str(i)):
                print "same"
            else:
                w.write(str(k) + '\t'+ str(i)+'\n')
    return dd

if __name__=='__main__':
    # 测试数据处理
    data_pro.turncsv('test_data.csv','test_data.txt')
    data_pro.getjieba('test_data.txt','test_datajieba.txt')

    # 训练数据处理
    data_pro.turncsv2('train_data.csv', 'train_data.txt')
    data_pro.getjieba('train_data.txt', 'train_datajieba.txt')

    # 测试距离
    cpsimi('test_datajieba.txt','train_datajieba.txt')