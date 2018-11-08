import pygame
from pygame.sprite import Group
from mario import Mario
from map import Map
from settings import Settings

import game_functions as gf

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Super Mario Bros.")

    floor = Group()
    floor2 = Group()
    stairs = Group()
    pitfalls = Group()

    mario = Mario(screen, ai_settings)
    map = Map(screen, "map/MarioLevel.txt", "OWfloor", floor, "OWstair", stairs, floor2, )

    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, mario, map)
        mario.update(floor, stairs)
        map.update(floor, stairs, floor2)
        floor.update()
        floor2.update()
        stairs.update()
        gf.update_screen(ai_settings, screen, mario, map, floor, stairs, floor2)


run_game()