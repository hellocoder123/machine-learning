#!/usr/bin/python
# -*- coding: UTF-8 -*-
from math import log
import operator

#计算给定数据集的香农熵
def calShannoEnt(DataSet):
	numEntries = len(DataSet)
	labelCounts = {}
	for vet in DataSet:
		nowLabel = vet[-1]
		if nowLabel not in labelCounts.keys():
			labelCounts[nowLabel] = 0
		labelCounts[nowLabel] +=1
	Entries = 0.0
	for key in labelCounts.keys():
		prob = float(labelCounts[key])/numEntries
		Entries -= prob*log(prob,2)
	return Entries

#创建数据集,这一部分可以根据具体函数给出
def createDataSet():
	DataSet = [[1,1,'yes'],
				[1,1,'yes'],
				[1,0,'no'],
				[0,1,'no'],
				[0,1,'no']]
	labels = ['no surfacing','filppering']
	return DataSet,labels
#按照给定规则划分数据集 即找出给定属性的属性值相等的项集
def splitDataSet(DataSet,axis,value):
	newDataSet = []
	newFeat =[]
	for featVect in DataSet:
		if(featVect[axis]==value):
			newFeat = featVect[:axis]
			newFeat.extend(featVect[axis+1:])
			newDataSet.append(newFeat)
	return newDataSet

#选择最好的数据集划分方式 遍历所有的特征属性，并比较相应的信息增益
def chooseBestFeatrueToSplit(DataSet):
	numOfFeature = len(DataSet[0])-1
	baseEntropy = calShannoEnt(DataSet)
	bestInfoGain = 0.0;bestFeat = -1
	for i in range(numOfFeature):
		featList = [example[i] for example in DataSet]
		uniqueVals = set(featList)
		newEntropy = 0.0
		for value in uniqueVals:
			subDataSet = splitDataSet(DataSet,i,value)
			prob = len(subDataSet)/float(len(DataSet))
			newEntropy +=prob*calShannoEnt(subDataSet)
		InfoGain = baseEntropy - newEntropy  #???
		if (bestInfoGain < InfoGain):
			bestInfoGain = InfoGain
			bestFeat = i
	return bestFeat

#当数据集处理完所有的属性，但类标签不唯一：多数表决
def majorityCnt(classList):
	classCount = {}#分类计数字典
	for vote in classList:
		if vote not in classCount.keys():
			classCount[vote]= 0
		classCount[vote] += 1
	sortedClassCount = sorted(classCount.iteritems(),\
		key=operator.itemgetter(1),reverse=True)
	return sortedClassCount[0][0]

#递归构造决策树
def creatTree(DataSet,labels):
	classList = [example[-1] for example in DataSet]
	#递归结束条件一：当所有的分支下具有相同的分类
	if (classList.count(classList[0])==len(classList)):
		return classList[0]
	#递归结束条件二：遍历完所有的属性
	if len(DataSet[0])==1:
		return majorityCnt(classList)
	bestFeat = chooseBestFeatrueToSplit(DataSet)
	bestFeatLabel = labels[bestFeat]
	mytree = {bestFeatLabel:{}}
	del(labels[bestFeat])
	featValues = [example[bestFeat] for example in DataSet]
	uniqueVals = set(featValues)
	for value in uniqueVals:
		subLabels = labels[:]
		mytree[bestFeatLabel][value] = creatTree(splitDataSet\
			(DataSet,bestFeat,value),subLabels)
	return mytree

#使用决策树进行分类测试
def classify(inputTree,featLabels,testVec):
	firstStr = inputTree.keys()[0]
	secondDict = inputTree[firstStr]
	featIndex = featLabels.index(firstStr)
	for key in secondDict.keys():
		if testVec[featIndex] == key:
			if type(secondDict[key]).__name__=='dict':
				classLabel = classify(secondDict[key],featLabels,testVec)
			else:	classLabel = secondDict[key]
	return classLabel

def storeTree(inputTree,filename):
    import pickle
    fw = open(filename,'w')
    pickle.dump(inputTree,fw)
    fw.close()
    
def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)



	