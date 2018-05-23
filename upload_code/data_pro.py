# encoding=utf-8

import jieba
import re,os
import csv
import Levenshtein
import json

# 添加值到二位字典中
def addtodict2(thedict, key_a, key_b, val):
    adic=thedict.keys()  #key是key_a的值
    if key_a in adic:
        thedict[key_a].update({key_b: val})
    else:
        thedict.update({key_a:{key_b: val}})

# 处理test_data.csv文件，去除标点符号，保存为test_data.txt文件后供调用
def turncsv(a,b):
    csv_file = csv.reader(open(a,'r'))
    wf = open(b, 'a')
    r1="[\s+\.\!\/_,$%^*()(+\"\']+|[+——！，。：；《》【】“”？、~@#￥%……&*（）：]+"
    for line in csv_file:
        print line
        lin=unicode(line[1],'gbk')
        text=re.sub(r1.decode("utf8"),''.decode("utf8"),lin)
        wf.write(line[0]+'，'+text.encode("utf8")+'\n')
    wf.close()

# 处理train_data.csv文件，去除标点符号，保存为train_data.txt文件后供调用
def turncsv2(a,b):
    csv_file = csv.reader(open(a,'r'))
    wf = open(b, 'a')
    r1="[\s+\.\!\/_,$%^*()(+\"\']+|[+——！，。：；《》【】“”？、~@#￥%……&*（）：]+"
    for line in csv_file:
        print line
        lin=unicode(line[1],'gbk')
        text=re.sub(r1.decode("utf8"),''.decode("utf8"),lin)
        wf.write(text.encode("utf8")+'\n')
    wf.close()

# 去除停用词
def stopw():
    #把停用词做成字典
    stopwords = {}
    fstop = open('stopwords.txt', 'r')
    for eachWord in fstop:
        stopwords[eachWord.strip().decode('utf-8', 'ignore')] = eachWord.strip().decode('utf-8', 'ignore')
    fstop.close()
    return stopwords

# 使用jieba分词
def getjieba(a,b):
    wf = open(a, 'r')
    w = open(b, 'a')
    for line in wf:
        lin=line.split('\n')[0].split('，')
        lj=jieba.cut(lin[1])
        lw=''
        stopwords=stopw()
        for seg in lj:
            if seg not in stopwords:
                lw+=seg
                lw+=' '
        print lw
        w.write(lin[0]+'，'+lw.encode("utf8")+'\n')
    wf.close()
    w.close()


