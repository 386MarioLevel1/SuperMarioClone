import pygame

class Mario:
    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings
        self.mario_image = pygame.image.load("marioImages/minimario5.png")
        self.rect = self.mario_image.get_rect()
        self.screen_rect = screen.get_rect()
        self.mario_image = pygame.transform.scale(self.mario_image, (32, 32))
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = 384
        # self.rect.bottom = self.screen_rect.bottom

        self.xlr8 = 0.0
        self.grav = 0.0
        self.autoGrav = 0.0

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.movingRight = False
        self.movingLeft = False
        self.touchingGround = False
        self.jump = False

    def checkFloorTouch(self, floor):
        for rect in floor:
            if self.rect.colliderect(rect):
                #self.centery -= 1
                #self.rect.centery = self.centery
                self.rect.bottom = rect.rect.bottom
                return True

    def checkFloorLess(self, floor):
        for rect in floor:
            if self.rect.bottom < rect.rect.bottom:
                return True

    def accel(self):
        if self.jump and self.xlr8 < 1:
            self.xlr8 += .03

    def gravity(self, floor):
        if self.checkFloorLess(floor):
            if self.jump:
                self.centery += self.grav
                self.rect.centery = self.centery
            else:
                self.centery += self.autoGrav
                self.rect.centery = self.centery
        if self.checkFloorTouch(floor):
            self.touchingGround = True
            self.grav = 0.0
            self.autoGrav = 0.0
        elif self.grav >= 2 or self.autoGrav >= 2:
            self.touchingGround = False

    def update(self, floor):
        self.accel()
        self.gravity(floor)
        if not self.jump and self.touchingGround:
            self.touchingGround = False
        if self.jump and self.touchingGround:
            self.centery -= self.xlr8
            self.rect.centery = self.centery
        if self.jump and self.grav < 2:
            self.grav += .02
        elif not self.jump and self.autoGrav < 2:
            if not self.touchingGround:
                self.autoGrav += .02
            else:
                self.autoGrav += .01



    def blitme(self):
        self.screen.blit(self.mario_image, self.rect)
