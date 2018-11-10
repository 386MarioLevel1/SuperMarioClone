import pygame
from pygame.sprite import Group
from mario import Mario
from goomba import Goomba
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
    # pitfalls = Group()
    smallPitfalls = Group()
    largePitfalls = Group()
    goombas = Group()

    mario = Mario(screen, ai_settings)
    # goomba = Goomba(screen, ai_settings)
    map = Map(screen, ai_settings, "map/MarioLevel.txt", "OWfloor", floor, "OWstair", stairs, floor2,
              "pitfallS", smallPitfalls, "pitfallX", largePitfalls, goombas)

    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, mario, map)
        mario.update(floor, stairs, smallPitfalls, largePitfalls)
        map.update(floor, stairs, floor2, smallPitfalls, largePitfalls)
        floor.update()
        floor2.update()
        stairs.update()
        smallPitfalls.update()
        largePitfalls.update()
        gf.update_screen(ai_settings, screen, mario, map, floor, stairs, floor2,
                         smallPitfalls, largePitfalls, goombas)


run_game()