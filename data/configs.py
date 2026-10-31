class Configs:
    def __init__(self):
        self.WISZ = (750, 750)
        self.DISZ = (
            self.WISZ[0] // 2,
            self.WISZ[1] // 2
        )
        self.RENDER_SCALE = 200

        # physics
        self.ELAC = .5
        self.g = 9.81
        self.MASS = 0.05