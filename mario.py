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

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.movingRight = False
        self.movingLeft = False
        self.jumping = False

    def update(self):
        if self.movingRight:
            self.centerx += .25
            self.rect.centerx = self.centerx
        if self.movingLeft:
            self.centerx -= .25
            self.rect.centerx = self.centerx



    def blitme(self):
        self.screen.blit(self.mario_image, self.rect)
