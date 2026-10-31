import pygame
from math import sin, cos, sqrt, radians


class Cast:
    def __init__(self, Main, obj):
        self.main = Main
        self.obj = obj
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
        self.obj[1] += (50 * self.main.dt) % 360
        points = self.obj[0]
        centre = self.obj[2]

        p0len = len(points[0]) - 1
        p1len = len(points[1]) - 1
        for id, layer in enumerate(points[0]):
            for id2, p in enumerate(layer):
                x, z = self.rotate(p[0], p[2], self.obj[1])
                y = p[1]

                x += centre[0]
                y += centre[1]
                z += centre[2]

                x, y = self.translate_Z(x, y, z)
                x, y = self.translate_coord(x, y)

                points[0][id][id2][-1] = (x, y)

        for id, layer in enumerate(points[1]):
            for id2, p in enumerate(layer):
                x, z = self.rotate(p[0], p[2], self.obj[1])
                y = p[1]

                x += centre[0]
                y += centre[1]
                z += centre[2]

                x, y = self.translate_Z(x, y, z)
                x, y = self.translate_coord(x, y)

                points[1][id][id2][-1] = (x, y)
    

    def render(self):
        points = self.obj[0]

        for layer in points:
            for sub_layer in layer:
                for id, p in enumerate(sub_layer):
                    if not id:
                        prevp = sub_layer[id - 1]
                        self.connect(prevp[-1], p[-1])
