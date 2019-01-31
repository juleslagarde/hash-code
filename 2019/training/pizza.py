

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

    def readFile(filename):
        file = open(filename, "r")
        line1 = file.readline().split(" ")
        pizza = Pizza(line1)
        for y in range(pizza.h):
            line = file.readline()
            for x in range(pizza.w):
                pizza.tab[x][y]=line[x]
        return pizza

class PizzaPart:
    def __init__(self, x1, y1, x2, y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2

    def __str__(self):
        return str(self.x1)+" "+str(self.y1)+" "+str(self.x2)+" "+str(self.y2)