import pygame
from imagerect import ImageRect

class Map():
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    BRICK_SIZE = 64
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

# class Pellets():
#     BRICK_SIZE = 7
#
#     def __init__(self, screen, mazefile, pacman):  # , portalfile, shieldfile, pointfile):
#         self.screen = screen
#         self.filename = mazefile
#         with open(self.filename, "r") as f:
#             self.rows = f.readlines()
#
#         self.pelletList = []
#         sz = Pellets.BRICK_SIZE
#
#         self.brick = ImageRect(screen, pacman, sz, sz)
#         #                      screen, square, height, width
#
#         self.deltax = self.deltay = Map.BRICK_SIZE
#
#         self.build()
#
#     def build(self):
#         r = self.brick.rect
#         w, h = r.width, r.height
#         dx, dy = self.deltax, self.deltay
#
#         for nrow in range(len(self.rows)):
#             row = self.rows[nrow]
#             for ncol in range(len(row)):
#                 col = row[ncol]
#                 if col == "O" or col == 'Y':
#                     self.pelletList.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
#
#     def blitme(self):
#         for rect in self.pelletList:
#             self.screen.blit(self.brick.image, rect)
#
# #wtf i added nodes
# class Nodes():
#     BRICK_SIZE = 15
#     def __init__(self, screen, mazefile, pacman):  # , portalfile, shieldfile, pointfile):
#         self.screen = screen
#         self.filename = mazefile
#         with open(self.filename, "r") as f:
#             self.rows = f.readlines()
#
#         self.bricks = []
#         sz = Map.BRICK_SIZE
#
#         self.brick = ImageRect(screen, pacman, sz, sz)
#         #                      screen, square, height, width
#         self.nodes = []
#         self.deltax = self.deltay = Map.BRICK_SIZE
#         self.x = 0
#         self.y = 0
#         self.build()
#
#     def build(self):
#         i = 1
#         r = self.brick.rect
#         w, h = r.width, r.height
#         dx, dy = self.deltax, self.deltay
#
#         for nrow in range(len(self.rows)):
#             row = self.rows[nrow]
#             for ncol in range(len(row)):
#                 col = row[ncol]
#                 if col == "M" or col == 'Y':
#                     self.bricks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
#
#         for rect in self.bricks:
#             self.x = rect.x
#             self.y = rect.y
#             print("Node " + str(i) + " (x,y): (" + str(self.x) + ") (" +
#                   str(self.y) + ")")
#             i += 1
#     def blitme(self):
#         for rect in self.bricks:
#
#             self.screen.blit(self.brick.image, rect)

