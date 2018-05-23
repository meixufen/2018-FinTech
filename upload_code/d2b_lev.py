#coding:utf-8

from ce import d2b
from Levenshtein import cpsimi

# 添加值到二位字典中
def addtodict2(thedict, key_a, key_b, val):
    adic=thedict.keys()  #key是key_a的值
    if key_a in adic:
        thedict[key_a].update({key_b: val})
    else:
        thedict.update({key_a:{key_b: val}})

dt_d2b=d2b()
dt_tf=cpsimi()
dt={}


# 两种方法分别对应两个dt字典，按照1：1的比重计算两个字典中各个键值对，最后得到新的距离字典。
for id,dd in dt_d2b.items():
    print id
    for it,df in dt_tf.items():
        print it
        if(id==it):
            for k1,v1 in dd.items():
                for k2,v2 in df.items():
                    if(k1==k2):
                        va=v1*0.5+v2*0.5
                        addtodict2(dt, id, k1, va)
                        break
                    else:
                        addtodict2(dt, id, k1, v1)
                        addtodict2(dt, id, k2, v2)
            break
        else:
            print "none"

for i, key in enumerate(dt.keys()):
    dt[key] = [(k, v) for (k, v) in dt[key].iteritems()]
    dt[key] = sorted(dt[key], key=lambda x: x[1], reverse=True)[0:20]
dt = sorted(dt.items())
w = open('result510d2b_tf.txt', 'w')
w.write(str("source_id") + '\t' + str("target_id") + '\n')
for i in range(len(dt)):
    k = dt[i][0]
    v = dt[i][1]
    for i, j in v:
        if(k==i):
            print "same"
        else:
            w.write(str(k) + '\t' + str(i) + '\n')
w.close()
