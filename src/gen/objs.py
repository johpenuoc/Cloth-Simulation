class Cloth:
    def __init__(self, centre, dim, theta):
        self.fov = 0

        width2 = dim[0] / 2
        height2 = dim[1] / 2
        depth2 = dim[2] / 2

        # generate cloth points
        size = (10, 10)
        _points = []
        x = -width2
        y = -height2
        for _ in range(size[1]):
            _points.append([])
            for _ in range(size[1]):
                _points[-1].append([x, y, depth2])

                y += (height2 / size[1]) * 2

            x += (width2 / size[0]) * 2
            y = -height2

    

        points = []
        for data in _points:
            points.append([[*i, i] for i in data])

        self.obj = [
            points, theta, centre
        ]