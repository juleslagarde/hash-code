#!/usr/bin/python

import sys
from pizza import *
from logic import *


def writeFile(filename, parts):
    file = open(filename, "w")
    out = str(parts.length) + "\n"
    for part in parts:
        out += str(part) + "\n"
    print(filename)


def main(argv):
    parts = {}
    pizza = readFile(argv[1])
    createsParts(pizza, parts)
    for p in parts:
        print(" " + str(parts[p]))


if __name__ == "__main__":
    main(sys.argv)
