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










def solve(simulation):
    t = 0
    while t < simulation.T:
        for d in simulation.drones:
            bestScore = 0
            bestOrder = 0
            for o in simulation.orders:
                if d.scoreFor(o, t) > bestScore:
                    bestScore = d.scoreFor(o, t)  #
                    bestOrder = o
            if bestOrder != 0:
                d.deliver(bestOrder)
        t += 1
