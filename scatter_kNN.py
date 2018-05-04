import matplotlib
import matplotlib.pyplot as plt
from numpy import *
import kNN
datingDataMat,datingLabels = kNN.file2Matrix('datingTestSet.txt')
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title('scatter of kNN')
plt.xlabel('asuming in game')
plt.ylabel('asuming in ice cream')
ax1.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))
plt.legend('gi')
plt.show()

