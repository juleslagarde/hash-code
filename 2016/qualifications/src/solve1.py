
def solve(simulation):
    t = 0
    while t < simulation.T:
        for d in simulation.drones:
            bestScore = 0
            bestOrder = None
            for o in simulation.orders:
                score = d.scoreFor(o, simulation, t)
                if score > bestScore:
                    bestScore = score
                    bestOrder = o
            if not bestOrder is None:
                d.deliver(bestOrder, simulation)
                simulation.orders.remove(bestOrder)
        t += 1

