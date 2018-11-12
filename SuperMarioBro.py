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
    clouds = Group()
    bushes = Group()
    mysteryBoxes = Group()
    bricks = Group()
    flag = Group()
    castle = Group()
    mountains = Group()
    # pitfalls = Group()
    smallPitfalls = Group()
    largePitfalls = Group()
    goombas = Group()

    mario = Mario(screen, ai_settings)
    # goomba = Goomba(screen, ai_settings)
    map = Map(screen, ai_settings, "map/MarioLevel.txt", "OWfloor", floor, "OWstair", stairs, floor2,
              "pitfallS", smallPitfalls, "pitfallX", largePitfalls, goombas, "OWcloud", clouds, "OWbush", bushes, "OWblock1", mysteryBoxes, "OWbrick", bricks, "OWflagPoleTop", "OWflagPolePart", flag, "OWcastleTop", "OWcastleTop2", "OWcastleDoorTop", "OWcastleDoorPart", castle, mountains)

    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, mario, map)
        mario.update(floor, stairs, smallPitfalls, largePitfalls)
        map.update(floor, stairs, floor2, smallPitfalls, largePitfalls, clouds, bushes, mysteryBoxes, bricks, flag, castle, mountains)
        floor.update()
        floor2.update()
        stairs.update()
        smallPitfalls.update()
        largePitfalls.update()
        clouds.update()
        bushes.update()
        mysteryBoxes.update()
        bricks.update()
        flag.update()
        castle.update()
        mountains.update()
        gf.update_screen(ai_settings, screen, mario, map, floor, stairs, floor2,
                         smallPitfalls, largePitfalls, goombas, clouds, bushes, mysteryBoxes, bricks, flag, castle, mountains)


run_game()