# coding=utf-8
"""
Created on Oct 28  2019
KNN
@author: HellToto
"""
# coding=utf-8
#!/usr/bin/python
from numpy import *
import operator


class KNNClassifier():
    def __init__(self,k=3):
        self._k=k

    def _calDistance(self,inputX,trainX):
        dataSetSize=trainX.shape[0]
        # tile for array and repeat for matrix in Python
        diffMat=tile(inputX,(dataSetSize,1))-trainX
        sqDiffMat=diffMat**2
        # take the sum of difference from all dimensions,axis=0是按列求和,axis=1 是按行求和
        sqDistances=sqDiffMat.sum(axis=1)
        distances=sqDistances**0.5
        # argsort returns the indices that would sort an array.argsort函数返回的是数组值从小到大的索引值
        # http://www.cnblogs.com/100thMountain/p/4719503.html
        # find the k nearest neighbours
        sortedDistIndicies = distances.argsort()
        return sortedDistIndicies

    def _classify(self,sample,trainX,trainY):
        if isinstance(sample,ndarray) and isinstance(trainX,ndarray) and isinstance(trainY,ndarray):
            pass
        else:
            try:
                sample=array(sample)
                trainX=array(trainX)
                trainY=array(trainY)
            except:
               raise TypeError("numpy.ndarray required for trainX and ..")
        sortedDistIndicies = self._calDistance(sample,trainX)
        classCount = {} # create the dictionary
        for i in range(self._k):
            label=trainY[sortedDistIndicies[i]]
            classCount[label]=classCount.get(label,0)+1
            # get(label,0) : if dictionary 'classCount' exist key 'label', return classCount[label]; else return 0
        sorteditem = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
        # operator.itemgetter(1) can be substituted by 'key = lambda x: x[1]'
        return sorteditem[0][0]

    def classify(self,inputX,trainX,trainY):
        if isinstance(inputX,ndarray) and isinstance(trainX,ndarray) \
            and isinstance(trainY,ndarray):
            pass
        else:
            try:
                inputX = array(inputX)
                trainX = array(trainX)
                trainY = array(trainY)
            except:
              raise TypeError("numpy.ndarray required for trainX and ..")
        d = len(shape(inputX))
        results=[]
        if d == 1:
            result = self._classify(inputX,trainX,trainY)
            results.append(result)
        else:
            for i in range(len(inputX)):
                result = self._classify(inputX[i],trainX,trainY)
                results.append(result)
        return results

if __name__ == "__main__":
    trainX = [[1, 1.1],
              [1, 1],
              [0, 0],
              [0, 0.1]]
    trainY = ['A', 'A', 'B', 'B']
    clf = KNNClassifier(k=3)
    inputX = [[0, 0.1], [1, 1.5]]

    result = clf.classify(inputX, trainX, trainY)

    print(result)