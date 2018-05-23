# encoding=utf-8
import jieba
import re
import csv
import Levenshtein
import json

# list1="美国地质勘探局：印度莫黑安东南部151公里处发生5.1级地震"
# line1 = re.sub("[0-9\s+\.\!\/_,$%^*()?;；:-【】+\"\']+|[+——！，;:。？、~@#￥%……&*（）]+".decode("utf8"), "".decode("utf8"),list1)
# list2=jieba.cut(line1,cut_all=True)
# print("full:"+",".join(list2))

# list2=jieba.cut("美国地质勘探局：印度莫黑安东南部151公里处发生5.1级地震")
# print("default:"+",".join(list2))
#
# list3=jieba.cut_for_search("美国地质勘探局：印度莫黑安东南部151公里处发生5.1级地震")
# print("search:"+",".join(list3))

# text1 = u'美国 地质 勘探局 印度 莫黑安 东南部 151 公里 处 发生 5.1 级 地震'
# text2 = u'地震 5.1 地质'
# print Levenshtein.distance(text1, text2)

def turncsv(a,b):
    csv_file = csv.reader(open(a,'r'))
    wf = open(b, 'a')
    r='[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+，：。'
    r1="[\s+\.\!\/_,$%^*()(+\"\']+|[+——！，。：；《》【】“”？、~@#￥%……&*（）：]+"
    # [\s +\:\?\;\.\!\ /_,$ % ^ *(+\"\']+|[+——-！：；，。？【】《》()“”、~@#￥%……&*（）]+
    for line in csv_file:
        print line
        lin=unicode(line[1],'gbk')
        text=re.sub(r1.decode("utf8"),''.decode("utf8"),lin)
        wf.write(line[0]+'，'+text.encode("utf8")+'\n')
    wf.close()

def stopw():
    #把停用词做成字典
    stopwords = {}
    fstop = open('stopwords/zhongwen.txt', 'r')
    for eachWord in fstop:
        stopwords[eachWord.strip().decode('utf-8', 'ignore')] = eachWord.strip().decode('utf-8', 'ignore')
    fstop.close()
    return stopwords

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
    dt=sorted(dt.items())
    print dt
    # print dt[0][1]
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
    w.close()
    #
    # w = open('j1.txt', 'w')
    # w.write(str("source_id")+'\t'+str("target_id")+'\n')
    # for i,key in enumerate(dt.keys()):
    #     # dic[i] = [(k, v) for (k, v) in dic[i].iteritems()]
    #     for k, v in dt[key]:
    #         if(str(key)==str(k)):
    #             print "same"
    #         else:
    #             w.write(str(key) + '\t'+ str(k)+'\n')
    # w.close()

# 添加值到二位字典中
def addtodict2(thedict, key_a, key_b, val):
    adic=thedict.keys()  #key是key_a的值
    if key_a in adic:
        thedict[key_a].update({key_b: val})
    else:
        thedict.update({key_a:{key_b: val}})
import os


def turncsv2(a,b):
    csv_file = csv.reader(open(a,'r'))
    wf = open(b, 'a')
    r='[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+，：。'
    r1="[\s+\.\!\/_,$%^*()(+\"\']+|[+——！，。：；《》【】“”？、~@#￥%……&*（）：]+"
    # [\s +\:\?\;\.\!\ /_,$ % ^ *(+\"\']+|[+——-！：；，。？【】《》()“”、~@#￥%……&*（）]+
    for line in csv_file:
        print line
        lin=unicode(line[1],'gbk')
        text=re.sub(r1.decode("utf8"),''.decode("utf8"),lin)
        wf.write(text.encode("utf8")+'\n')
    wf.close()

if __name__=='__main__':
    # turncsv2('test_data.csv','test_data2.txt')
    # getjieba('test_data.txt','test_datajieba.txt')
    #
    # turncsv2('train_data.csv', 'train_data2.txt')
    # getjieba('train_data.txt', 'train_datajieba.txt')
    # cpsimi('test_datajieba.txt','train_datajieba.txt')
    # cpsimi('111.txt', '222.txt')
    # {0: {1: 2, 2: 3}, 1: {3: 2, 5: 4}}
    # dic={0: [(2783, 0), (328925, 16)], 1: [(12056, 0), (178183, 1), (259130, 1)], 2: [(19619, 0), (55769, 39)]}
    # print dic[0]

    f=open('train_data2.txt','r')
    fa=f.readlines()
    for inx,l in enumerate(fa):
        os.chdir("C:\Users\mxf\Desktop\docsim-master\\traindata")
        f1=open("%d.txt" % inx,'w')
        f1.write(l.split('\n')[0])
    print "done"


