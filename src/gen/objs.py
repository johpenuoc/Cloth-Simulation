class Cloth:
    def __init__(self, centre, dim, theta):
        self.fov = 0

        width2 = dim[0] / 2
        height2 = dim[1] / 2
        depth2 = dim[2] / 2

        # generate cloth points
        size = (10, 10)
        ver_points = []
        x = -width2
        y = -height2
        for _ in range(size[1]):
            ver_points.append([])
            for _ in range(size[1]):
                ver_points[-1].append([x, y, depth2])

                y += (height2 / size[1]) * 2

            x += (width2 / size[0]) * 2
            y = -height2

        hoz_points = []
        x = -width2
        y = -height2
        for _ in range(size[0]):
            hoz_points.append([])
            for _ in range(size[0]):
                hoz_points[-1].append([x, y, depth2])

                x += (width2 / size[0]) * 2

            y += (height2 / size[1]) * 2
            x = -width2

        points = [[], []]
        for data in hoz_points:
            points[0].append([[*i, i] for i in data])
        for data in ver_points:
            points[1].append([[*i, i] for i in data])

        self.obj = [
            points, theta, centre
        ]