#!/usr/bin/python3.2

import sys

from header import labelIntMap

labelInstanceCount = [0] * len(labelIntMap) 

def read_input(datafile):
    for line in datafile:
        yield line.rstrip().rsplit(",",1)

def mapper():
    
    for attributes,label in read_input(sys.stdin):
       key = labelInstanceCount[int(label) - 1]
       labelInstanceCount[int(label) - 1] += 1
       print ("{}\t{},{}".format(int(key), attributes, label))

if __name__ == "__main__":
    mapper()
