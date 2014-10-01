#!/usr/bin/python3.2

import sys

def read_reducer_input(input):
    for line in input:
        yield line.rstrip().split("\t",1)[1]

def reducer():
    for record in read_reducer_input(sys.stdin):
        print(record)

if __name__=="__main__":
    reducer()

