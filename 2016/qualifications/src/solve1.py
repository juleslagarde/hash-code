
def solve1(simulation):
    t = 0
    while t < simulation.T:
        for d in simulation.drones:
            bestScore = 0
            bestOrder = None
            for o in simulation.orders:
                if d.scoreFor(o, t) > bestScore:
                    bestScore = d.scoreFor(o, t)
                    bestOrder = o
            if not bestOrder is None:
                d.deliver(bestOrder)
                simulation.orders.remove(bestOrder)
        t += 1

