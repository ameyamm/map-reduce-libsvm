#!/usr/bin/python3.2

import sys
import pickle
from numpy import array
from sklearn import svm

from utils_csi5387 import getReqdLists
from utils_csi5387 import generateFeatureVector
from header import labelIntMap

def reducerString(inputFile):
    for line in inputFile:
        keyValue = line.rstrip().split("\t",1)
        label = keyValue[0]
        attribute = keyValue[1]
        yield label, attribute

def createOVADatasets( datasetList, labelList ):
    ''' 
    Separates the input dataset into n datasets where 
    n is the number of classes. Each dataset is a binary 
    classification problem. Each dataset contains two 
    classes - one representing actual class and other with 
    value 99 for other classes.
    '''
    numOfFeatures = None
    for Y, X in reducerString(sys.stdin) :
        featureVector = generateFeatureVector(X) 

        if numOfFeatures is None:
            numOfFeatures = len(featureVector)

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

def buildClassifiers(datasetList, labelList):

    classifierList = list()
    for i in range(len(datasetList)):
        datasetArray = array(datasetList[i])
        if len(set(labelList[i])) <= 1:
            continue 

        labelArray = array(labelList[i])

        svmClassifier = svm.SVC(gamma = 0.1, class_weight = 'auto')
        svmClassifier.fit( X=datasetArray, y=labelArray )
 
        classifierList.append(svmClassifier)
        return classifierList
        

def reducer():
    '''
    datasetList, labelList = getReqdLists(len(labelIntMap))

    createOVADatasets( datasetList, labelList )

    classifierList = buildClassifiers(datasetList, labelList)

    s = pickle.dumps(classifierList)
    print (s)
    for classifier in buildClassifier(datasetList, labelList):
        s = pickle.dumps(classifier)
        print (s)
   ''' 
   # Dump support vectors
    for label, attribute in reducerString(sys.stdin):
        print ("{},{}".format(attribute,label))

if __name__ == "__main__":
    reducer()
