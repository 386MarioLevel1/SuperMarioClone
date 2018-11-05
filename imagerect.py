import pygame

class ImageRect:
    def __init__(self, screen, imagename, height, width):
        self.screen = screen
        name = 'blockImages/' + imagename + '.png'

        img = pygame.image.load(name)
        img = pygame.transform.scale(img, (height, width))
        self.rect = img.get_rect()
        self.rect.left -= self.rect.width
        self.rect.top -= self.rect.height

        self.image = img

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