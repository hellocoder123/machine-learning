from numpy import *

def pca(dataMat,k):
	meanData = mean(dataMat,axis=0)
	newDataMat = dataMat-meanData

	covMat = cov(newDataMat,rowvar = 0)
	e,v = linalg.eig(mat(covMat))

	esorted = argsort(e)
	esorted = esorted[:-(k+1):-1]

	rev = v[:,esorted]
	lowData = newDataMat*rev
	reconMat = (lowData*rev.T)+meanData
	return lowData,reconMat


