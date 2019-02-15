#!/usr/bin/python

import sys
from pizza import *

def readOutput(filename):
    parts=[]
    file = open(filename, "r")
    nb = int(file.readline())
    for i in range(nb):
        line = file.readline().split(" ")
        parts.append(PizzaPart.fromFile(line))
    return parts


def main(argv):
    if(len(argv)!=3):
        print("usage : python3 show_parts.py <input> <output>")
        exit()
    pizza = readFile(argv[1])
    parts = readOutput(argv[2])

    #fill parts
    for i in range(len(parts)):
        p = parts[i]
        for dx in range(p.dx):
            for dy in range(p.dy):
                c = pizza.tab[p.x+dx][p.y+dy]
                if c!="M" and c!="T":
                    print("part number "+str(i)+" overlap") 
                    exit(42)
                pizza.tab[p.x+dx][p.y+dy]=i%10

    #stats
    tomatoes=0
    mushrooms=0
    for col in pizza.tab:
        for c in col:
            if c=='T':
                tomatoes+=1
            elif c=='M':
                mushrooms+=1
    cellFilled = pizza.w*pizza.h-tomatoes-mushrooms;
    print(str(cellFilled)+"/("+str(pizza.w)+"*"+str(pizza.h)+") = "+str(cellFilled/(pizza.h*pizza.w)))
    print(str(pizza))
        


if __name__ == "__main__":
    main(sys.argv)
