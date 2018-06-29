#!/usr/bin/env python
# -*- coding: utf-8 -*-
# read dealgraph.txt and 去噪，二值化
import cv2
import caffe
import numpy as np
root="/home/guorui/Data/"   #根目录

def read():
    file = open(root+"validate_code/dealgraph.txt")
    while 1:
        line = file.readline()
        if not line:
            break
        print line
        line=line.strip('\n')
        img = cv2.imread(line)
        img = dealgraph(img)
        cv2.imwrite(line.replace('newpics','pics'), img)

def dealgraph(graph):
    x = graph.shape
    for i in xrange(0,x[0]):
        for j in xrange(0,x[1]):
            if (graph[i,j,:] <= 16).all():
                graph[i,j,:] = np.array([255,255,255])
    graph = cv2.cvtColor(graph, cv2.COLOR_BGR2GRAY)
    _ , graph = cv2.threshold(graph,170,255,cv2.THRESH_BINARY)
    return graph

if __name__ == '__main__':
    read()