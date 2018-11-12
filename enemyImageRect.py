import pygame
from pygame.sprite import Sprite

class ImageRect2(Sprite):
    def __init__(self, screen, imagename, height, width, x, y):
        super(ImageRect2, self).__init__()
        self.screen = screen
        name = 'enemyImages/' + imagename + '.png'

        img = pygame.image.load(name)
        img = pygame.transform.scale(img, (height, width))
        self.rect = img.get_rect()
        self.rect.left -= self.rect.width
        self.rect.top -= self.rect.height

        self.image = img

        self.rect.x = x
        self.rect.y = y

        self.xlr8 = 0.0

        self.centerx = float(self.rect.centerx)

        self.movingRight = False
        self.movingLeft = False

    def accel(self):
        if self.movingRight and self.xlr8 > -.5:
            self.xlr8 -= .0015
            #.0015
        elif not self.movingRight and self.xlr8 < 0:
            self.xlr8 += .0015
        if self.movingLeft and self.xlr8 < .5:
            self.xlr8 += .0015
        elif not self.movingLeft and self.xlr8 > 0:
            self.xlr8 -= .0015

    def update(self):
        self.accel()
        if self.movingRight:
            self.centerx += self.xlr8
            self.rect.centerx = self.centerx
        elif self.movingLeft:
            self.centerx += self.xlr8
            self.rect.centerx = self.centerx

    def __str__(self):
        return 'imagerect(' + str(self.image) + str(self.rect) + ')'

    def get_rect(self):
        return self.rect

    def blit(self):
        self.screen.blit(self.image, self.rect)