from init import init
from random import uniform

class Physx:
    def __init__(self, Main):
        self.main = Main

        self.main.obj = init(self.main.obj)

    def simulate(self):
        points = self.main.obj
        g = self.main.g
        mass = self.main.mass
        dt = self.main.dt

        for id, layer in enumerate(points[0]):
            for id2, p in enumerate(layer):
                if not id2:
                    appf = p[-1]

                    variation = 1 - uniform(0, 1)
                    #f = g * (mass * variation)

                    prevy = points[0][id][id2][-1][1]
                    points[0][id][id2][-1][1] += g * dt

                    ychange = points[0][id][id2][-1][1] - prevy

                    f = (500 * ychange) / mass
                    points[0][id][id2][-1][1] -= f * dt
                    


