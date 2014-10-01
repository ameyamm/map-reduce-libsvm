#!/usr/bin/python

import sys
def read_instance(file):
    for line in file:
        splitValue = line.rsplit(",",1) 
        attribute = splitValue[0]
        label = splitValue[1]
        yield label, attribute

def main():
    
    for label, attributes in read_instance(sys.stdin):
        print ("{}\t{}".format(label, attributes))

if __name__ == "__main__":
    main()
