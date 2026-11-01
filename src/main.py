import pygame
import sys
from pygame.locals import *

from pathlib import Path
parent_dir = str(Path(__file__).resolve().parent.parent)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from data.configs import Configs
from gen.objs import Cloth
from gfx.cast import Cast

from phsxtot import phsx

class Main(Configs):
    def __init__(self):
        super().__init__()

        self.win = pygame.display.set_mode(self.WISZ)
        self.dis = pygame.Surface(self.DISZ)
        self.clock = pygame.time.Clock()
        self.dt = 0

        self.obj = Cloth([0, 0, 35], (30, 30, 0), 0).obj
        self.cast = Cast(self)

        self.phsx = phsx.Physx(self)

    def refresh(self):
        self.dis.fill((0, 0, 0))

    def render(self):
        self.cast.render()

    def update(self):
        self.win.blit(
            pygame.transform.scale(self.dis, self.win.get_size()), (0, 0)
        )

        pygame.display.update()

    def rollups(self):
        self.dt = self.clock.tick(60) / 1000

    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        self.phsx.simulate()

        self.cast.vertex_proc()

    def run(self):
        while 1:
            self.rollups()

            self.events()

            self.refresh()

            self.render()

            self.update()

if __name__ == '__main__':
    main = Main()
    main.run()