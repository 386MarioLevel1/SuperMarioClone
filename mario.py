import pygame

class Mario:
    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings
        self.mario_image = pygame.image.load("enemyImages/Goomba0.png")
        self.rect = self.mario_image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


    def blitme(self):
        self.screen.blit(self.mario_image, self.rect)
