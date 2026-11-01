import sys
from pathlib import Path
parent_dir = str(Path(__file__).resolve().parent.parent)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from phsxtot.initf import initialise
from math import sqrt

class Physx:
    def __init__(self, Main):
        self.main = Main

        self.main.obj = initialise(self.main.obj)

    def simulate(self):
        points = self.main.obj[0]
        rest_dis = self.main.obj[3]
        g = self.main.g
        mass = self.main.MASS
        dt = self.main.dt

        #self.main.obj[2][1] += g ** dt

        for id, layer in enumerate(points):
            for id2, p in enumerate(layer):
                if id2:
                    prev_pos = p[3].copy()

                    # apply gravitional force to each point
                    acc = g
                    self.main.obj[0][id][id2][3][0] += (self.main.obj[0][id][id2][3][0] - self.main.obj[0][id][id2][4][0])
                    self.main.obj[0][id][id2][3][1] += (self.main.obj[0][id][id2][3][1] - self.main.obj[0][id][id2][4][1] + acc * (dt ** 2))
                    self.main.obj[0][id][id2][3][2] += (self.main.obj[0][id][id2][3][2] - self.main.obj[0][id][id2][4][2])

                    self.main.obj[0][id][id2][4] = prev_pos

                    # string constraint
                    objx = self.main.obj[0][id][id2][3][0]
                    objy = self.main.obj[0][id][id2][3][1]
                    objz = self.main.obj[0][id][id2][3][2]

                    prevp = self.main.obj[0][id][id2 - 1][3]
                    dx = objx - prevp[0]
                    dy = objy - prevp[1]
                    dz = objz - prevp[2]

                    diff = sqrt(dx ** 2 + dy ** 2 + dz ** 2)

                    err = ((diff - rest_dis) / diff) * 10

                    is_pinned = 0 if (id2 - 1 - 1) == 0 else 1
                    self.main.obj[0][id][id2][3][0] -= dx * err * (.5 + (.5 * (1 - is_pinned))) * dt
                    self.main.obj[0][id][id2][3][1] -= dy * err * (.5 + (.5 * (1 - is_pinned))) * dt
                    self.main.obj[0][id][id2][3][2] -= dz * err * (.5 + (.5 * (1 - is_pinned))) * dt

                    self.main.obj[0][id][id2 - 1][3][0] += (dx * err * .5 * dt) * is_pinned
                    self.main.obj[0][id][id2 - 1][3][1] += (dy * err * .5 * dt) * is_pinned
                    self.main.obj[0][id][id2 - 1][3][2] += (dz * err * .5 * dt) * is_pinned


        #self.main.obj[0] = points



