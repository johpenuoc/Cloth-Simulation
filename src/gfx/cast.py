import pygame
from math import sin, cos, sqrt, radians


class Cast:
    def __init__(self, Main):
        self.main = Main
        self.fov = 0

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
        self.main.obj[1] += (50 * self.main.dt) % 360
        points = self.main.obj[0]
        centre = self.main.obj[2]

        for id, layer in enumerate(points):
            for id2, p in enumerate(layer):
                x, z = self.rotate(p[0], p[2], self.main.obj[1])
                y = p[1]

                x += centre[0]
                y += centre[1]
                z += centre[2]

                x, y = self.translate_Z(x, y, z)
                x, y = self.translate_coord(x, y)

                points[id][id2][3] = (x, y)
    

    def render(self):
        points = self.main.obj[0]

        for id, layer in enumerate(points):
            for id2, p in enumerate(layer):
                if not id2:
                    prevp = points[id][id2 - 1]
                    self.connect(prevp[-1], p[-1])

                if not id:
                    prevp = points[id - 1][id2]
                    self.connect(prevp[-1], p[-1])

