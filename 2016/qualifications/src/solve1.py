
def solve(simulation):
    t = 0
    while t < simulation.T and len(simulation.orders) > 0:
        print("tick ! "+str(t))
        for d in simulation.drones:
            print("drone "+str(d.id)+" . "+str(d.deliveryTime))
            bestScore = 0
            bestOrder = None
            for o in simulation.orders:
                score = d.scoreFor(simulation.orders[o], simulation, t)
                if score > bestScore:
                    bestScore = score
                    bestOrder = o
            if not bestOrder is None:
                d.deliver(simulation, simulation.orders[bestOrder], t)
                simulation.orders.pop(bestOrder)
        t += 1

