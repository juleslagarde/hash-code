#!/usr/bin/python

import sys

class Pizza:
    def __init__(self, params):
        self.h=int(params[0])
        self.w=int(params[1])
        self.min=int(params[2])
        self.max=int(params[3])
        #tab[x][y]
        self.tab=[]
        for x in range(self.w):
            self.tab.append([])
            for y in range(self.h):
                self.tab[x].append([])

    def __str__(self):
        out="min:"+str(self.min)+" max:"+str(self.max)+"\n"
        for y in range(self.h):
            for x in range(self.w):
                out+=str(self.tab[x][y])
            out+="\n"
        return out

class PizzaPart:
    def __init__(self, x1, y1, x2, y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2

    def __str__(self):
        return str(self.x1)+" "+str(self.y1)+" "+str(self.x2)+" "+str(self.y2)


def readFile(filename):
    file = open(filename, "r")
    line1 = file.readline().split(" ")
    pizza = Pizza(line1)
    for y in range(pizza.h):
        line = file.readline()
        for x in range(pizza.w):
            pizza.tab[x][y]=line[x]
    return pizza

def createsParts(parts):
    parts.append(PizzaPart(0,0,2,1))
    parts.append(PizzaPart(0,2,2,2))
    parts.append(PizzaPart(0,3,2,4))

def writeFile(filename, parts):
    file = open(filename, "w")
    out = str(parts.length)+"\n"
    for part in parts:
        out+=str(part)+"\n"
    print(filename)

def main(argv):
    parts = []
    pizza = readFile(argv[1])
    createsParts(parts)
    print(pizza)
    for p in parts:
        print(" "+str(p))

if __name__ == "__main__":
    main(sys.argv);

