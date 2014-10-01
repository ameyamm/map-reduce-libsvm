#!/usr/bin/python3.2

import sys
from numpy import array
from sklearn import preprocessing

def read_input(f):
    
    for line in f:
        yield line.rstrip().rsplit(",",1)

def normalizer():
    
    f = open(sys.argv[1])
    outFileName = sys.argv[1] + ".norm"
    outFile = open(outFileName,'w')

    labelList = list()
    instanceList = list() 

    for attribute, label in read_input(f):
        featureVector = [float(x) for x in attribute.split(",")]
        instanceList.append(featureVector)
        labelList.append(int(label))

    instanceArray = array(instanceList)
    scaler = preprocessing.MinMaxScaler()
    scaledInstance = scaler.fit_transform(instanceArray)

    instanceList = scaledInstance.tolist()
    for i in range(len(instanceList)):
        outFile.write("{},{}\n".format(",".join(str(x) for x in instanceList[i]),labelList[i]))
    outFile.close()
    f.close()

if __name__=="__main__":
    normalizer()
