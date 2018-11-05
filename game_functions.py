import sys
import pygame


def checkKeydownEvents(event, mario):
    if event.key == pygame.K_RIGHT:
        mario.movingRight = True
    elif event.key == pygame.K_LEFT:
        mario.movingLeft = True

def checkKeyupEvents(event, mario):
    if event.key == pygame.K_RIGHT:
        mario.movingRight = False
    elif event.key == pygame.K_LEFT:
        mario.movingLeft = False

def check_events(ai_settings, screen, mario):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeydownEvents(event, mario)
        elif event.type == pygame.KEYUP:
            checkKeyupEvents(event, mario)




def update_screen(ai_settings, screen, mario, map):
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)

    mario.blitme()

    map.blitme()

    pygame.display.flip()

