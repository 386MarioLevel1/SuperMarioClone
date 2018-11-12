import pygame
from pygame.sprite import Sprite

class ImageRect(Sprite):
    def __init__(self, screen, imagename, height, width, x, y, filename=None):
        super(ImageRect, self).__init__()
        self.screen = screen
        if filename is None:
            name = 'blockImages/' + imagename + '.png'
        else:
            name = filename + '/' + imagename + '.png'

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
        if self.movingRight and self.xlr8 > -5:
            self.xlr8 -= 2
            #.0015
        elif not self.movingRight and self.xlr8 < 0:
            self.xlr8 += 2
        if self.movingLeft and self.xlr8 < 5:
            self.xlr8 += 2
        elif not self.movingLeft and self.xlr8 > 0:
            self.xlr8 -= 2

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

    def blit(self): self.screen.blit(self.image, self.rect)


    # if self.moving_right and self.rect.right < self.screen_rect.right:
    #             self.center += self.ai_settings.ship_speed_factor
    #         if self.moving_left and self.rect.left > 0:
    #             self.center -= self.ai_settings.ship_speed_factor
    #
    #         # Update rect object from self.center.
    #         self.rect.centerx = self.center