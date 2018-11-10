import pygame
from imagerect import ImageRect
from goomba import Goomba

class Map():
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    BRICK_SIZE = 32
    PS = 64
    PX = 86
    def __init__(self, screen, ai_settings, mazefile, brickfile, floor, stairfile, stairs,
                 floor2, pitfallS, smallPitfalls, pitfallX, largePitfalls, goombas):
        self.screen = screen
        self.filename = mazefile
        self.ai_settings = ai_settings
        self.brickfile = brickfile
        self.stairfile = stairfile
        self.pitfallS = pitfallS
        self.pitfallX = pitfallX
        with open(self.filename, "r") as f:
            self.rows = f.readlines()

        self.bricks = []
        sz = Map.BRICK_SIZE
        ps = Map.PS
        pz = Map.PX

        self.brick = ImageRect(screen, brickfile, sz, sz, 0, 0)
        #                      screen, square, height, width

        self.stair = ImageRect(screen, stairfile, sz, sz, 0, 0)

        self.holeS = ImageRect(screen, pitfallS, sz, ps, 0, 0)

        self.holeX = ImageRect(screen, pitfallX, sz, pz, 0, 0)

        self.rect = self.brick.get_rect()

        self.deltax = self.deltay = Map.BRICK_SIZE

        self.smallPitDeltaX = Map.PS
        self.smallPitDeltaY = Map.BRICK_SIZE

        self.largePitDeltaX = Map.PX
        self.largePitDeltaY = Map.BRICK_SIZE

        self.build(floor, stairs, floor2, smallPitfalls, largePitfalls, goombas)

        # self.x_direction = .25
        # self.y_direction = 2

        self.movingRight = False
        self.movingLeft = False

    def update(self, floor, stairs, floor2, smallPitFalls, largePitfalls):
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

        for rect in smallPitFalls.sprites():
            if self.movingRight:
                rect.movingRight = True
            else:
                rect.movingRight = False
            if self.movingLeft:
                rect.movingLeft = True
            else:
                rect.movingLeft = False

        for rect in largePitfalls.sprites():
            if self.movingRight:
                rect.movingRight = True
            else:
                rect.movingRight = False
            if self.movingLeft:
                rect.movingLeft = True
            else:
                rect.movingLeft = False

        for rect in floor2.sprites():
            if self.movingRight:
                rect.movingRight = True
            else:
                rect.movingRight = False
            if self.movingLeft:
                rect.movingLeft = True
            else:
                rect.movingLeft = False


    def build(self, floor, stairs, floor2, smallPitfalls, largePitfalls, goombas):
        r = self.brick.rect
        w, h = r.width, r.height
        dx, dy = self.deltax, self.deltay

        SPdx, SPdy = self.smallPitDeltaX, self.smallPitDeltaY
        LPdx, LPdy = self.largePitDeltaX, self.largePitDeltaY

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
                elif col == "x":
                    flooring2 = ImageRect(self.screen, self.brickfile, Map.BRICK_SIZE, Map.BRICK_SIZE, ncol * dx, nrow * dy)
                    floor2.add(flooring2)

                elif col == ",":
                    falling = ImageRect(self.screen, self.pitfallS, Map.BRICK_SIZE, Map.PS,
                                         ncol * dx, nrow * dy)
                    smallPitfalls.add(falling)

                elif col == "Q":
                    death = ImageRect(self.screen, self.pitfallX, Map.BRICK_SIZE, Map.PX,
                                         ncol * dx, nrow * dy)
                    largePitfalls.add(death)

                elif col == "G":
                    loomba = Goomba(self.screen, self.ai_settings, ncol * dx, nrow * dy)
                    goombas.add(loomba)


    def blitme(self, floor, stairs, floor2, smallPitfalls, largePitfalls, goombas):
        for rect in floor:
            self.screen.blit(self.brick.image, rect)

        for rect in stairs:
            self.screen.blit(self.stair.image, rect)

        for rect in floor2:
            self.screen.blit(self.brick.image, rect)

        for rect in smallPitfalls:
            self.screen.blit(self.holeS.image, rect)

        for rect in largePitfalls:
            self.screen.blit(self.holeX.image, rect)

        for rect in goombas:
            rect.blitme()
