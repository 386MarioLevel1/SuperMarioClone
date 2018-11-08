import pygame
from imagerect import ImageRect

class Map():
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    BRICK_SIZE = 32
    def __init__(self, screen, mazefile, brickfile, floor, stairfile, stairs):#, portalfile, shieldfile, pointfile):
        self.screen = screen
        self.filename = mazefile
        self.brickfile = brickfile
        self.stairfile = stairfile
        with open(self.filename, "r") as f:
            self.rows = f.readlines()

        self.bricks = []
        sz = Map.BRICK_SIZE

        self.brick = ImageRect(screen, brickfile, sz, sz, 0, 0)
        #                      screen, square, height, width

        self.stair = ImageRect(screen, stairfile, sz, sz, 0 ,0)

        self.rect = self.brick.get_rect()

        self.deltax = self.deltay = Map.BRICK_SIZE

        self.build(floor, stairs)

        # self.x_direction = .25
        # self.y_direction = 2

        self.movingRight = False
        self.movingLeft = False

    def update(self, floor, stairs):
        #random comment
        for rect in floor.sprites():
            if self.movingRight:
                rect.movingRight = True
            else:
                rect.movingRight = False
            if self.movingLeft:
                rect.movingLeft = True
            else:
                rect.movingLeft = False

        for rect in stairs.sprites():
            if self.movingRight:
                rect.movingRight = True
            else:
                rect.movingRight = False
            if self.movingLeft:
                rect.movingLeft = True
            else:
                rect.movingLeft = False


    def build(self, floor, stairs):
        r = self.brick.rect
        w, h = r.width, r.height
        dx, dy = self.deltax, self.deltay

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == "X":

                    #turning every OWfloor into a flooring sprites that are in the floor group?
                    flooring = ImageRect(self.screen, self.brickfile, Map.BRICK_SIZE, Map.BRICK_SIZE,
                                         ncol * dx, nrow * dy)
                    floor.add(flooring)
                elif col == "s":
                    stairing = ImageRect(self.screen, self.stairfile, Map.BRICK_SIZE, Map.BRICK_SIZE,
                                         ncol * dx, nrow * dy)
                    stairs.add(stairing)

    def blitme(self, floor, stairs):
        for rect in floor:
            self.screen.blit(self.brick.image, rect)

        for rect in stairs:
            self.screen.blit(self.stair.image, rect)


