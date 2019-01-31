#!/usr/bin/python

import sys
from pizza import Pizza, PizzaPart
from logic import createsParts

class Cell:
    def __init__(self, x, y):
        self.x=x
        self.y=y



def createsParts(pizza,parts):
    print("createParts...")
    #tab initialisation 
    tab=[]
    for x in range(pizza.w):
        tab.append([])
        for y in range(pizza.h):
            tab[x].append(Cell(x,y))
    #stats
    tomatoes=0
    mushrooms=0
    for col in pizza.tab:
        for c in col:
            if c=='T':
                tomatoes+=1
            elif c=='M':
                mushrooms+=1
            else:
                print("error:"+c)
    print("T:"+str(tomatoes))
    print("M:"+str(mushrooms))

    #search
    groupId=0
    for col in tab:
        for cell in col:
            cell.groupId=groupId

#   parts.append(PizzaPart(0,0,2,1))
#   parts.append(PizzaPart(0,2,2,2))
#   parts.append(PizzaPart(0,3,2,4))

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

