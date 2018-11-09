class Goomba:
    def __init__(self, screen, ai_settings):
        super(Goomba, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.goombaImage = pygame.image.load("enemyImages/Goomba0.png")
        self.mario_image = pygame.transform.scale(self.mario_image, (32, 32))
        self.rect = self.goombaImage.get_rect()
        self.screen_rect = screen.get_rect()

