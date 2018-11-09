import pygame
from pygame.sprite import Sprite
from timer import Timer

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

        self.rightFrames = ["marioImages/minimario8.png", "marioImages/minimario7.png", "marioImages/minimario6.png"]#876
        self.leftFrames = ["marioImages/minimario1.png", "marioImages/minimario2.png", "marioImages/minimario3.png"]#123
        self.stillRight = ["marioImages/minimario5.png"]
        self.stillLeft = ["marioImages/minimario4.png"]


        self.rightTime = Timer(self.rightFrames)
        self.leftTime = Timer(self.leftFrames)
        self.stillTime = Timer(self.stillRight)
        self.stillTime2 = Timer(self.stillLeft)

        self.grav = 0.0
        self.autoGrav = 0.0

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.movingRight = False
        self.movingLeft = False
        self.wasRight = False
        self.wasLeft = False
        self.jump = False
        self.touchingGround = False
        self.inPitfall = False

    def checkStairTouch(self, stairs): #refactor this
        for tile in stairs:
            if self.rect.colliderect(tile):
                self.touchingGround = True
                self.rect.bottom = tile.rect.bottom
                return True
            else:
                return False

    # Makes Mario not go inside the floor
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
        # commeting this entire if out, Mario will never fall down after he jumps
        if self.checkFloorLess(floor):

            if self.jump:
                self.centery += self.grav
                self.rect.centery = self.centery

            #Mario falls down after jump from floor without needing to pressing space
            else:
                self.centery += self.autoGrav
                self.rect.centery = self.centery

        # Allows Mario to jump off the floor
        if self.checkFloorEqual(floor):
            self.touchingGround = True
            self.grav = 0.0
            self.autoGrav = 0.0

        # Not sure what this is needed for
        elif self.grav >= 2.5 or self.autoGrav >= 2.5:
            self.touchingGround = False

        #check comment above
        self.checkFloorGreater(floor)

    def fall(self):
        if self.inPitfall:
            self.centery += .2
            self.rect.centery = self.centery

    def update(self, floor, stairs, smallPitfalls, largePitfalls):
        # self.centery += 1
        # self.rect.centery = self.centery
        for tile in smallPitfalls.sprites():
            for i in range(tile.rect.left, tile.rect.right):
                    if self.rect.left == i and self.rect.bottom == tile.rect.top:
                        # self.centery = 468
                        # self.rect.centery = self.centery
                        self.touchingGround = False
                        self.inPitfall = True


        for hole in largePitfalls.sprites():
            for i in range(hole.rect.left, hole.rect.right+32):
                if self.rect.left == i and self.rect.bottom == hole.rect.top:
                    # self.centery = 468
                    # self.rect.centery = self.centery
                    self.touchingGround = False
                    self.inPitfall = True

        self.gravity(floor)
        self.fall()

        #if this code is disable, we need to hold jump for mario to fall back down
        #otherwise we have to keep  pressing space
        if not self.jump and self.touchingGround:
            self.touchingGround = False

        #Mario jumps
        if self.jump and self.touchingGround:
            self.centery -= 1
            self.rect.centery = self.centery

        #Make Mario fall back down?
        if self.jump and self.grav < 2.5:
            if self.touchingGround:
                self.grav += .005

        #Also helps Mario fall back down
        #have to press space bar again if this code isn't in
        elif not self.jump and self.autoGrav < 2.5:
            if not self.touchingGround:
                self.autoGrav += .005



    def blitme(self):
        # self.screen.blit(self.mario_image, self.rect)
        if self.movingRight:
            self.image2 = pygame.image.load(self.rightTime.imagerect())
            self.wasLeft = False
            self.wasRight = True
        elif self.movingLeft:
            self.image2 = pygame.image.load(self.leftTime.imagerect())
            self.wasRight = False
            self.wasLeft = True
        else:
            if self.wasLeft:
                self.image2 = pygame.image.load(self.stillTime2.imagerect())
            else:
                self.image2 = pygame.image.load(self.stillTime.imagerect())


        self.image2 = pygame.transform.scale(self.image2, (32, 32))
        self.newRect = self.image2.get_rect()
        self.newRect.center = self.rect.center
        self.screen.blit(self.image2, self.newRect)
