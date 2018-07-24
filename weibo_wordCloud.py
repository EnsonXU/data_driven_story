#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 00:31:26 2018

@author: enson
"""

import os
import jieba  
import matplotlib.pyplot as plt 
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 
from wordcloud import WordCloud

tokens = []
result = ""
stop_words = [u'。', u'，', u'“', u'”', u'…', u'？', u'！', u'、', u'；', u'（', 
u'）',u'?',u'：',u'—',u'《',u'》',u'「',u'」',u'月',u'多',u'做',u'好',u'來'
,u'治',u'長',u'的',u'在',u'是',u'與',u'為',u'圖文',u'上',u'人',u'嗎',u'和',u'讓',
u'了',u'3',u'有',u'不',u'你',u'從',u'可',u'我',u'後',u'製',u'個',u'要',u'更',u'用'
,u'大',u'被',u'之',u'年',u'等',u'對',u'吃',u'也',u'啓',u'走',u'到',u'就',u'能',u'都',
u'復',u'歲',u'或',u'把',u'會',u'再',u'10',u'下',u'我們',u'佈',u'於',u'他',u'陳',u'-',
u'名',u'說',u'黃',u'衆',u'(',u'看',u'及',u'\r',u' ',u'中醫',u'中',u'中藥',u'中醫藥'
,u'',u'治療',u'醫藥',u'健康',u'專家',u'患者',u'中國',u'醫院',u'如何',u'複',u'醫'
,u'之路',u'老中',u'如何',u'/',u'@',u':',u'】',u'【',u'"',u'#',u'...',u'个',u'小',u'很'
,u'.',u'链接',u'c',u'11',u',',u'[',u']',u'~',u'网页',u'说',u'其实',u'简单',u'做饭',u'各种'
,u'关注',u'可以',u'_',u'|',u'转载',u'全文',u'展开',u'会',u'我们',u'这',u'给',u'一个',u'为'
,u'分享',u'来',u'还',u'去',u'对',u'1',u'又',u'就是',u'认为',u'爸爸',u'客人',u'视频',u'这里'
,u'而出名',u'客栈',u'民宿',u'良玉']

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
            stop_words.append(line.strip().decode('UTF-8'))

for i in range(len(stop_words)):
    stop_words[i] = stop_words[i].encode('UTF-8')
    
    
s = "".join(stop_words)

y=2012
content=""
for i in range(0,6):
    ms = open("w"+str(y+i)+".txt")  
    for line in ms.readlines():  
        content += "%s "%(line)
with open("weibo_content.txt","a") as mon:
    mon.write(line)

text = open("weibo_content.txt","rb").read()  
jieba.load_userdict('dic.txt')

wordlist = jieba.cut(text,cut_all=True)  
wl = " ".join(wordlist)  

wc = WordCloud(background_color = "white",   
               #mask = "图片",  #设置背景图片  
               max_words = 80,  
               width=1920, 
               height=1080,
               stopwords = s,   
               font_path = "Songti.ttc",  
               max_font_size = 500,  
               random_state = 100, 
    )  
myword = wc.generate(wl)
myword.to_file('WeiBo_wordCloud.png')

plt.imshow(myword)  
plt.axis("off")  
plt.show()  
