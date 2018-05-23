# encoding=utf-8
import csv
from gensim.models import Word2Vec

csv_file = csv.reader(open('train.csv'))
wf = open('train', 'a')
for line in csv_file:
    print line
    wf.write(line[0])
    wf.write(' ')
    wf.write(line[1])
    wf.write(' ')
wf.close()