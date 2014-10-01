#!/usr/bin/python3.2

import sys

def read_input(input):
    for line in input:
       yield line.rstrip().rsplit(",",1)

def mapper():
    for attribute, label in read_input(sys.stdin):
        print ("{}\t{}".format(label,attribute))

if __name__=="__main__":
    mapper()
