import os

with open('../new wenjian/wgt2.txt', mode='rt', encoding='utf-8') as f, \
        open('new wenjian\wgt3.txt', mode='wt', encoding='utf-8') as f1:
    for res in f:
        line = res.replace('一天', '一年')
        f1.write(line)
os.remove(r'/wgt2.txt')
os.rename('new wenjian\wgt3.txt', '../new wenjian/wgt2.txt')
