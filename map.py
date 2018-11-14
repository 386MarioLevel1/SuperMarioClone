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
                 floor2, pitfallS, smallPitfalls, pitfallX, largePitfalls, goombas, cloudFile, clouds, bushFile, bushes, mysteryBoxFile, mysteryBoxes, boxFile, boxes, flagTopFile,
                 flagPartFile, flag, castleTopFile, castleTopFile2, castleDoorTopFile, castleDoorPartFile, castle, mountains, pipeTopFile, pipePartFile, pipes):
        self.screen = screen
        self.filename = mazefile
        self.ai_settings = ai_settings
        self.brickfile = brickfile
        self.stairfile = stairfile
        self.cloudFile = cloudFile
        self.bushFile = bushFile
        self.mysteryBoxFile = mysteryBoxFile
        self.boxFile = boxFile
        self.flagTopFile = flagTopFile
        self.flagPartFile = flagPartFile
        self.castleTopFile = castleTopFile
        self.castleTopFile2 = castleTopFile2
        self.castleDoorTopFile = castleDoorTopFile
        self.castleDoorPartFile = castleDoorPartFile
        self.pipeTopFile = pipeTopFile
        self.pipePartFile = pipePartFile
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

        self.mysteryBox = ImageRect(screen, mysteryBoxFile, sz, sz, 0, 0)

        self.regularBox = ImageRect(screen, boxFile, sz, sz, 0, 0)

        self.cloud = ImageRect(screen, cloudFile, ps, int(ps * 0.75), 0, 0, "sceneryImages")

        self.bush = ImageRect(screen, bushFile, int(ps * 0.75), sz, 0, 0, "sceneryImages")

        self.flagTop = ImageRect(screen, flagTopFile, sz, sz, 0, 0)

        self.flagPart = ImageRect(screen, flagPartFile, sz, ps, 0, 0)

        self.castleTop = ImageRect(screen, castleTopFile, sz, sz, 0, 0)

        self.castleDoorTop = ImageRect(screen, castleDoorTopFile, sz, sz, 0, 0)

        self.castleDoorPart = ImageRect(screen, castleDoorPartFile, sz, sz, 0, 0)

        self.rect = self.brick.get_rect()

        self.deltax = self.deltay = Map.BRICK_SIZE

        self.smallPitDeltaX = Map.PS
        self.smallPitDeltaY = Map.BRICK_SIZE

        self.largePitDeltaX = Map.PX
        self.largePitDeltaY = Map.BRICK_SIZE

        self.build(floor, stairs, floor2, smallPitfalls, largePitfalls, goombas, clouds, bushes, mysteryBoxes, boxes, flag, castle, mountains, pipes)

        # self.x_direction = .25
        # self.y_direction = 2

        self.movingRight = False
        self.movingLeft = False

    def update(self, floor, stairs, floor2, smallPitFalls, largePitfalls, clouds, bushes, mysteryBoxes, boxes, flag, castle, mountains, pipes):
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

        for rect in clouds.sprites():
            if self.movingRight:
                rect.movingRight = True
            else:
                rect.movingRight = False
            if self.movingLeft:
                rect.movingLeft = True
            else:
                rect.movingLeft = False

        for rect in bushes.sprites():
            if self.movingRight:
                rect.movingRight = True
            else:
                rect.movingRight = False
            if self.movingLeft:
                rect.movingLeft = True
            else:
                rect.movingLeft = False

        for rect in mysteryBoxes.sprites():
            if self.movingRight:
                rect.movingRight = True
            else:
                rect.movingRight = False
            if self.movingLeft:
                rect.movingLeft = True
            else:
                rect.movingLeft = False

        for rect in boxes.sprites():
            if self.movingRight:
                rect.movingRight = True
            else:
                rect.movingRight = False
            if self.movingLeft:
                rect.movingLeft = True
            else:
                rect.movingLeft = False

        for rect in flag.sprites():
            if self.movingRight:
                rect.movingRight = True
            else:
                rect.movingRight = False
            if self.movingLeft:
                rect.movingLeft = True
            else:
                rect.movingLeft = False

        for rect in castle.sprites():
            if self.movingRight:
                rect.movingRight = True
            else:
                rect.movingRight = False
            if self.movingLeft:
                rect.movingLeft = True
            else:
                rect.movingLeft = False

        for rect in mountains.sprites():
            if self.movingRight:
                rect.movingRight = True
            else:
                rect.movingRight = False
            if self.movingLeft:
                rect.movingLeft = True
            else:
                rect.movingLeft = False

        for rect in pipes.sprites():
            if self.movingRight:
                rect.movingRight = True
            else:
                rect.movingRight = False
            if self.movingLeft:
                rect.movingLeft = True
            else:
                rect.movingLeft = False

    def build(self, floor, stairs, floor2, smallPitfalls, largePitfalls, goombas, clouds, bushes, mysteryBoxes, boxes, flag, castle, mountains, pipes):
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

                elif col == "?":
                    box = ImageRect(self.screen, self.mysteryBoxFile, Map.BRICK_SIZE, Map.BRICK_SIZE, ncol * dx, nrow * dy)
                    mysteryBoxes.add(box)

                elif col == "B":
                    bush = ImageRect(self.screen, self.bushFile, Map.PS, int(Map.PS * 0.75), ncol * dx, nrow * dy, "sceneryImages")
                    bushes.add(bush)

                elif col == "b":
                    box = ImageRect(self.screen, self.boxFile, Map.BRICK_SIZE, Map.BRICK_SIZE, ncol * dx, nrow * dy)
                    boxes.add(box)

                elif col == "c":
                    cloud = ImageRect(self.screen, self.cloudFile, Map.PS, Map.PS, ncol * dx, nrow * dy, "sceneryImages")
                    clouds.add(cloud)

                elif col == "O":
                    flagPart = ImageRect(self.screen, self.flagTopFile, Map.PS, Map.PS, ncol * dx - int(Map.PS * 0.25), nrow * dy - int(Map.PS * 0.25))
                    flag.add(flagPart)

                elif col == "|":
                    flagPart = ImageRect(self.screen, self.flagPartFile, Map.PS, Map.PS, ncol * dx - int(Map.PS * 0.25), nrow * dy - int(Map.PS * 0.25))
                    flag.add(flagPart)

                elif col == "u":
                    castlePart = ImageRect(self.screen, self.castleTopFile, Map.BRICK_SIZE, Map.BRICK_SIZE, ncol * dx, nrow * dy)
                    castle.add(castlePart)

                elif col == 'U':
                    castlePart = ImageRect(self.screen, self.castleTopFile2, Map.BRICK_SIZE, Map.BRICK_SIZE, ncol * dx,
                                           nrow * dy)
                    castle.add(castlePart)

                elif col == "D":
                    castlePart = ImageRect(self.screen, self.castleDoorTopFile, Map.BRICK_SIZE, Map.BRICK_SIZE, ncol * dx, nrow * dy)
                    castle.add(castlePart)

                elif col == "d":
                    castlePart = ImageRect(self.screen, self.castleDoorPartFile, Map.BRICK_SIZE, Map.BRICK_SIZE, ncol * dx, nrow * dy)
                    castle.add(castlePart)

                elif col == "C":
                    castlePart = ImageRect(self.screen, "OWbrick", Map.BRICK_SIZE, Map.BRICK_SIZE, ncol * dx, nrow * dy)
                    castle.add(castlePart)

                elif col == "_":
                    mountainPart = ImageRect(self.screen, "OWmtTop", Map.BRICK_SIZE, Map.BRICK_SIZE, ncol * dx, nrow * dy, "sceneryImages")
                    mountains.add(mountainPart)

                elif col == "/":
                    mountainPart = ImageRect(self.screen, "OWmtSlantLeft", Map.BRICK_SIZE, Map.BRICK_SIZE, ncol * dx, nrow * dy, "sceneryImages")
                    mountains.add(mountainPart)

                elif col == "\\":
                    mountainPart = ImageRect(self.screen, "OWmtSlantRight", Map.BRICK_SIZE, Map.BRICK_SIZE, ncol * dx, nrow * dy, "sceneryImages")
                    mountains.add(mountainPart)

                elif col == "r":
                    mountainPart = ImageRect(self.screen, "OWmtDotRight", Map.BRICK_SIZE, Map.BRICK_SIZE, ncol * dx, nrow * dy, "sceneryImages")
                    mountains.add(mountainPart)

                elif col == "m":
                    mountainPart = ImageRect(self.screen, "OWmtFill", Map.BRICK_SIZE, Map.BRICK_SIZE, ncol * dx, nrow * dy, "sceneryImages")
                    mountains.add(mountainPart)

                elif col == "l":
                    mountainPart = ImageRect(self.screen, "OWmtDotLeft", Map.BRICK_SIZE, Map.BRICK_SIZE, ncol * dx, nrow * dy, "sceneryImages")
                    mountains.add(mountainPart)

                elif col == "p":
                    pipePart = ImageRect(self.screen, self.pipePartFile, int(Map.PS * 0.9), Map.BRICK_SIZE, ncol * dx + int(Map.BRICK_SIZE * 0.1), nrow * dy)
                    pipes.add(pipePart)
                elif col == "P":
                    pipeTop = ImageRect(self.screen, self.pipeTopFile, Map.PS, Map.BRICK_SIZE, ncol * dx, nrow * dy)
                    pipes.add(pipeTop)


    def blitme(self, floor, stairs, floor2, smallPitfalls, largePitfalls, goombas, clouds, bushes, mysteryBoxes, boxes, flag, castle, mountains, pipes):
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

        for rect in mysteryBoxes:
            self.screen.blit(self.mysteryBox.image, rect)

        for rect in boxes:
            self.screen.blit(self.regularBox.image, rect)

        for rect in clouds:
            self.screen.blit(self.cloud.image, rect)

        for rect in bushes:
            self.screen.blit(self.bush.image, rect)

        for rect in flag:
            self.screen.blit(rect.image, rect)

        for rect in castle:
            self.screen.blit(rect.image, rect)

        for rect in mountains:
            self.screen.blit(rect.image, rect)

        for rect in pipes:
            self.screen.blit(rect.image, rect)
