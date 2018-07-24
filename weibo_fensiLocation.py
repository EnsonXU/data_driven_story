#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 00:48:15 2018

@author: enson
"""


import os
import jieba
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from collections import Counter

tokens = []

stop_words = [u' ',u'其他',u'深圳',u'东城区',u'大连',u'地址',u'济南',u'杭州',
u'郑州',u'武汉',u'长沙',u'厦门',u'苏州',u'南京',u'合肥',u'哈尔滨',u'青岛',u'湖州',u'无锡'
,u'福州',u'阜阳',u'贵阳',u'沈阳',u'浦东新区',u'通化']
stop_words_file_list = [
    "hit_stopword.txt",
    "baidu_stopword.txt",
    "sichuan_stopword.txt",
    "chinese_stopword.txt"
]

for file_path in stop_words_file_list:
    with open(os.path.join(os.path.dirname(__file__), file_path)) as f:
        lines = f.readlines()
        for line in lines:
            stop_words.append(line.strip().decode('utf-8'))

jieba.add_word("location_dic.txt")

with open(os.path.join(os.path.dirname(__file__), "fensi.txt")) as f:
    lines = f.readlines()
    for line in lines:
        clean_line = line.strip()
        if len(clean_line) > 0:
                seg_list = jieba.cut(clean_line)
                for seg in seg_list:
                    if seg not in stop_words:
                        tokens.append(seg)
                    
counter = Counter(tokens)
result=""
totalnum=0
for a in counter.most_common(57):
    print(a[0] + '\t' + str(a[1]))
    totalnum += a[1]
print(str(totalnum)) 
    
print("Out put Success!") 