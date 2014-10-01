#!/usr/bin/python3.2

import sys

def read_input(input):
    for line in input:
        yield line.rstrip().split("\t",1)

def reducer():
    for label, attribute in read_input(sys.stdin):
        print("{},{}".format(attribute,label))

if __name__=="__main__" :
    reducer()

