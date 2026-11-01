import pygame
from math import sin, cos, sqrt, radians


class Cast:
    def __init__(self, Main):
        self.main = Main
        self.fov = 0
        self.wincoords = []

    def translate_coord(self, x, y):
        return x + (self.main.DISZ[0] / 2), y + (self.main.DISZ[1] / 2)

    def point(self, x, y, s):
        pygame.draw.rect(self.main.dis, (255, 255, 255), (x, y, s, s))

    def translate_Z(self, x, y, z):
        return (x / (z + self.fov)) * self.main.RENDER_SCALE, (y / (z + self.fov)) * self.main.RENDER_SCALE

    def rotate(self, x, z, theta):
        c = cos(radians(theta))
        s = sin(radians(theta))
        _x = (x * c) - (z * s)
        _z = (x * s) + (z * c)

        return _x, _z

    def connect(self, p1, p2):
        pygame.draw.line(self.main.dis, (255, 255, 255), (p1[0], p1[1]), (p2[0], p2[1]))

    def vertex_proc(self):
        self.main.obj[1] += (20 * self.main.dt) % 360
        points = self.main.obj[0]
        centre = self.main.obj[2]

        self.wincoords = []
        for id, layer in enumerate(self.main.obj[0]):
            self.wincoords.append([])
            for id2, p in enumerate(layer):
                p = p[3]
                x, z = self.rotate(p[0], p[2], self.main.obj[1])
                y = p[1]

                x += centre[0]
                y += centre[1]
                z += centre[2]

                x, y = self.translate_Z(x, y, z)
                x, y = self.translate_coord(x, y)

                #print((points[id][id2][3][0], points[id][id2][4][0]))

                self.wincoords[-1].append((x, y))
                #points[id][id2][3] = [x + phsx_adj[0], y + phsx_adj[1]]

    def render(self):
        #points = self.main.obj[0]
        points = self.wincoords

        for id, layer in enumerate(points):
            for id2, p in enumerate(layer):
                if id2:
                    prevp = points[id][id2 - 1]
                    self.connect(prevp, p)
                else:
                    pygame.draw.rect(self.main.dis, (255, 0, 0), (p[0], p[1], 5, 5))

                if id:
                    prevp = points[id - 1][id2]
                    self.connect(prevp, p)

