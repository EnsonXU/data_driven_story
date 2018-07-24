#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 13:19:48 2018

@author: enson
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup

y=2006
output_text=""

'''
for i in range(1,23):   
    print(str(i)+'.html')
    soup = BeautifulSoup(open(str(i)+'.html')) 
    [script.extract() for script in soup.findAll('script')]
    [style.extract() for style in soup.findAll('style')]    
    for t in soup.find_all("font",size="3"):
        output_text += "%s\r"%(str(t.get_text()))     
       
    if(i%2==0):
        y=y+1
        with open(str(y)+".txt", "w") as text_file:
            text_file.write(output_text)
        print("Out put "+str(y)+".txt "+"Success!")         
        output_text=""
'''

for i in range(1,23):   
    print(str(i)+'.html')
    soup = BeautifulSoup(open(str(i)+'.html')) 
    [script.extract() for script in soup.findAll('script')]
    [style.extract() for style in soup.findAll('style')]    
    for t in soup.find_all("font",size="3"):
        output_text += "%s\r"%(str(t.get_text()))     

with open("title.txt", "w") as text_file:
    text_file.write(output_text)
print("Out put Success!")         
        