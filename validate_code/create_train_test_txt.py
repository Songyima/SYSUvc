#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
# parent='D:/Desktop/vcode/'
parent=''
pics='newpics2/'
all_ = ['0','1','2','3','4','5','6','7','8','9','a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i' ,'j', 'k', 'l' ,'m', 'n' ,'o', 'p' ,'q' ,'r' ,'s', 't' ,'u' ,'v', 'w' ,'x', 'y', 'z']

os.remove(parent+'train.txt')
os.remove(parent+'test.txt')

f1=open(parent+'train.txt', 'w')
f2=open(parent+'test.txt', 'w')

for x in xrange(len(all_)):
    tmp = parent+pics+all_[x]

    if os.path.isdir(tmp):
        i=0
        tmpitem = os.listdir(tmp)
        for y in tmpitem:
            if i%25==0:
                f2.write(pics+all_[x]+'/'+y+' %d\n'%x)
            else:
                f1.write(pics+all_[x]+'/'+y+' %d\n'%x)
            i+=1

f1.close()
f2.close()