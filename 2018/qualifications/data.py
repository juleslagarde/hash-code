

class Data:
    def __init__(self, filename):
        self.h = -1 # number of rows
        self.w = -1 # number of columns
        self.cars    = -1 # number of vehicules
        self.nbRides = -1 # number of rides
        self.bonus   = -1 # number of points gain per bonus
        self.maxSteps= -1 # number of steps in the simulation
        self.rides=[]
        self.parse(filename)

    def parse(self,filename):
        file = open(filename, "r")
        params = file.readline().split(" ")
        self.h = int(params[0]) # number of rows
        self.w = int(params[1]) # number of columns
        self.cars    = int(params[2]) # number of vehicules
        self.nbRides = int(params[3]) # number of rides
        self.bonus   = int(params[4]) # number of points gain per bonus
        self.maxSteps= int(params[5]) # number of steps in the simulation
        self.rides=[]
        for i in range(self.nbRides):
            line = file.readline().split()
            self.rides.append(Ride(line))

    def __str__(self):
        out=""
        for attr in self.__dict__:
            out+=attr+":"+getattr(self,attr)
        out+="\n"
        for i in range(self.nbRides):
            out+=str(self.rides[i])
            out+="\n"
        return out

class Ride:
    def __init__(self, params):
        self.originX = int(params[0])
        self.originY = int(params[1])
        self.destX   = int(params[2])
        self.destY   = int(params[3])
        self.start   = int(params[4])
        self.end     = int(params[5])
