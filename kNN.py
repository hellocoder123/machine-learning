from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

def classfy0(inX,dataSet,labels,k):
	dataSize = dataSet.shape[0]
	diffMat = tile(inX,(dataSize,1))-dataSet
	sqDiffMat = diffMat**2
	distance = sqDiffMat.sum(axis=1)**0.5
	sortedDistance = distance.argsort()
	classCount={}
	for i in range(k):
		voteIlabel = labels[sortedDistance[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
	sortedClassCount = sorted(classCount.iteritems(),
		key = operator.itemgetter(1),reverse = True)
	return sortedClassCount[0][0]

def fileToMatrix(filename):
	fr = open(filename)
	arrayOLines = fr.readlines()
	num = len(arrayOLines)
	matReturn = zeros((num,4))

	index =0
	for line in arrayOLines:
		line = line.strip()
		listFormLine = line.split('\t')
		matReturn[index,:] = listFormLine[0:4]
		index = index+1
	return mat(matReturn)

