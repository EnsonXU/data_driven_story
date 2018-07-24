#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 12:09:47 2018

@author: enson
"""
import os
import jieba
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from collections import Counter

tokens = []
stop_words = [u'。', u'，', u'“', u'”', u'…', u'？', u'！', u'、', u'；', u'（', 
u'）',u'?',u'：',u'—',u'《',u'》',u'「',u'」',u'月',u'多',u'做',u'好',u'來'
,u'治',u'長',u'的',u'在',u'是',u'與',u'為',u'圖文',u'上',u'人',u'嗎',u'和',u'讓',
u'了',u'3',u'有',u'不',u'你',u'從',u'可',u'我',u'後',u'製',u'個',u'要',u'更',u'用'
,u'大',u'被',u'之',u'年',u'等',u'對',u'吃',u'也',u'啓',u'走',u'到',u'就',u'能',u'都',
u'復',u'歲',u'或',u'把',u'會',u'再',u'10',u'下',u'我們',u'佈',u'於',u'他',u'陳',u'-',
u'名',u'說',u'黃',u'衆',u'(',u'看',u'及',u'\r',u' ',u'中醫',u'中',u'中藥',u'中醫藥'
,u'',u'治療',u'醫藥',u'健康',u'專家',u'患者',u'中國',u'醫院',u'如何',u'複',u'醫']
stop_words_file_list = [
    "hit_stopword.txt",
    "baidu_stopword.txt",
    "sichuan_stopword.txt",
    "chinese_stopword.txt"
]
y=2007
for file_path in stop_words_file_list:
    with open(os.path.join(os.path.dirname(__file__), file_path)) as f:
        lines = f.readlines()
        for line in lines:
            stop_words.append(line.strip().decode('utf-8'))
for i in range(0,11):
    with open(os.path.join(os.path.dirname(__file__), str(y+i)+".txt")) as f:
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
    dic=""
    print("****"+str(y+i)+"****")
    for a in counter.most_common(11):
        print(a[0] + '\t' + str(a[1]))
    
'''    
    for a in counter.most_common(102):
        r =  a[0].encode('UTF-8')
        for i in range(1,a[1]):
            result += "%s"%(r)

    for a in counter.most_common(102):
        r =  a[0].encode('UTF-8')
        dic += "%s "%(r)
    
with open("dic.txt", "w") as text_file:
    text_file.write(dic) 
'''
    
print("Out put Success!") 