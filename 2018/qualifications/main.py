#!/usr/bin/python

import sys
from data import Data
from logic import createsPlanning


#def writeFile(filename, planning):
#    file = open(filename, "w")
#    out = str(planning.length)+"\n"
#    for part in planning:
#        out+=str(part)+"\n"
#    print(filename)

def main(argv):
    if(len(argv)!=3):
        print("usage : python3 main.py <input> <output>")
        exit()
    planning = 0 # Planning()
    data = Data(argv[1])
    createsPlanning(data, planning)
    print(planning)

if __name__ == "__main__":
    main(sys.argv);

