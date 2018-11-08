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

    def update(self, floor, stairs):
        self.centery += 1
        self.rect.centery = self.centery

        #                 for rect2 in maze.bricks:
        #                     if rect.colliderect(rect2):
        #                         # self.y_hit = self.y
        #                         # self.hit_right = True
        #                         self.x = self.x - self.x_direction
        #                         rect.x = self.x
        #                         return

        for tile in floor:
            if self.rect.colliderect(tile):
                self.centery -= 1
                self.rect.centery = self.centery
                return

        for tile in stairs:
            if self.rect.colliderect(tile):
                self.centery -= 1
                self.rect.centery = self.centery
                return

        if self.movingRight:
            self.centerx += .25
            self.rect.centerx = self.centerx
        if self.movingLeft:
            self.centerx -= .25
            self.rect.centerx = self.centerx



    def blitme(self):
        self.screen.blit(self.mario_image, self.rect)
