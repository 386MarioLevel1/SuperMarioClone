import pygame
from pygame.sprite import Sprite

class Mario(Sprite):
    def __init__(self, screen, ai_settings):
        super(Mario, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.mario_image = pygame.image.load("marioImages/minimario5.png")
        self.mario_image = pygame.transform.scale(self.mario_image, (32, 32))
        self.rect = self.mario_image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = 384
        # self.rect.bottom = self.screen_rect.bottom

        self.grav = 0.0
        self.autoGrav = 0.0

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.movingRight = False
        self.movingLeft = False
        self.jump = False
        self.touchingGround = False

    def checkStairTouch(self, stairs): #refactor this
        for tile in stairs:
            if self.rect.colliderect(tile):
                self.touchingGround = True
                self.rect.bottom = tile.rect.bottom
                return True
            else:
                return False

    def checkFloorGreater(self, floor): #used to be part of checkFloorTouch
        if pygame.sprite.spritecollideany(self, floor):
            for tile in floor.sprites():
                self.rect.bottom = tile.rect.top

    def checkFloorLess(self, floor): #used to be part of checkFloorTouch
        for tile in floor.sprites():
            if self.rect.bottom < tile.rect.top:
                return True
            else:
                return False

    def checkFloorEqual(self, floor): #used to be part of checkFloorTouch
        for tile in floor.sprites():
            if self.rect.bottom == tile.rect.top:
                return True
            else:
                return False

    def gravity(self, floor):
        if self.checkFloorLess(floor):
            if self.jump:
                self.centery += self.grav
                self.rect.centery = self.centery
            else:
                self.centery += self.autoGrav
                self.rect.centery = self.centery
        if self.checkFloorEqual(floor):
            self.touchingGround = True
            self.grav = 0.0
            self.autoGrav = 0.0
        elif self.grav >= 2.5 or self.autoGrav >= 2.5:
            self.touchingGround = False
        self.checkFloorGreater(floor)

    def update(self, floor, stairs):
        # self.centery += 1
        # self.rect.centery = self.centery
        self.gravity(floor)
        if not self.jump and self.touchingGround:
            self.touchingGround = False
        if self.jump and self.touchingGround:
            self.centery -= 1
            self.rect.centery = self.centery
        if self.jump and self.grav < 2.5:
            if self.touchingGround:
                self.grav += .005
        elif not self.jump and self.autoGrav < 2.5:
            if not self.touchingGround:
                self.autoGrav += .005



    def blitme(self):
        self.screen.blit(self.mario_image, self.rect)
