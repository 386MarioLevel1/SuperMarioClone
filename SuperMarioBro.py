import pygame
from pygame.sprite import Group
from settings import Settings

import game_functions as gf

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Super Mario Bro")

    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen)

        gf.update_screen(ai_settings, screen)


run_game()