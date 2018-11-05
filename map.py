import pygame
from imagerect import ImageRect

class Map():
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    BRICK_SIZE = 32
    def __init__(self, screen, mazefile, brickfile):#, portalfile, shieldfile, pointfile):
        self.screen = screen
        self.filename = mazefile
        with open(self.filename, "r") as f:
            self.rows = f.readlines()

        self.bricks = []
        sz = Map.BRICK_SIZE

        self.brick = ImageRect(screen, brickfile, sz, sz)
        #                      screen, square, height, width

        self.rect = self.brick.get_rect()

        self.deltax = self.deltay = Map.BRICK_SIZE

        self.build()

        self.x_direction = .25
        # self.y_direction = 2

        self.movingRight = False
        self.movingLeft = False

    def update(self):
        #random comment
        for rect in self.bricks:
            if self.movingRight:
                rect.x -= self.x_direction

            if self.movingLeft:
                rect.x += self.x_direction

    def build(self):
        r = self.brick.rect
        w, h = r.width, r.height
        dx, dy = self.deltax, self.deltay

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == "X":
                    self.bricks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))

    def blitme(self):
        for rect in self.bricks:
            self.screen.blit(self.brick.image, rect)


