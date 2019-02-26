import math

IN_FOLDER = "../in/"
OUT_FOLDER = "../out/"
FILES = [
    "busy_day",
    "mother_of_all_warehouses",
    "redundancy",
]
file_index = 0
in_file = IN_FOLDER + FILES[file_index] + ".in"
out_file = OUT_FOLDER + FILES[file_index] + ".out"

def distance(r0, c0, r1, c1):
    dr = r0-r1
    dc = c0-c1
    return math.ceil(math.sqrt(dr*dr+dc*dc))

class Simulation:
    def __init__(self, filename):
        f = open(filename, "r")
        (self.R, self.C, self.D, self.T, self.MaxLoad) = map(int, f.readline().split())

        self.products = []
        self.P = int(f.readline())
        p = 0
        for u in map(int, f.readline().split()):
            self.products.append((p, u))
            p += 1

        self.warehouses = []
        self.W = int(f.readline())
        for w in range(0, self.W):
            self.warehouses.append(Warehouse(w, f))

        self.orders = []
        self.O = int(f.readline())
        for o in range(0, self.O):
            self.orders.append(Order(o, f))

        self.drones = []
        (start_r, start_c) = (self.warehouses[0].r, self.warehouses[0].c)
        for d in range(0, self.D):
            self.drones.append(Drone(d, start_r, start_c, self.MaxLoad))

    def printOut(self):
        print(self.R)
        print(self.C)
        print(self.D)
        print(self.T)
        print(self.MaxLoad)

class Warehouse:
    def __init__(self, id, file):
        self.id = id
        (self.r, self.c) = map(int, file.readline().split())
        self.storage = map(int, file.readline().split())

class Drone:
    def __init__(self, id, r, c, maxLoad):
        self.id = id
        self.r = r
        self.c = c
        self.maxLoad = maxLoad
        self.deliveryTime = 0

    def scoreFor(self, simulation, order, time):
        pass

    def deliver(self, order):
        pass


class Order:
    def __init__(self, id, file):
        self.id = id
        (self.r, self.c) = map(int, file.readline().split())
        self.items_count = int(file.readline())
        self.items = {}
        for p in map(int, file.readline().split()):
            if not self.items.has_key(p):
                self.items[p] = 1
            else:
                self.items[p] += 1

simulation = Simulation(in_file)
simulation.printOut()

