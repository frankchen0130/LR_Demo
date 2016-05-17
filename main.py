# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 09:55:23 2016

@author: Frankchen
"""

import matplotlib.pyplot as plt
import sys
import numpy as np
from pylab import *


#加载数据
def load_data(data_name):
    dataMat = []
    fr = open(data_name)
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0,float(lineArr[0])])#在第一列加上1.0
    return dataMat

#加载标签
def load_label(label_name):
    labelMat = []
    fr = open(label_name)
    for line in fr.readlines():
        lineArr = line.strip().split()
        labelMat.append(float(lineArr[0]))
    return labelMat


if __name__ == "__main__":
    x = load_data(r'ex2x.dat')
    #print x
    y = load_label(r'ex2y.dat')

    x = np.mat(x)#用np.mat转换成矩阵
    y = np.mat(y).transpose()#将标签转置plt.plot(x[:50], y, 'o')

    m,n = np.shape(x)#获得矩阵行，列数
    lr = 0.07
    theat = np.mat(np.zeros(n))

    # h = np.dot(x, theat.transpose())
    # plt.plot(x[:50], y, 'o')
    # plt.plot(x, h)
    # show()

    for i in range(1000):#迭代次数可以设置的大些
        h = np.dot(x,theat.transpose())
        det_h = h-y
        det_t = lr*(1.0/m)*np.dot(det_h.transpose(),x)


        theat = theat-det_t

        print theat




    #最后展示结果
    plt.plot(x[:50],y,'o') #打印图，在此不打印了
    plt.plot(x, h)
    show()