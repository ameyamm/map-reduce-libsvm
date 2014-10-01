#!/usr/bin/python3.2

import sys
from sklearn import svm
from sklearn import cross_validation
from numpy import array

from header import labelIntMap
from utils_csi5387 import generateFeatureVector
from utils_csi5387 import getReqdLists

def read_input(datafile):
    for line in datafile:
        yield line.rstrip().rsplit(",",1)

def createOVADatasets( datasetList, labelList ):
    ''' 
    Separates the input dataset into n datasets where 
    n is the number of classes. Each dataset is a binary 
    classification problem. Each dataset contains two 
    classes - one representing actual class and other with 
    value 99 for other classes.
    '''
    for X, Y in read_input(sys.stdin) :
        featureVector = generateFeatureVector(X) 

        '''
        if labelIntMap.has_key(Y):
            labelIndex = labelIntMap[Y]
        else :
            labelIntMap[Y] = 
            labelIndex = labelIntMap[Y] 
        '''

        labelIndex = labelIntMap[Y] 

        for i in range(len(labelIntMap)):
            datasetList[i].append(featureVector)
            if labelIndex == i :
                labelList[i].append(int(Y))
            else:
                labelList[i].append(99)
        
        '''featureVectorList.append(featureVector)
        labels.append(Y)
    for i in range(len(datasetList)):
        for j in range(len(datasetList[i])):
            print ("DATASET: {}".format(datasetList[i][j]))
            print ("LABELS: {}".format(labelList[i][j]))
    '''

def generateSupportVectorsForEachClass(datasetList, labelList):
   
    '''
    supportVectorList = [None] * len(labelIntMap)

    for i in len(supportVectorList):
        supportVectorList[i] = list()
    '''
    supportVectorList = list()

    for i in range(len(datasetList)):
        datasetArray = array(datasetList[i])
        if len(set(labelList[i])) <= 1:
            continue 

        labelArray = array(labelList[i])

        svmClassifier = svm.SVC(gamma = 0.1, class_weight = 'auto')#, kernel='linear')
        svmClassifier.fit( X=datasetArray, y=labelArray )
        hyperplaneDistance = svmClassifier.decision_function( X=datasetArray ) 
    
        '''
        print ("Dataset : {}".format(i))

        print ("Number of support vectors: {}".format(len(svmClassifier.support_)))
        print ("SV for each class : {} ".format(svmClassifier.n_support_))
        minDistance = 999
        maxDistance = -999
        '''

        for suppVectorIndex in svmClassifier.support_:    
            
            if labelList[i][suppVectorIndex] != 99 :
                supportVectorList.append( \
                        list([labelList[i][suppVectorIndex]]) + \
                        datasetList[i][suppVectorIndex] )
                '''
                if hyperplaneDistance[suppVectorIndex] <= minDistance:
                    minDistance = hyperplaneDistance[suppVectorIndex]
                if hyperplaneDistance[suppVectorIndex] >= maxDistance:
                    maxDistance = hyperplaneDistance[suppVectorIndex]
                supportVectorSet.add(suppVectorIndex)
                '''

        '''
       # Add remaining instances to supportVector list
        for j in range(len(datasetList[i])):
            if j in supportVectorSet:
                continue
            if labelList[i][j] == 99:
                continue
            if hyperplaneDistance[j] >= minDistance and hyperplaneDistance[j] <= maxDistance:
                supportVectorList.append( \
                        list([labelList[i][j]]) + datasetList[i][j] )
        '''

    return supportVectorList

def mapper(): 

    datasetList, labelList = getReqdLists(len(labelIntMap))

    createOVADatasets( datasetList, labelList )

    supportVectorList = generateSupportVectorsForEachClass(datasetList, labelList)

    classValList = sorted(labelIntMap, key=labelIntMap.get)
    
    for supportVector in supportVectorList:
        print ("{}\t{}".format(supportVector[0], ",".join(str(x) for x in supportVector[1:])))

if __name__ == "__main__":
    mapper()

