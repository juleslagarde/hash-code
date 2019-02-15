#!/usr/bin/python

import sys
from pizza import *
from logic import *


def writeFile(filename, parts):
    file = open(filename, "w")
    out = str(len(parts)) + "\n"
    for part in parts:
        out += str(part) + "\n"
    file.write(out)
    print(filename+" written")


def main(argv):
    if(len(argv)!=3):
        print("usage : python3 main.py <input> <output>")
        exit()
    parts = {}
    pizza = readFile(argv[1])
    print(str(pizza))
    createsParts(pizza, parts)
    writeFile(argv[2], parts.values())
    for p in parts:
        print(" " + str(parts[p]))


if __name__ == "__main__":
    main(sys.argv)
