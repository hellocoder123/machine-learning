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

def file2Matrix(filename):
	fr = open(filename)
	arrayOLines = fr.readlines()
	num = len(arrayOLines)
	matReturn = zeros((num,3))
	classLableVector = []
	index =0
	for line in arrayOLines:
		line = line.strip()
		listFormLine = line.split('\t')
		matReturn[index,:] = listFormLine[0:3]
		classLableVector.append(int(listFormLine[-1]))
		index = index+1
	return matReturn,classLableVector

def autoNorm(dataSet):
	minValues = dataSet.min(0)
	maxValues = dataSet.max(0)
	ranges = maxValues - minValues
	normDataSet = zeros(shape(dataSet))
	m = dataSet.shape[0]
	normDataSet = dataSet - tile(minValues,(m,1))
	normDataSet = normDataSet/tile(ranges,(m,1))
	return normDataSet,ranges,minValues

def datingClassTest():
	hoRatio = 0.10
	datingDataMat,datingLabels = file2Matrix('datingTestSet.txt')
	normMat,ranges,minVals = autoNorm(datingDataMat)
	m = normMat.shape[0]
	numTestVecs = int(m*hoRatio)
	errorCount = 0.0

	for i in range(numTestVecs):
		classfierResult = classfy0(normMat[i,:],normMat[numTestVecs:m,:],
			datingLabels[numTestVecs:m],3)
		print "the classfier come back with: %d,the real answer is: %d"\
		    % (classfierResult,datingLabels[i])
		if (classfierResult != datingLabels[i]): errorCount +=1.0
	print "the total error rate is: %f" % (errorCount/float(numTestVecs))

def classifyPerson():
	resultSet = ['not at all','in small doses','in large doses']
	percentTats = float(raw_input('percnetage of time spent playing video game?'))
	ffMiles = float(raw_input('frequent flier miles earned per year?'))
	iceCream = float(raw_input('liters of ice cream consumed per year?'))
	datingDataMat,datingLabels = file2Matrix('datingTestSet.txt')
	normMat,ranges,minVals = autoNorm(datingDataMat)
	inArr = array([ffMiles,percentTats,iceCream])
	classfierResult = classfy0((inArr-minVals)/ranges,normMat,datingLabels,3)
	print "You will probably like this person: ",resultSet[classfierResult - 1]
	