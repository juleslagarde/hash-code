import math
from solve2 import *

IN_FOLDER = "../in/"
OUT_FOLDER = "../out/"
FILES = [
    "example",
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
        (self.R, self.C, self.D, self.T, self.M) = map(int, f.readline().split())

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

        self.warehousesByProducts = {i: [] for i in range(self.P)}
        for w in self.warehouses:
            for pId in w.storage:
                warehouses = self.warehousesByProducts[pId]
                if not w in warehouses:
                    warehouses.append(w)


        self.orders = []
        self.O = int(f.readline())
        for o in range(0, self.O):
            self.orders.append(Order(o, f))

        self.drones = []
        (start_r, start_c) = (self.warehouses[0].r, self.warehouses[0].c)
        for d in range(0, self.D):
            self.drones.append(Drone(d, start_r, start_c, self.M))



    def printOut(self):
        print(self.R)
        print(self.C)
        print(self.D)
        print(self.T)
        print(self.M)
        for warehouse in self.warehouses:
            print(warehouse)
        for order in self.orders:
            print(order)

class Warehouse:
    def __init__(self, id, file):
        self.id = id
        (self.r, self.c) = map(int, file.readline().split())
        self.storage = {}
        p = 0
        for n in map(int, file.readline().split()):
            if n != 0:
                self.storage[p] = n
            p += 1

    def __str__(self):
        return str((self.id, (self.r, self.c), self.storage))

class Drone:
    def __init__(self, id, r, c, M):
        self.id = id
        self.r = r
        self.c = c
        self.M = M
        self.deliveryTime = 0
        self.commands = []

    def scoreFor(self, simulation, order, time):
        totalTime = 0
        pos_r = self.r
        pos_c = self.c
        # gather products
        for pId in order.items:
            closest = None
            for w in simulation.warehousesByProducts[pId]:
                if w.storage[pId] > order.items[pId] and (closest is None or distance(pos_r, pos_c, w.r, w.c) < distance(pos_r, pos_c, closest.r, closest.c)):
                    closest = w
            if closest is None :
                print("no more products "+pId+" in simulation")
                return 0
            totalTime += 1 + distance(pos_r, pos_c, closest.r, closest.c)
            (pos_r, pos_c) = (closest.r, closest.c)
        # deliver
        totalTime += 1 + distance(pos_r, pos_c, order.r, order.c)
        return math.floor(100*(simulation.T-max(time, self.deliveryTime)+totalTime)/simulation.T)

    def deliver(self, simulation, order):
        commands = self.calculateCommands(simulation, order)
        self.commands.append(commands)
        self.deliveryTime += self.timeFromCommands(simulation, self.r, self.c, commands)

    def calculateCommands(self, simulation, order):
        commands = []
        for pId in order.items:
            closest = None
            for w in simulation.warehousesByProducts[pId]:
                if w.storage[pId] > order.items[pId] and (closest is None or distance(pos_r, pos_c, w.r, w.c) < distance(pos_r, pos_c, closest.r, closest.c)):
                    closest = w
            if closest is None :
                print("no more products "+pId+" in simulation")
                return 0
            commands.append(('L', w.id, pId, order.items[pId]))
            (pos_r, pos_c) = (closest.r, closest.c)
        commands.append(('D', order.id, pId, order.items[pId]))
        return commands

    def timeFromCommands(self, simulation, start_r, start_c,  commands):
        time = 0
        pos_r = start_r
        pos_c = start_c
        for c in commands:
            if c[0] == 'W':
                time += c[1]
            elif c[0] == 'L':
                w = simulation.warehouses[c[1]]
                time += 1 + distance(pos_r, pos_c, w.r, w.c)
            elif c[0] == 'D':
                p = simulation.orders[c[1]]
                time += 1 + distance(pos_r, pos_c, p.r, p.c)
            else:
                print("commands "+c[0]+" not understood")

    def getCommands(self):
        return map(lambda e: (self.id,)+e, self.commands)


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

    def __str__(self):
        return str((self.id, (self.r, self.c), self.items))

simulation = Simulation(in_file)
simulation.printOut()
solve(simulation)

for d in simulation.drones:
    for c in d.getCommands():
        print(str(c))