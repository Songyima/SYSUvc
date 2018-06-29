#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 用于测试我们的网络,读取中大验证码图片，保存到本地，对其预测
import requests
import os
import cv2
import caffe
import numpy as np
root = '/home/guorui/Data/validate_code/'

deploy=root + 'deploy.prototxt'    #deploy文件
#训练好的 caffemodel
caffe_model=root + 'lenet2__iter_1500.caffemodel'
#加载model和network 
net = caffe.Net(deploy,caffe_model,caffe.TEST)  

def dealgraph(graph):
    x = graph.shape
    for i in xrange(0,x[0]):
        for j in xrange(0,x[1]):
            if (graph[i,j,:] <= 15).all():
                graph[i,j,:] = np.array([255,255,255])
    graph = cv2.cvtColor(graph, cv2.COLOR_BGR2GRAY)
    _ , graph = cv2.threshold(graph,170,255,cv2.THRESH_BINARY)
    return graph


def check(x):
    img=x   #随机找的一张待测图片
    labels_filename = root + 'label.txt'  #类别名称文件，将数字标签转换回类别名称

    #图片预处理设置
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})  #设定图片的shape格式(1,3,28,28)
    transformer.set_transpose('data', (2,0,1))    #改变维度的顺序，由原始图片(28,28,3)变为(3,28,28)
    im=caffe.io.load_image(img, color=False)                   #加载图片
    net.blobs['data'].data[...] = transformer.preprocess('data',im)      #执行上面设置的图片预处理操作，并将图片载入到blob中

    #执行测试
    out = net.forward()

    labels = np.loadtxt(labels_filename, str, delimiter='\t')   #读取类别名称文件
    prob= net.blobs['loss'].data[0].flatten() #取出最后一层（Softmax）属于某个类别的概率值，并打印
    order=prob.argsort()[-1]  #将概率值排序，取出最大值所在的序号 
    # print x
    # print 'the class is:',labels[order],'\n'   #将该序号转换成对应的类别名称，并打印
    return labels[order][len(labels[order])-1]

print '###################'

with requests.Session() as s:
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
        cv2.imwrite(root+'testgraph/%d_%d.jpg'%(i,i), img2)
        print check(root+'testgraph/%d_%d.jpg'%(i,i))