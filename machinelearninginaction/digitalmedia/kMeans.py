from numpy import *
##kMeans 聚类分析

#处理数据集
def loadDataSet(filename):
	dataMat = []
	fr = open(filename)
	for line in fr.readlines():
		curLine = line.strip().split('\t')
		fltLine = map(float,curLine)
		dataMat.append(fltLine)
	return dataMat

#欧式距离
def cal_distance(vecA,vecB):
	return sqrt(sum(power(vecA - vecB),2))

#初始化簇中心
def randCent(dataSet,k):
	n = shape(dataSet)[1]
	centroids = mat(zeros((k,n)))
	for j in range(n):
		minJ = min(dataSet[:,j])
		ranges = float(max(dataSet[:,j]-minJ))
		centroids[:,j] = minJ+ranges*random.rand(k,1)
	return centroids

##kMeans核心算法
def kMeans(dataSet,k,distMeas = cal_distance,createCent = randCent):
	m = shape(dataSet)[0]
	clusterAssment = mat(zeros((m,2)))
	centroids = createCent(dataSet,k)
	clusterChanged = True
	while clusterChanged:
		clusterChanged = False
		for i in range(m):
			minDist = inf;minIndex = -1
			for j in range(k):
				distJI = distMeas(centroids[j,:],dataSet[i,:])
				if minDist>distJI:
					minDist = distJI;minIndex = j
			if clusterAssment[i,0]!=minIndex:clusterChanged=True
			clusterAssment[i,:] = minIndex,minDist**2
		print centroids
		for i in range(k):
			ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]#get all the point in this cluster
            centroids[cent,:] = mean(ptsInClust, axis=0) #assign centroid to mean 
    return centroids, clusterAssment

