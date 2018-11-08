import sys
import pygame


def checkKeydownEvents(event, mario, map):
    if event.key == pygame.K_RIGHT:
        # mario.movingRight = True
        map.movingRight = True
    elif event.key == pygame.K_LEFT:
        # mario.movingLeft = True
        map.movingLeft = True
    elif event.key == pygame.K_SPACE:
        mario.jump = True

def checkKeyupEvents(event, mario, map):
    if event.key == pygame.K_RIGHT:
        # mario.movingRight = False
        map.movingRight = False
    elif event.key == pygame.K_LEFT:
        # mario.movingLeft = False
        map.movingLeft = False
    elif event.key == pygame.K_SPACE:
        mario.jump = False

def check_events(ai_settings, screen, mario, map):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeydownEvents(event, mario, map)
        elif event.type == pygame.KEYUP:
            checkKeyupEvents(event, mario, map)

def update_screen(ai_settings, screen, mario, map, floor, stairs):
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)

    mario.blitme()

    map.blitme(floor, stairs)

    pygame.display.flip()

