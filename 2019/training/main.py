#!/usr/bin/python

import sys
from pizza import Pizza, PizzaPart
from logic import createsParts


def writeFile(filename, parts):
    file = open(filename, "w")
    out = str(parts.length)+"\n"
    for part in parts:
        out+=str(part)+"\n"
    print(filename)

def main(argv):
    parts = []
    pizza = Pizza.readFile(argv[1])
    createsParts(pizza,parts)
    for p in parts:
        print(" "+str(p))

if __name__ == "__main__":
    main(sys.argv);

