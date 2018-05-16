#!/usr/bin/python
# -*- coding: UTF-8 -*-
from numpy import *

def pca(dataMat,k):
	##去中心化
	#求向量每一维的平均值
	meanData = mean(dataMat,axis=0)
	#每一维减去平均值
	newDataMat = dataMat-meanData

	##求数据集的协方差矩阵及其特征与特征向量
	#协方差矩阵，表示不同特征（维度）之间的相关性，对角线为对应特征的方差。
	covMat = cov(newDataMat,rowvar = 0)
	#特征值和特征向量。
	e,v = linalg.eig(mat(covMat))

	##按特征值大小排序，选出最大的k个值
	esorted = argsort(e)#argsort 返回排序后的索引值
	#从后往前取k个
	esorted = esorted[:-(k+1):-1]

	##返回降维后的数据集
	#最大k个特征值对应的特征向量
	rev = v[:,esorted]
	lowData = newDataMat*rev
	reconMat = (lowData*rev.T)+meanData
	return lowData,reconMat


