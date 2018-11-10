import pygame
from pygame.sprite import Sprite

class Goomba(Sprite):
    def __init__(self, screen, ai_settings, x, y):
        super(Goomba, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.goombaImage = pygame.image.load("enemyImages/Goomba0.png")
        self.goombaImage = pygame.transform.scale(self.goombaImage, (32, 32))
        self.rect = self.goombaImage.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx + 32
        self.rect.centery = 384

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.rect.x = x
        self.rect.y = y

    def blitme(self):
        self.screen.blit(self.goombaImage, self.rect)

