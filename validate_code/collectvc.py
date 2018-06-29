#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 运行此文件，即可在newpics2下生成验证码数据
import requests
import os
import cv2
import numpy as np
root = '/home/guorui/Data/validate_code/newpics2/'

def dealgraph(graph):
    x = graph.shape
    for i in xrange(0,x[0]):
        for j in xrange(0,x[1]):
            if (graph[i,j,:] <= 15).all():
                graph[i,j,:] = np.array([255,255,255])
    graph = cv2.cvtColor(graph, cv2.COLOR_BGR2GRAY)
    _ , graph = cv2.threshold(graph,170,255,cv2.THRESH_BINARY)
    return graph


with requests.Session() as s:
    for j in xrange(500,502):   
        r=s.get('https://cas.sysu.edu.cn/cas/captcha.jsp')
        local = open(root+'x.jpg', 'wb')
        local.write(r.content)
        local.close()
        img = cv2.imread(root+'x.jpg')

        t=int(90/4)
        for i in range(0,4):
            img2 = img[:,i*t:(i+1)*t]
            img2 = cv2.resize(img2,(32,32))
            # if not os.path.isdir(root+r.cookies['rand'][i].lower()):
            #     os.mkdir(root+r.cookies['rand'][i].lower())
            img2 = dealgraph(img2)

            cv2.namedWindow("FullImageGBR",0)
            cv2.resizeWindow("FullImageGBR", 200, 150);
            cv2.imshow("FullImageGBR", img2)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            print 'Answer?'
            answer = raw_input()
            answer =answer.lower()

            if not os.path.isdir(root+answer):
                os.mkdir(root+answer)
            cv2.imwrite(root+answer+'/%s_%d_%d.jpg'%(answer,j,i), img2)
        print 'We have j: ',j