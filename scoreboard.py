import pygame.font
from pygame.sprite import Group

from mario import Mario

class Scoreboard():
    """A class to report scoring information."""
    def __init__(self, ai_settings, screen):
        """Initialize scorekeeping attributes."""
        self.screen = screen

        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        # self.stats = stats

        # Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 24)

        # Prepare the initial score images.

        self.prep_MARIO()
        self.prep_score()

        # use this for coins
        self.prep_coins()
        self.prep_coinCounts()
        # self.prep_ships()
        #

        self.prep_TIME()
        self.prep_seconds()

        self.prep_WORLD()
        self.prep_level()

    # prep_coins instead vvv
    def prep_MARIO(self):
        self.MARIO_image = self.font.render("MARIO", True,
            self.text_color, self.ai_settings.bg_color)

        self.MARIO_rect = self.MARIO_image.get_rect()
        self.MARIO_rect.left = self.screen_rect.left + 64
        self.MARIO_rect.top = 20

    def prep_score(self):
        self.score_image = self.font.render("000000", True, self.text_color,
                                                self.ai_settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 64
        self.score_rect.top = self.MARIO_rect.bottom

    def prep_coins(self):
        # you can make self.coin_color instead of using self.text_color
        # make the 0 yellow
        self.coin_image = self.font.render("0", True, self.text_color,
                                            self.ai_settings.bg_color)
        self.coin_rect = self.coin_image.get_rect()
        self.coin_rect.left = self.score_rect.right + 32
        self.coin_rect.top = self.MARIO_rect.bottom

        # Elmer this may or may not help
        # self.marios = Group()
        # # self, screen, ai_settings
        # mario = Mario(self.screen, self.ai_settings)
        # mario.rect.left = self.score_rect.right + 32
        # mario.rect.top = self.score_rect.top
        # self.marios.add(mario)

    def prep_coinCounts(self):
        self.coinCount_image = self.font.render("x 00", True, self.text_color,
                                           self.ai_settings.bg_color)
        self.coinCount_rect = self.coinCount_image.get_rect()
        self.coinCount_rect.left = self.coin_rect.right + 10
        self.coinCount_rect.top = self.MARIO_rect.bottom

    def prep_WORLD(self):
        self.WORLD_image = self.font.render("World", True, self.text_color,
                                                self.ai_settings.bg_color)
        self.WORLD_rect = self.WORLD_image.get_rect()
        self.WORLD_rect.right = self.TIME_rect.left - 32
        self.WORLD_rect.bottom = self.MARIO_rect.bottom

    def prep_level(self):
        self.level_image = self.font.render("1-1", True, self.text_color,
                                            self.ai_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.TIME_rect.left - 32
        self.level_rect.top = self.MARIO_rect.bottom

    def prep_TIME(self): #hold up
        self.TIME_image = self.font.render("TIME", True, self.text_color,
                                                self.ai_settings.bg_color)
        self.TIME_rect = self.TIME_image.get_rect()
        self.TIME_rect.right = self.screen_rect.right - 64
        self.TIME_rect.top = self.MARIO_rect.top

    def prep_seconds(self):
        self.seconds_image = self.font.render("500", True, self.text_color,
                                           self.ai_settings.bg_color)
        self.seconds_rect = self.seconds_image.get_rect()
        self.seconds_rect.right = self.screen_rect.right - 64
        self.seconds_rect.top = self.MARIO_rect.bottom


    def show_score(self):
        """Draw scores and ships to the screen."""
        self.screen.blit(self.MARIO_image, self.MARIO_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.coin_image, self.coin_rect)
        self.screen.blit(self.coinCount_image, self.coinCount_rect)

        self.screen.blit(self.TIME_image, self.TIME_rect)
        self.screen.blit(self.WORLD_image, self.WORLD_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.seconds_image, self.seconds_rect)
        # self.screen.blit(self.score_image, self.score_rect)
        # self.screen.blit(self.high_score_image, self.high_score_rect)
        # self.screen.blit(self.level_image, self.level_rect)
        # Draw ships.
        # self.marios.draw(self.screen)